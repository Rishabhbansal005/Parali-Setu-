# Executive Summary: ParaliSetu
**Submission for: Hack for Social Hackathon | Theme: Environment & Sustainability**  
*Project Repository: [Rishabhbansal005/Parali-setu](https://github.com/Rishabhbansal005/Parali-setu) | Code Health: 100% Green Tests*

---

## 1. The Core Social & Environmental Crisis
Every October and November, North India faces a severe public health and environmental crisis. Over **20 million tonnes of paddy straw (parali)** are set on fire across Punjab, Haryana, and Western Uttar Pradesh within an acute **15-to-20 day window** between paddy harvest and wheat sowing.
*   **The Human Cost:** Air Quality Index (AQI) levels across the National Capital Region (NCR) surge past **500–600**, triggering a **300% spike in acute pediatric respiratory illnesses** and affecting over **50 million citizens**.
*   **The Economic Irony:** While farmers burn stubble because commercial balers refuse small 2-acre plots, industrial Bio-CNG (CBG) and 2G ethanol plants are shutting down their multi-crore boilers due to severe biomass feedstock shortages.

---

## 2. The Solution: ParaliSetu
**ParaliSetu is an AI-driven, hyperlocal biomass supply chain and digital escrow marketplace that bridges smallholder farmers, machinery owners, and industrial green-energy buyers.**

```
   [Marginal Farmer]                 [Baler Aggregator]             [Industrial Buyer]
           |                                  |                              |
 (Voice Intake in Punjabi)           (Contiguous Runs)            (Guaranteed Daily Feed)
           |                                  |                              |
           +------------------> [ PARALISETU ENGINE ] <----------------------+
                                       |
                     +-----------------+-----------------+
                     |                                   |
             [PostGIS Spatial]                  [Dharamkanta Scale]
          (15-25 km Clustering)                (Instant Escrow Payout)
```

### Core Technological Innovations:
1.  **Vernacular Voice AI Intake (Mobile App):** Eliminates rural digital literacy barriers. Farmers speak naturally in Punjabi or Hindi (*"4 killa PR-126, 25 October"*), which the system parses and confirms verbally with 1-tap confirmation.
2.  **PostGIS Spatial Clustering:** Solves the machinery operator's deadhead fuel crisis by grouping fragmented 1–3 acre plots into contiguous **30–50 acre operational runs**, reducing transit fuel overhead by 32%.
3.  **Dharamkanta Escrow Payouts (Next.js Portal):** Replaces middleman fraud with absolute transparency. Independent village weighbridge gross/tare scale tickets instantly trigger direct banking payouts to farmers within 24 hours.
4.  **Copernicus Sentinel-2 Satellite Verification:** Automated Normalized Burn Ratio (NBR) monitoring audits field coordinates to generate verifiable **No-Burn Certificates**, protecting farmers from government pollution fines.

---

## 3. Commercial Viability & Unit Economics
ParaliSetu is designed as a financially self-sustaining enterprise, not a grant-dependent charity:
*   **Market Mandate (SATAT & CBO):** The Ministry of Petroleum & Natural Gas has introduced a **mandatory Compressed Bio-Gas (CBG) blending obligation**, scaling from **1% in FY 2025–26 to 5% by FY 2028–29**. Industrial bio-energy plants *must* buy millions of tonnes of agricultural straw.
*   **Unit Economics per Tonne:**
    *   Industrial Gate Purchase Price: **₹2,600 / Tonne**
    *   Baler & Transportation Logistics: ₹1,550 / Tonne
    *   Farmer Stubble Cash Payout: **₹650 / Tonne (₹1,300 / Acre Net)**
    *   **ParaliSetu Platform Fee:** **₹150 / Tonne (5.8% Take-Rate paid by corporate buyers; 0% fee for farmers)**
*   **Break-Even Point:** With annual fixed overheads of ₹30 Lakhs, ParaliSetu reaches operational break-even at just **20,000 tonnes** (servicing ~10,000 acres in 1 district).
*   **3-Year Projections (Base Target):**
    *   *Year 1 (Pilot):* 25,000 Tonnes | ₹37.5L Revenue | ₹7.5L EBITDA
    *   *Year 2 (Expansion):* 250,000 Tonnes | ₹3.75 Cr Revenue | ₹2.77 Cr EBITDA
    *   *Year 3 (Scale):* 1,000,000 Tonnes | ₹15.00 Cr Revenue | **₹12.66 Cr EBITDA**

---

## 4. Measurable Social & Climate Impact
*   **Climate & Air:** At full 3-year scale, diverting 1,000,000 tonnes of stubble abates **1,200,000 tonnes of $\text{CO}_2\text{e}$** and eliminates **7.1 million kg of hazardous PM2.5** particulate matter from North Indian skies.
*   **Farmer Welfare:** Puts **₹50+ Crore** in direct cash payments into the hands of smallholders, while protecting them from CAQM punitive fines (₹5,000–₹15,000/acre).
*   **Circular Bio-Economy:** Provides reliable, moisture-tested feedstock to substitute imported fossil fuels with domestic Bio-CNG and 2G bio-ethanol.

---

## 5. Prototype Status & Readiness
Unlike conceptual ideas, ParaliSetu is an actively engineered, operational prototype:
*   **Mobile App (Flutter):** Fully functional on Android devices with vernacular voice intake, offline fallback parsing, and live escrow tracking.
*   **Backend & Spatial API (FastAPI + PostGIS):** 12 normalized database tables, PostGIS proximity queries, and JWT auth with **35/35 passing backend tests (100% green)**.
*   **Weighbridge Operations Portal (Next.js):** 3-second live synchronizer for Dharamkanta scale operators to verify shipments and release escrow funds.

**ParaliSetu transforms an annual environmental catastrophe into a self-funding, ₹260-crore rural bio-economy engine.**
