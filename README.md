<p align="center">
  <img src="https://img.shields.io/badge/Platform-Android%20%7C%20Web-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Stack-Flutter%20%7C%20FastAPI%20%7C%20Next.js-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/AI-OR--Tools%20%7C%20Gemini%20%7C%20Sentinel--2-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" />
</p>

<h1 align="center">🌾 ParaliSetu — ਪਰਾਲੀ ਸੇਤੁ</h1>

<p align="center">
  <strong>Voice-First Stubble Management Platform for Punjab Farmers</strong><br/>
  <em>Eliminating parali burning by connecting farmers, balers, trucks, and biomass buyers in one tap</em>
</p>

<p align="center">
  <a href="#-the-problem">Problem</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-features">Features</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-environment-variables">Env Vars</a> •
  <a href="#-api-reference">API</a> •
  <a href="#-ai--ml-models">AI & ML</a> •
  <a href="#-testing">Testing</a>
</p>

---

## 🚨 The Problem

Every October–November, **Punjab, Haryana, and UP farmers** burn **20+ million tonnes** of paddy stubble (*parali*). Not out of choice — but because they have only **10–15 days** between rice harvest and the next wheat sowing, and no affordable, convenient alternative.

The resulting smoke is a **primary cause of hazardous air quality** choking Delhi-NCR for weeks.

| The Reality | The Numbers |
|---|---|
| Stubble burned annually in Punjab alone | ~20 million tonnes |
| Farmers fined by CAQM | ₹2,500–₹15,000 per incident |
| Total residue per acre (PAU Ludhiana research) | ~3.6 tonnes |
| Baler-recoverable tradable stubble | ~2.0–2.2 tonnes/acre |
| Market value of stubble as biomass feedstock | ₹900–₹1,600/tonne |
| **Potential income per acre — wasted by burning** | **₹1,800–₹3,200** |

**Government fines without alternatives only punish farmers.** ParaliSetu creates the alternative.

---

## ✅ The Solution

**ParaliSetu** (*"parali bridge"*) is a **voice-first, trilingual Android app** that removes every barrier between a farmer and a complete stubble-management deal **in a single tap**.

```
Farmer speaks in Punjabi/Hindi
        ↓
App estimates stubble yield & income (PAU agronomic formula)
        ↓
OR-Tools CP-SAT matches farmer with baler + truck + buyer
        ↓
One-tap booking, buyer escrow holds payment
        ↓
Dharamkanta weighbridge slip confirms actual weight
        ↓
Payment released. Sentinel-2 satellite verifies no burning.
        ↓
No-Burn Certificate issued. CO₂ credits logged.
```

---

## 🏗️ Architecture

```
┌────────────────────────────────┐      ┌──────────────────────────────────┐
│   Farmer Mobile App (Flutter)  │      │  Operations Web Portal (Next.js) │
│  • Punjabi / Hindi / English   │      │  • Biomass Buyers (Set Demand)   │
│  • Voice Intake + OTP Login    │      │  • Weighbridge Ticket Entry      │
│  • Stubble Estimate + Booking  │      │  • KVK Subsidy & Hotspot Map     │
│  • SMS notifications           │      │  • Admin Dashboards              │
└───────────────┬────────────────┘      └──────────────────┬───────────────┘
                │                                          │
                └───────────────────┬──────────────────────┘
                                    ▼
                     ┌──────────────────────────────┐
                     │     FastAPI Central Backend   │
                     │  • JWT Auth & Phone OTP       │
                     │  • OR-Tools Matching Engine   │
                     │  • Stubble Agronomic Logic    │
                     │  • PostGIS Geo-Queries        │
                     │  • Cashfree Escrow Payments   │
                     │  • Fast2SMS Notifications     │
                     └──────────────┬───────────────┘
                                    ▼
                     ┌──────────────────────────────┐
                     │  Supabase PostgreSQL+PostGIS  │
                     │  • 12 Normalized Tables       │
                     │  • Row-Level Security (RLS)   │
                     │  • Real-time subscriptions    │
                     └──────────────────────────────┘
```

### Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Mobile App** | Flutter 3.x (Dart) | Trilingual farmer app (EN/HI/PA) |
| **Web Portal** | Next.js 14 + TypeScript | Buyer, operator, and KVK dashboards |
| **Backend API** | FastAPI + Python 3.11 | Core business logic, auth, matching |
| **Database** | PostgreSQL + PostGIS (Supabase) | 12-table normalized schema with RLS |
| **ORM** | SQLAlchemy 2.0 + Alembic | Database models and migrations |
| **Auth** | FastAPI + PyJWT + Phone OTP | 60-min access tokens, 30-day refresh |
| **AI Optimization** | Google OR-Tools CP-SAT | Multi-constraint logistics matching |
| **Voice AI** | Sarvam AI / Bhashini ASR + Gemini 1.5 Flash | Punjabi/Hindi speech-to-structured-data |
| **Satellite** | Copernicus Sentinel-2 SWIR (CDSE) | Post-harvest burn verification (NBR) |
| **Payments** | Cashfree Payouts API | Escrow hold + real farmer payouts |
| **SMS** | Fast2SMS | OTP delivery + booking notifications |
| **Mapping** | MapBox GL | Field location and route visualization |

---

## 🎯 Multi-Stakeholder Design

ParaliSetu serves **6 distinct stakeholders**, each with a tailored interface:

| Stakeholder | Interface | Core Value |
|---|---|---|
| 🌾 **Marginal Farmer (Kisaan)** | Flutter App (Voice-first) | Speak crop details → get cash, skip burning |
| 👥 **Kisan Mitra** | Flutter App (Agent Mode) | Help illiterate farmers book on their behalf |
| 🏭 **Biomass Buyer** (Bio-CNG/Pellet Plants) | Next.js Web Portal | Set daily demand & price, guaranteed supply via escrow |
| 🚜 **Baler & Truck Owners** | Next.js Portal + SMS | Get clustered 25–40 acre runs, maximize utilization |
| ⚖️ **Dharamkanta (Weighbridge)** | Mobile browser form | Fast gross/tare entry with OCR anti-fraud |
| 🏛️ **KVK / Agriculture Officer** | Admin Dashboard | Burn hotspot map, compliance tracking, subsidy approval |

---

## ✨ Features

### ✅ BUILT (Production Ready)

- **📱 Trilingual Flutter App** — English, Hindi, Punjabi (120+ native strings, zero placeholder text)
- **🔐 Phone OTP Authentication** — Real SMS via Fast2SMS; 6-digit OTP, 5-minute expiry
- **💾 Persistent Session Login** — Auto-restore on app restart (no re-OTP required)
- **🌾 Stubble Yield Estimator** — PAU Ludhiana agronomic formula, variety-specific (PR-126, Pusa-44, Basmati)
- **🗺️ Field Details Screen** — Acres, variety, harvest date, GPS coordinates
- **📦 Booking System** — State machine: `requested` → `confirmed` → `in_progress` → `completed`
- **💰 Escrow Payment** — Cashfree-backed escrow hold; released on weighbridge confirmation
- **📲 Real SMS Notifications** — Farmer notified via SMS on escrow release (Fast2SMS)
- **🎓 3-Slide Onboarding** — Localized in all 3 languages
- **🏆 No-Burn Certificate Screen** — CO₂ and PM₂.₅ avoided calculation
- **🌐 Web Portal** — Buyer portal, KVK dashboard (Next.js)
- **🗄️ 12-Table Database Schema** — PostgreSQL + PostGIS, full RLS on all tables
- **🧪 Test Suite** — 35/35 pytest passes + Flutter widget tests

### 🔄 PLANNED (Architecture Designed, Not Yet Deployed)

- **🎤 Voice Intake** — Sarvam AI ASR + Gemini 1.5 Flash entity extraction (UI mic placeholder built)
- **🤖 OR-Tools Matching Engine** — CP-SAT multi-constraint optimization (scaffolded)
- **🛰️ Satellite Burn Verification** — Sentinel-2 SWIR NBR via Copernicus CDSE
- **📊 Weighbridge OCR** — Anti-fraud gross/tare slip validation
- **🔔 Push Notifications** — Firebase FCM for real-time alerts
- **📈 Self-Improving Yield Model** — Ridge regression calibration from actual weighbridge data

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Flutter 3.x (`flutter doctor` must be clean)
- Node.js 18+ and npm
- PostgreSQL 15+ with PostGIS extension (or Supabase account)
- Android device or emulator

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/parali-setu.git
cd parali-setu
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy and configure environment variables
cp .env.example .env
# Edit .env with your actual values (see Environment Variables section)

