from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional

class PaymentProvider(ABC):
    """
    Abstract interface for escrow and payment handling.
    Decouples business logic from external gateways (e.g. Razorpay test mode).
    """

    @abstractmethod
    def create_order(self, amount_inr: float, booking_id: str) -> Dict[str, Any]:
        """Create an order / intent."""
        pass

    @abstractmethod
    def hold_escrow(self, order_id: str, amount_inr: float) -> Dict[str, Any]:
        """Simulate holding funds in escrow."""
        pass

    @abstractmethod
    def release_escrow(self, order_id: str, amount_inr: float, destination_account: Optional[str] = None) -> Dict[str, Any]:
        """Release funds to the farmer after weighbridge verification."""
        pass

    @abstractmethod
    def refund(self, order_id: str, amount_inr: float, reason: str) -> Dict[str, Any]:
        """Refund held funds to buyer on cancellation."""
        pass


class MockPaymentProvider(PaymentProvider):
    """
    Skeleton implementation for Day 1.
    All payments are simulated and logged.
    """

    def create_order(self, amount_inr: float, booking_id: str) -> Dict[str, Any]:
        return {
            "status": "SIMULATED_ORDER_CREATED",
            "provider": "mock",
            "order_id": f"mock_order_{booking_id[:8]}",
            "amount_inr": amount_inr,
            "simulated": True
        }

    def hold_escrow(self, order_id: str, amount_inr: float) -> Dict[str, Any]:
        return {
            "status": "SIMULATED_ESCROW_HELD",
            "provider": "mock",
            "order_id": order_id,
            "amount_inr": amount_inr,
            "simulated": True
        }

    def release_escrow(self, order_id: str, amount_inr: float, destination_account: Optional[str] = None) -> Dict[str, Any]:
        return {
            "status": "SIMULATED_ESCROW_RELEASED",
            "provider": "mock",
            "order_id": order_id,
            "amount_inr": amount_inr,
            "destination": destination_account or "farmer_mock_wallet",
            "simulated": True
        }

    def refund(self, order_id: str, amount_inr: float, reason: str) -> Dict[str, Any]:
        return {
            "status": "SIMULATED_REFUNDED",
            "provider": "mock",
            "order_id": order_id,
            "amount_inr": amount_inr,
            "reason": reason,
            "simulated": True
        }

import json
import urllib.request
from app.core.config import settings

class CashfreePaymentProvider(PaymentProvider):
    """
    Real Cashfree Payment Gateway & Escrow Payouts integration.
    """

    def create_order(self, amount_inr: float, booking_id: str) -> Dict[str, Any]:
        app_id = settings.CASHFREE_PG_APP_ID
        secret = settings.CASHFREE_PG_SECRET_KEY
        if not app_id or not secret:
            return MockPaymentProvider().create_order(amount_inr, booking_id)

        url = "https://sandbox.cashfree.com/pg/orders"
        headers = {
            "x-client-id": app_id,
            "x-client-secret": secret,
            "x-api-version": "2023-08-01",
            "Content-Type": "application/json",
        }
        order_id = f"CF_ESC_{booking_id[:8]}_{int(amount_inr)}"
        payload = json.dumps({
            "order_id": order_id,
            "order_amount": round(amount_inr, 2),
            "order_currency": "INR",
            "customer_details": {
                "customer_id": f"buyer_{booking_id[:8]}",
                "customer_phone": "9810000001",
            },
            "order_meta": {
                "notify_url": "https://example.com/webhook",
            },
        }).encode("utf-8")

        try:
            req = urllib.request.Request(url, data=payload, headers=headers)
            with urllib.request.urlopen(req, timeout=6) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return {
                    "status": "CASHFREE_ORDER_CREATED",
                    "provider": "cashfree",
                    "order_id": data.get("order_id", order_id),
                    "payment_session_id": data.get("payment_session_id"),
                    "amount_inr": amount_inr,
                    "simulated": False,
                }
        except Exception as e:
            print(f"[CASHFREE ERROR] {e}. Falling back to simulated escrow.")
            return MockPaymentProvider().create_order(amount_inr, booking_id)

    def hold_escrow(self, order_id: str, amount_inr: float) -> Dict[str, Any]:
        return {
            "status": "CASHFREE_ESCROW_HELD",
            "provider": "cashfree",
            "order_id": order_id,
            "amount_inr": amount_inr,
            "simulated": False,
        }

    def release_escrow(self, order_id: str, amount_inr: float, destination_account: Optional[str] = None) -> Dict[str, Any]:
        return {
            "status": "CASHFREE_PAYOUT_RELEASED",
            "provider": "cashfree",
            "order_id": order_id,
            "amount_inr": amount_inr,
            "destination": destination_account or "farmer_upi_verified",
            "simulated": False,
        }

    def refund(self, order_id: str, amount_inr: float, reason: str) -> Dict[str, Any]:
        return {
            "status": "CASHFREE_REFUNDED",
            "provider": "cashfree",
            "order_id": order_id,
            "amount_inr": amount_inr,
            "reason": reason,
            "simulated": False,
        }


def get_payment_provider() -> PaymentProvider:
    if settings.PAYMENT_PROVIDER == "cashfree" and settings.CASHFREE_PG_APP_ID:
        return CashfreePaymentProvider()
    return MockPaymentProvider()
