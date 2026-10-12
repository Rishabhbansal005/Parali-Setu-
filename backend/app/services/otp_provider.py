from __future__ import annotations
import json
import urllib.request
import urllib.error
from abc import ABC, abstractmethod
from typing import Any
from app.core.config import settings


class OtpDeliveryResult:
    def __init__(self, delivered: bool, provider: str, error: str = "", raw_response: Any = None):
        self.delivered = delivered
        self.provider = provider
        self.error = error
        self.raw_response = raw_response

    def __bool__(self) -> bool:
        return self.delivered


class OtpProvider(ABC):
    """Abstract base class for SMS/WhatsApp OTP delivery."""

    @abstractmethod
    def send_otp(self, phone_e164: str, otp: str) -> OtpDeliveryResult:
        """Deliver the OTP to the specified E.164 phone number."""
        pass

    @abstractmethod
    def send_sms(self, phone_e164: str, message: str) -> OtpDeliveryResult:
        """Deliver a transactional SMS notification (e.g. Escrow payment released)."""
        pass


class MockOtpProvider(OtpProvider):
    """
    Mock implementation for local development and tests.
    Prints the OTP to the console/logs instead of sending a real SMS.
    """

    def send_otp(self, phone_e164: str, otp: str) -> OtpDeliveryResult:
        print(f"\n==========================================")
        print(f" [MOCK OTP] Sent to: {phone_e164} | OTP: {otp}")
        print(f"==========================================\n")
        return OtpDeliveryResult(delivered=True, provider="mock")

    def send_sms(self, phone_e164: str, message: str) -> OtpDeliveryResult:
        print(f"\n==========================================")
        print(f" [MOCK SMS NOTIFICATION] Sent to: {phone_e164}")
        print(f" Message: {message}")
        print(f"==========================================\n")
        return OtpDeliveryResult(delivered=True, provider="mock")


class Fast2SmsOtpProvider(OtpProvider):
    """
    Real Indian SMS Gateway via Fast2SMS API.
    Sends authentic 6-digit OTP to farmer's mobile phone via Quick SMS / OTP route.
    """

    def send_otp(self, phone_e164: str, otp: str) -> OtpDeliveryResult:
        api_key = settings.FAST2SMS_API_KEY
        if not api_key:
            print(f" [MOCK OTP Fallback] To: {phone_e164} | OTP: {otp}")
            return OtpDeliveryResult(delivered=False, provider="fast2sms", error="FAST2SMS_API_KEY missing")

        # Extract 10-digit mobile number
        clean_phone = phone_e164.replace("+91", "").replace("+", "").strip()[-10:]
        url = "https://www.fast2sms.com/dev/bulkV2"
        headers = {
            "authorization": api_key,
            "Content-Type": "application/json",
        }
        body = json.dumps({
            "variables_values": otp,
            "route": "otp",
            "numbers": clean_phone,
        }).encode("utf-8")

        try:
            req = urllib.request.Request(url, data=body, headers=headers)
            with urllib.request.urlopen(req, timeout=8) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                print(f" [FAST2SMS REAL] Sent OTP {otp} to {clean_phone} | Response: {data}")
                is_ok = bool(data.get("return", False))
                return OtpDeliveryResult(delivered=is_ok, provider="fast2sms", raw_response=data)
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8")
            print(f" [FAST2SMS GATEWAY ERROR {e.code}] {err_body}")
            try:
                err_data = json.loads(err_body)
                err_msg = err_data.get("message", err_body)
            except Exception:
                err_msg = err_body
            return OtpDeliveryResult(delivered=False, provider="fast2sms", error=err_msg)
        except Exception as e:
            print(f" [FAST2SMS NETWORK ERROR] {e}. Falling back to console log.")
            return OtpDeliveryResult(delivered=False, provider="fast2sms", error=str(e))

    def send_sms(self, phone_e164: str, message: str) -> OtpDeliveryResult:
        api_key = settings.FAST2SMS_API_KEY
        if not api_key:
            print(f" [MOCK SMS Fallback] To: {phone_e164} | Message: {message}")
            return OtpDeliveryResult(delivered=False, provider="fast2sms", error="FAST2SMS_API_KEY missing")

        clean_phone = phone_e164.replace("+91", "").replace("+", "").strip()[-10:]
        url = "https://www.fast2sms.com/dev/bulkV2"
        headers = {
            "authorization": api_key,
            "Content-Type": "application/json",
        }
        body = json.dumps({
            "route": "q",
            "message": message,
            "numbers": clean_phone,
            "language": "english",
            "flash": 0,
        }).encode("utf-8")

        try:
            req = urllib.request.Request(url, data=body, headers=headers)
            with urllib.request.urlopen(req, timeout=8) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                print(f" [FAST2SMS NOTIFICATION REAL] Sent to {clean_phone} | Response: {data}")
                is_ok = bool(data.get("return", False))
                return OtpDeliveryResult(delivered=is_ok, provider="fast2sms", raw_response=data)
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8")
            print(f" [FAST2SMS NOTIFICATION GATEWAY ERROR {e.code}] {err_body}")
            try:
                err_data = json.loads(err_body)
                err_msg = err_data.get("message", err_body)
            except Exception:
                err_msg = err_body
            return OtpDeliveryResult(delivered=False, provider="fast2sms", error=err_msg)
        except Exception as e:
            print(f" [FAST2SMS NOTIFICATION NETWORK ERROR] {e}")
            return OtpDeliveryResult(delivered=False, provider="fast2sms", error=str(e))


def get_otp_provider() -> OtpProvider:
    if settings.OTP_PROVIDER == "fast2sms" and settings.FAST2SMS_API_KEY:
        return Fast2SmsOtpProvider()
    return MockOtpProvider()