# Run database migrations
alembic upgrade head

# Start the backend server
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at `http://localhost:8000`
Interactive docs: `http://localhost:8000/docs`

### 3. Flutter App Setup

```bash
cd app

# Get Flutter dependencies
flutter pub get

# Connect Android device (USB debugging ON) or start emulator
adb devices

# Run in debug mode
flutter run

# Build release APK (arm64, ~17 MB)
cd android && .\gradlew --stop   # Clear Gradle daemon (Windows)
cd ..
flutter build apk --release --split-per-abi --target-platform android-arm64
```

### 4. Web Portal Setup

```bash
cd web/portal    # or web/buyer-portal / web/kvk-dashboard
npm install
npm run dev
```

---

## 🔑 Environment Variables

Copy `backend/.env.example` to `backend/.env`. **Never commit `.env` to version control.**

### Database

| Variable | Example | Description |
|---|---|---|
| `DATABASE_URL` | `postgresql+psycopg2://user:pass@host:5432/paralisetu` | PostgreSQL connection string. Use Supabase pooler URL (port 6543) for production |

### JWT Authentication

| Variable | Default | Description |
|---|---|---|
| `JWT_SECRET_KEY` | *(none)* | **MUST be ≥32 chars in production.** Generate: `openssl rand -hex 32` |
| `JWT_ALGORITHM` | `HS256` | JWT signing algorithm |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | `60` | Access token lifetime |
| `REFRESH_TOKEN_EXPIRE_DAYS` | `30` | Refresh token lifetime |

### OTP / SMS (Fast2SMS)

| Variable | Description | How to Get |
|---|---|---|
| `FAST2SMS_API_KEY` | Fast2SMS Dev API key | [fast2sms.com](https://fast2sms.com) → Dashboard → Dev API |
| `OTP_PROVIDER` | `fast2sms` / `firebase` / `msg91` | Choose SMS provider |
| `MSG91_AUTH_KEY` | MSG91 Auth Key (alternative) | [msg91.com](https://msg91.com) → API |
| `FIREBASE_PROJECT_ID` | Firebase project ID | Firebase Console → Project Settings |
| `FIREBASE_SERVICE_ACCOUNT_JSON` | Path to service account JSON | Firebase Console → Service Accounts |

### Demo / Development Mode

| Variable | Default | Description |
|---|---|---|
| `DEBUG` | `false` | Enable debug logging (`true` for local dev) |
| `DEMO_MODE` | `false` | When `true`, OTP `123456` accepted for DEMO_PHONES only |
| `DEMO_PHONES` | *(empty)* | Comma-separated E.164 numbers allowed to use demo OTP |

> ⚠️ **NEVER set `DEMO_MODE=true` in production.**

### AI & Satellite

| Variable | Description | How to Get |
|---|---|---|
| `SARVAM_API_KEY` | Sarvam AI ASR for Punjabi/Hindi voice | [sarvam.ai](https://sarvam.ai) → API Keys |
| `BHASHINI_API_KEY` | Bhashini ASR (government alternative) | [bhashini.gov.in](https://bhashini.gov.in) → Developer Portal |
| `BHASHINI_USER_ID` | Bhashini User ID | Same portal |
| `FIRMS_MAP_KEY` | NASA FIRMS fire hotspot data | [firms.modaps.eosdis.nasa.gov](https://firms.modaps.eosdis.nasa.gov/api/area/) → Map Key (free) |
| `CDSE_CLIENT_ID` | Copernicus CDSE OAuth Client ID | [dataspace.copernicus.eu](https://dataspace.copernicus.eu) → User Profile → OAuth Clients |
| `CDSE_CLIENT_SECRET` | Copernicus CDSE Client Secret | Same portal → create OAuth client |

> **About Copernicus CDSE:** EU Copernicus Data Space Ecosystem. Register at dataspace.copernicus.eu → User Profile → OAuth Clients → Create client → copy ID & Secret. Used for Sentinel-2 satellite imagery to verify post-harvest burn status.

> **About NASA FIRMS:** Free fire/burn hotspot data from MODIS & VIIRS satellites. Register for a free Map Key at firms.modaps.eosdis.nasa.gov.

### Payments (Cashfree)

| Variable | Description | How to Get |
|---|---|---|
| `PAYMENT_PROVIDER` | `mock` (dev) or `cashfree` (prod) | — |
| `CASHFREE_CLIENT_ID` | Cashfree Payment Gateway App ID | [merchant.cashfree.com](https://merchant.cashfree.com) → API Keys |
| `CASHFREE_CLIENT_SECRET` | Cashfree Payment Gateway Secret | Same dashboard |
| `CASHFREE_PAYOUT_CLIENT_ID` | Cashfree Payouts (farmer disbursement) | Cashfree → Payouts section |
| `CASHFREE_PAYOUT_SECRET` | Cashfree Payouts Secret | Same |

### Mapping & Routing

| Variable | Description | How to Get |
|---|---|---|
| `MAPBOX_API_KEY` | MapBox GL access token | [account.mapbox.com](https://account.mapbox.com) → Tokens |
| `OSRM_BASE_URL` | OSRM routing server URL | Default: `http://router.project-osrm.org` (free public) |

### Flutter App Config

Update `app/lib/constants.dart`:

```dart
// Local development (Android emulator)
const String kBaseUrl = 'http://10.0.2.2:8000';

// Local development (Physical device — use your PC's LAN IP)
const String kBaseUrl = 'http://192.168.x.x:8000';

// Production
const String kBaseUrl = 'https://your-backend.onrender.com';
```

---

## 📡 API Reference

Base URL: `http://localhost:8000/api/v1`

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/auth/otp/send` | Send OTP to phone number |
| `POST` | `/auth/otp/verify` | Verify OTP → returns JWT access + refresh tokens |
| `POST` | `/auth/token/refresh` | Refresh expired access token |
| `GET` | `/auth/me` | Get current user profile |
| `PATCH` | `/auth/me` | Update profile (name, language, role) |

### Estimates & Farmers

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/farmers/profile` | Get farmer profile |
| `POST` | `/estimates/` | Create stubble yield estimate |
| `GET` | `/estimates/{id}` | Get estimate details |

### Matching & Booking

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/matching/run` | Run OR-Tools matching for estimate |
| `GET` | `/bookings/` | List farmer bookings |
| `POST` | `/bookings/` | Create booking |
| `PATCH` | `/bookings/{id}` | Update booking state |
| `POST` | `/bookings/{id}/release-escrow` | Release escrow + send SMS to farmer |

### Voice AI

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/voice/parse` | Parse Punjabi/Hindi voice transcript to structured JSON |

### Health

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/health` | Backend health check |

> 📚 Full interactive docs: `http://localhost:8000/docs` (Swagger UI)

---

## 🤖 AI & ML Models

### Model 1: Vernacular Voice Intake (ASR + Gemini 1.5 Flash)

**Status:** 🔄 PLANNED — UI mic button scaffolded; system prompt designed

- **ASR:** Sarvam AI or Bhashini converts Punjabi/Hindi speech → text
- **LLM:** Gemini 1.5 Flash extracts structured crop entities from vernacular text

**System prompt (entity extraction):**
```
You are an expert vernacular agricultural parser for Punjab and Haryana farmers.
Convert voice transcripts in Punjabi, Hindi, or Hinglish into structured JSON.
Rules:
- 1 Killa = 1.0 Acre | 1 Bigha (Punjab) = 0.20 Acre
- Map variety to: 'PR-126', 'Pusa-44', 'Basmati', or 'other'
- Parse relative dates ('parso', 'kal', '25 tareek') relative to today
Return ONLY valid JSON: { acres, variety, harvest_date (YYYY-MM-DD), confidence }
```

**Safety guardrail:** App always speaks back parsed result for farmer confirmation:
> *"Aapne bola: 4 Killa PR-126, 25 October. Sahi hai?"* → [Confirm] [Retry]

### Model 2: Logistics Matching (Google OR-Tools CP-SAT)

**Status:** ✅ BUILT — Scaffolded in `backend/app/services/matching.py`

Solves: **Farmers ↔ Balers ↔ Trucks ↔ Biomass Buyers** multi-sided matching.

**Decision variable:** `x[i,j,k,m] ∈ {0,1}` — Farmer i served by baler j, truck k, buyer m

**Constraints:**
1. Time window: `harvest_date ≤ baling_date ≤ delivery_date ≤ sowing_deadline`
2. Operating radius: baler within 25 km, buyer within 60 km
3. Contiguous clustering: group neighboring fields into 25–40 acre baler runs

**Objective:** Maximize farmer net earnings + minimize logistics deadhead distance

### Model 3: Stubble Yield Estimator (PAU Agronomic Formula)

**Status:** ✅ BUILT

```python
YIELD_FACTOR = {
    # Recoverable dry baled stubble (tonnes/acre)
    "PR-126":  {"combine": 2.0, "manual": 1.2},   # 123-day short duration
    "Pusa-44": {"combine": 2.5, "manual": 1.5},   # 160-day long duration
    "Basmati": {"combine": 1.5, "manual": 0.9},   # Softer straw
    "other":   {"combine": 2.0, "manual": 1.2},
}
YIELD_RANGE_LOW  = 0.80   # -20% lower boundary
YIELD_RANGE_HIGH = 1.20   # +20% upper boundary
```

> **Ironclad Rule:** The estimate is only for logistics sizing. **Final payment uses actual Dharamkanta weighbridge net weight — never the formula.**

### Model 4: Satellite Burn Verification (Sentinel-2 SWIR NBR)

**Status:** 🔄 PLANNED

```
NBR = (Band 8 NIR − Band 12 SWIR) / (Band 8 NIR + Band 12 SWIR)
ΔNBR = NBR_pre_harvest − NBR_post_harvest

ΔNBR < 0.10  →  No burn detected  →  Issue No-Burn Certificate ✅
ΔNBR ≥ 0.10  →  Burn detected     →  Alert KVK officer ⚠️
```

### Model 5: Self-Improving Yield Calibration

**Status:** 🔄 PLANNED

Ridge regression continuously refines district-level yield estimates using actual weighbridge slip data, improving prediction accuracy over successive paddy seasons.

---

## 📊 Database Schema

12 core tables, Row-Level Security on all:

| Table | Purpose |
|---|---|
| `users` | All users: phone, role, language |
| `farmer_profiles` | Extended farmer data, GPS location |
| `fields` | Farm fields with PostGIS geometry |
| `estimates` | Stubble yield calculations |
| `machine_owners` | Baler/tractor profiles + availability |
| `truck_owners` | Logistics profiles + capacity |
| `buyers` | Biomass buyer demand & pricing |
| `bookings` | Booking lifecycle state machine |
| `weighbridge_tickets` | Gross/tare/net weight entries |
| `payments` | Escrow hold + release records |
| `satellite_checks` | Sentinel-2 verification results |
| `certificates` | No-Burn Certificate records |

> Schema: `backend/alembic/versions/0001_initial_schema.py`

---

## 🧪 Testing

### Backend Tests

```bash
cd backend
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pytest                  # Run all 35 tests
pytest -v               # Verbose output
pytest tests/test_auth.py -v   # Single file
```

**Current status: ✅ 35/35 passing**

### Flutter Tests

```bash
cd app
flutter analyze         # Static analysis (must be clean)
flutter test            # Run widget tests
flutter test --reporter expanded   # Verbose
```

**Current status: ✅ All tests passing**

### Manual End-to-End (Golden Path)

| Step | Action | Expected Result |
|---|---|---|
| 1 | Launch app → Select language | Onboarding screens appear in selected language |
| 2 | Enter phone number → OTP login | Real SMS OTP received; 6-digit entry works |
| 3 | View Home screen | Localized greeting with farmer name |
| 4 | Enter: 4 acres, PR-126, harvest date | Field details saved |
| 5 | View Stubble Estimate | Total ~14.4 t, Baled ~8.0 t, Income ~₹9,600 |
| 6 | Tap "Book Pickup" | Booking created, escrow held |
| 7 | Release escrow (web portal) | Farmer receives SMS in Punjabi/Hindi |

### Demo Credentials (Dev Only)

```env
DEMO_MODE=true
DEMO_PHONES=+91XXXXXXXXXX
# Demo OTP: 123456 (whitelisted phones only)
```

---

## 📁 Project Structure

```
parali-setu/
├── app/                          # Flutter mobile app
│   ├── lib/
│   │   ├── main.dart             # App entry point
│   │   ├── constants.dart        # API base URL, config
│   │   ├── theme.dart            # Design system & colors
│   │   ├── l10n/app_strings.dart # Trilingual strings (EN/HI/PA)
│   │   ├── models/               # Dart data models
│   │   ├── repositories/         # API + mock data layer
│   │   ├── screens/              # 11 app screens
│   │   └── widgets/              # Reusable UI components
│   ├── android/                  # Android build config
│   ├── pubspec.yaml              # Flutter dependencies
│   └── test/                     # Widget tests
│
├── backend/                      # FastAPI backend
│   ├── app/
│   │   ├── main.py               # FastAPI app factory
│   │   ├── api/
│   │   │   ├── auth.py           # OTP + JWT auth
│   │   │   ├── bookings.py       # Booking lifecycle + escrow
│   │   │   ├── estimates.py      # Stubble yield estimation
│   │   │   ├── farmers.py        # Farmer profile CRUD
│   │   │   ├── matching.py       # OR-Tools matching trigger
│   │   │   └── voice.py          # Voice AI endpoint
│   │   ├── core/
│   │   │   ├── config.py         # Pydantic settings + secret guard
│   │   │   └── stubble_config.py # PAU yield factors
│   │   ├── models/               # SQLAlchemy ORM models
│   │   ├── schemas/              # Pydantic request/response schemas
│   │   └── services/
│   │       ├── matching.py       # OR-Tools CP-SAT engine
│   │       └── otp_provider.py   # Fast2SMS integration
│   ├── alembic/                  # Database migrations
│   ├── tests/                    # Pytest test suite (35 tests)
│   ├── .env.example              # Environment variable template
│   └── requirements.txt          # Python dependencies
│
├── web/                          # Next.js web portals
│   ├── portal/                   # Main operations portal
│   ├── buyer-portal/             # Biomass buyer dashboard
│   └── kvk-dashboard/            # KVK officer dashboard
│
├── docs/
│   ├── ROADMAP.md                # ⭐ Living source of truth (read first!)
│   └── screenshots/              # Device verification screenshots
│
├── SPEC.md                       # Full product specification
├── AGENTS.md                     # AI coding agent directives
├── render.yaml                   # Render.com deployment config
└── README.md                     # This file
```

---

## 🚀 Deployment

### Backend — Render.com

The `render.yaml` in the root enables one-click deployment:

1. Push code to GitHub
2. Connect repo to [render.com](https://render.com)
3. Set all environment variables in the Render dashboard
4. Render auto-deploys on every push to `main`

### Flutter App — Release APK

```bash
cd app/android
.\gradlew --stop    # Clear Gradle daemon (required on Windows)

cd ..
flutter build apk --release --split-per-abi --target-platform android-arm64
# Output: build/app/outputs/flutter-apk/app-arm64-v8a-release.apk (~17 MB)
```

### Database — Supabase

1. Create project at [supabase.com](https://supabase.com)
2. Enable PostGIS: Database → Extensions → `postgis`
3. Set `DATABASE_URL` to the **connection pooler** URL (port 6543, pgBouncer)
4. Run `alembic upgrade head` from `backend/`

---

## 🌍 Environmental Impact

When a farmer uses ParaliSetu instead of burning:

| Metric | Per Acre | Per 10-Acre Farm |
|---|---|---|
| CO₂ avoided | ~3.0 tonnes | ~30 tonnes |
| PM₂.₅ avoided | ~37.5 kg | ~375 kg |
| Farmer income earned | ₹1,800–₹3,200 | ₹18,000–₹32,000 |
| Biomass converted to biogas | ~2.0 tonnes | ~20 tonnes |

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feat/your-feature-name`
3. **Read `docs/ROADMAP.md` and `AGENTS.md` before writing any code**
4. Run tests before submitting: `pytest` (backend) and `flutter test` (app)
5. All tests must be **100% green** before opening a PR
6. Open a Pull Request against `main`

> ⚠️ **Never commit `.env`, JWT secrets, Supabase passwords, or API keys.**

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <strong>🌾 ParaliSetu — Bridging the gap between farmers and a cleaner future 🌾</strong>
</p>
