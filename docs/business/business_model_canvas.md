# ParaliSetu — Business Model Canvas (BMC)
**SEVA First Innovation Challenge 2026 (DTU & Govt. of NCT of Delhi) | Theme: Environment & Sustainability**  
*Grounded in the Open-Source Business Model Canvas Markdown Template*  
*Project Repository: [ParaliSetu](https://github.com/Rishabhbansal005/Parali-setu)*

---

```
+---------------------------------------------------------------------------------------------------------------------+
|                                              BUSINESS MODEL CANVAS                                                  |
+-------------------+--------------------+--------------------+-----------------------+-------------------------------+
| 8. KEY            | 6. KEY             | 2. VALUE           | 4. CUSTOMER           | 1. CUSTOMER                   |
|    PARTNERS       |    ACTIVITIES      |    PROPOSITIONS    |    RELATIONSHIPS      |    SEGMENTS                   |
|                   |                    |                    |                       |                               |
| • Bio-CNG/Ethanol | • PostGIS Spatial  | • Smallholders:    | • Vernacular Voice-   | • Beneficiaries:              |
|   Plants (SATAT)  |   Clustering       |   Free harvest     |   First Onboarding    |   Small & marginal farmers    |
| • Custom Hiring   | • Voice AI Intake  |   clearing, zero   |   (Punjabi/Hindi)     |   (1–4 acre paddy plots)      |
|   Centres (CHCs)  |   & Localization   |   penalties, cash  | • Dharamkanta Neutral | • Paying Customers:           |
| • Baler & Tractor | • Dharamkanta Scale|   at scale.        |   Assistance Desk     |   Industrial biomass buyers   |
|   Owners          |   Integration      | • Balers: Contigu- | • Dedicated Key       |   (Bio-CNG, pellets, boilers) |
| • Dharamkanta     | • Buyer Demand &   |   ous 30-acre runs,|   Account Manager for | • Supply Operators:           |
|   Weighbridges    |   Escrow Mgmt      |   +35% daily fuel  |   Industrial Offtakers|   Commercial baler owners     |
| • Punjab/Haryana  | • Sentinel-2 Burn  |   efficiency.      | • WhatsApp/SMS Status |   & rural tractor aggregators |
|   Agri Depts & KVK|   Audit Validation | • Buyers: Predict- |   Updates (No Smart-  | • Institutional Partners:     |
| • Oil Marketing   | • Ground FPO/Kisan |   able daily supply|   phone Requirement)  |   State Agri Depts, KVKs,     |
|   Companies (OMCs)|   Mitra Engagement |   moisture-tested  | • Rapid Dispute /     |   OMCs, and Carbon Registries |
|                   |                    |   at plant gate.   |   Grievance Redressal |                               |
+-------------------+--------------------+                    +-----------------------+                               +
| 7. KEY RESOURCES                       |                    | 3. CHANNELS                                           |
|                                        |                    |                                                       |
| • PostGIS Matching Engine              |                    | • Flutter Mobile App (Voice AI & Vernacular UI)       |
| • Vernacular Speech Model (Hindi/Pa)   |                    | • Next.js Operations Web Portal (Weighbridge/Buyer)   |
| • Ground Network of Baler Aggregators  |                    | • Village Custom Hiring Centres (CHCs) & Panchayats   |
| • PAU-Validated Agronomic Formula      |                    | • Local Dharamkanta Weighbridge Kiosks                |
| • Operational Escrow Contract Engine   |                    | • Direct Enterprise B2B Supply Contracts              |
+----------------------------------------+--------------------+-------------------------------------------------------+
| 9. COST STRUCTURE                                           | 5. REVENUE STREAMS                                    |
|                                                             |                                                       |
| • Tech Infrastructure: Supabase PostgreSQL/PostGIS, Cloud   | • Primary: B2B Offtake Commission (₹120–₹180/tonne    |
|   hosting, Whisper/Gemini API, SMS gateway.                 |   paid by industrial buyers; 0% farmer commission).   |
| • Ground Operations: Village Cluster Coordinators (Kisan    | • Secondary: Baler Route Optimization Fee (₹40/tonne  |
|   Mitras) during 20-day peak harvest season.                |   software fee on digitized aggregation runs).        |
| • Quality & Verification: Mobile moisture testers & spatial | • Institutional: Satellite Burn-Audit & ESG Tracking  |
|   Sentinel-2 verification pipelines.                        |   SaaS fees for district administrations & OMCs.      |
| • Sales & Corporate Integration: Industrial off-taker key   | • Future: Verifiable Voluntary Carbon Credits         |
|   account management & legal escrow integrations.           |   (0.5 tCO2e/tonne parali diverted from open fires).  |
+-------------------------------------------------------------+-------------------------------------------------------+
```

---

## Detailed Block-by-Block Analysis

### 1. Customer Segments
*   **Primary Beneficiaries (The Grassroots Kisaan):**
    *   *Profile:* Small and marginal farmers in Punjab (Majha, Malwa, Doaba) and Haryana (Karnal, Kurukshetra, Kaithal) with 1 to 5 acres of land cultivating non-Basmati paddy (PR-126, Pusa-44).
    *   *Pain & Needs:* Must clear thick stubble (~3.6 tonnes total residue, ~2.0 tonnes baler-recoverable per acre) in a narrow 15–20 day window to sow wheat. Fined ₹5,000–₹15,000 per violation under CAQM regulations.
    *   *Affordability:* Zero ability to purchase balers (which cost ₹14–₹18 Lakhs). Willingness to pay is strictly zero; they require free field clearance or cash payment for their straw.
*   **Paying Customers (Industrial Biomass Off-Takers):**
    *   *Profile:* Bio-CNG / CBG plants operating under the SATAT initiative (e.g., Sangrur 33 TPD plant), 2G bio-ethanol plants (IOCL Panipat), biomass pellet manufacturers, and industrial power boilers.
    *   *Pain & Needs:* Continuous, guaranteed daily feedstock (100–350 tonnes/day) with moisture < 18%. Supply disruptions shut down expensive digesters/boilers.
    *   *Willingness to Pay:* High. Current landed gate rate in Punjab/Haryana is ₹2,000–₹3,200/tonne of baled paddy straw. They willingly pay a ₹120–₹180/tonne digital aggregation premium for guaranteed, scheduled delivery.
*   **Supply Operators (Baler Owners & Tractor Aggregators):**
    *   *Profile:* Custom Hiring Centre (CHC) operators, progressive farmers, and rural transport entrepreneurs owning tractors, square balers, and rakes.
    *   *Pain & Needs:* High equipment debt; seasonal operational window of only 20–25 days. Refuse 2-acre smallholder fields due to diesel wastage in transit ("deadhead miles"). Need contiguous 30–50 acre clusters to maximize throughput.
*   **Institutional Partners & Funders:**
    *   State Agriculture Departments (Punjab/Haryana), Commission for Air Quality Management (CAQM), Krishi Vigyan Kendras (KVKs), Corporate CSR environmental wings (automotive, logistics, FMCG), and climate impact investors.

---

### 2. Value Propositions

| Segment | Value Proposition Delivered | Defensible Technological Advantage |
| :--- | :--- | :--- |
| **Smallholder Farmers** | **Zero-Hassle Field Clearing + Guaranteed Cash:**<br>Fields baled and cleared within 48–72 hours of harvest without burning. ₹1,200–₹2,000/acre net income.<br>Zero CAQM pollution fines. | **Vernacular Voice AI (Flutter + Offline Engine):**<br>Illiterate farmers book via Punjabi/Hindi voice in under 30 seconds. In-app No-Burn Satellite Certificate. |
| **Baler Operators** | **Maximum Fuel & Equipment Utilization:**<br>Clustering algorithms group 10–15 fragmented smallholders into 35-acre contiguous runs, reducing transit diesel consumption by 32%. | **PostGIS Spatial Radius & Route Optimization:**<br>FastAPI + PostGIS clusters adjacent farm boundaries and generates fuel-optimized machinery travel paths. |
| **Biomass Buyers** | **Predictable, Moisture-Validated Feedstock Supply:**<br>Guaranteed daily tonnage schedule directly to plant gate; eliminated supplier price gouging and dry-run factory shutdowns. | **Escrow-Backed Dharamkanta Web Portal:**<br>Gross/tare weighbridge digital slip integration ensures buyers pay *only* for verified net weight received. |
| **Government & KVKs** | **Verifiable Stubble Diversion & CAQM Audit Proof:**<br>Real-time district heatmaps showing tonnes diverted from burning; automated farmer subsidy qualification. | **Sentinel-2 SWIR NBR Satellite Verification:**<br>Automated pre/post harvest burn detection confirms zero fire events before issuing certifications. |

---

### 3. Channels
*   **Direct-to-Farmer Mobile Channel:** Lightweight Flutter Android APK (17 MB budget) optimized for rural 3G/4G connectivity, offline local regex fallback, and voice-first interaction.
*   **On-Ground Village Nodes:** Custom Hiring Centres (CHCs), Primary Agricultural Credit Societies (PACS), and local village Dharamkanta weighbridge operators who act as physical touchpoints.
*   **Enterprise Web Portal:** Responsive Next.js operations portal deployed for industrial plant procurement managers, baler fleet dispatchers, and KVK audit officers.
*   **Low-Tech Fallback Channels:** Automated SMS and WhatsApp bot notifications delivering weighment receipts, truck gate ETAs, and bank payment confirmations to farmers without smartphones.

---

### 4. Customer Relationships
*   **Farmer Segment:** Automated self-service voice intake backed by **Dharamkanta Neutral Verification**. Trust is built because payments are determined by a physical, trusted village scale ticket, not an arbitrary algorithm.
*   **Baler Operators:** Automated dispatch schedules via simple SMS/app routes. Dedicated seasonal telephone hotline (Kisan Helpline) during the high-stress 20-day harvest window.
*   **Biomass Buyers:** High-touch enterprise key account management. Dedicated SLA contracts guaranteeing daily delivered tonnage with calibrated moisture parameters.
*   **Grievance Redressal:** Built-in dispute ticket system. If gross weight differs by > 3% from field estimation, automated arbitration prompts a secondary weighment at the nearest licensed Dharamkanta.

---

### 5. Revenue Streams & Funding Model
*   **Primary Revenue — B2B Offtake Commission:**
    *   *Mechanics:* Industrial buyers pay ₹2,600/tonne delivered. ParaliSetu charges a **5% platform facilitation fee (₹130/tonne)** for aggregation, spatial scheduling, and digital escrow settlement.
    *   *Volume Unit Economics:* Diverting 100,000 tonnes of paddy straw yields **₹1.30 Crore ($156,000 USD)** in direct platform revenue.
*   **Secondary Revenue — Baler Fleet Dispatch SaaS:**
    *   *Mechanics:* Baler owners pay a nominal ₹40/tonne dispatch fee for access to contiguous, pre-clustered smallholder acreage, saving them ~₹90/tonne in transit diesel.
*   **Institutional Data & ESG Audit Fees:**
    *   *Mechanics:* Annual subscription fees charged to Oil Marketing Companies (OMCs like IOCL, BPCL, HPCL) and corporate ESG buyers for verified Scope 3 supply chain traceability and satellite-audited No-Burn data.
*   **Future Upside — Carbon Offsets:**
    *   Every tonne of paddy straw diverted from open-field burning prevents approximately **1.2 tonnes of CO₂ equivalent (tCO₂e)** emissions. Monetization via Article 6 / Voluntary Carbon Markets (Verra / Gold Standard) at $6–$10/tonne CO₂.

---

### 6. Key Activities
*   **Algorithmic Optimization:** Continuous maintenance and refinement of PostGIS spatial clustering models and OR-Tools constraint engines.
*   **Vernacular Localization:** Updating ASR voice models and LLM prompts across local dialects (Malwai, Majhi, Puadhi Punjabi, and Haryanvi).
*   **Scale Integration:** Onboarding and digitalizing independent Dharamkanta weighbridges across target districts (Tarn Taran, Sangrur, Ludhiana, Karnal).
*   **Quality Compliance:** Calibrating field moisture testing protocols to ensure stubble delivered to bio-digesters remains strictly below 18% moisture.
*   **Field Engagement:** Conducting village-level farmer meetings with Panchayats and KVK officers prior to the October harvest.

---

### 7. Key Resources
*   **Proprietary Software IP:** PostGIS geospatial clustering pipeline, offline vernacular voice intake engine, and real-time Dharamkanta weighbridge escrow state machine.
*   **Agronomic Ground-Truth Data:** PAU-calibrated yield factors mapping crop varieties (PR-126, Pusa-44, Basmati) and harvest methods to recoverable baled tonnage.
*   **Ecosystem Partnerships:** Verified registry of 500+ baler operators, 1,200 tractor-trolleys, and industrial off-take contracts with SATAT Bio-CNG plants.
*   **Human Capital:** Full-stack software engineers, GIS spatial specialists, rural field coordinators, and agricultural extension advisors.

---

### 8. Key Partnerships
*   **Bio-CNG & Ethanol Refineries:** Off-take partners (e.g., Verbio Sangrur, IOCL 2G Plant Panipat, EverEnviro, Reliance Bio-Energy) providing guaranteed purchase contracts.
*   **Punjab & Haryana Agriculture Departments:** Integration with the Sub-Mission on Agricultural Mechanization (SMAM) and State Crop Residue Management (CRM) databases.
*   **Village Dharamkanta Operators:** Neutral third-party physical weight certifiers acting as local trust anchors.
*   **Custom Hiring Centres (CHCs) & Farmer Cooperatives:** Equipment pools deploying subsidized machinery for aggregated smallholder clusters.
*   **Bhashini / AI4Bharat:** Open-source Indic language speech-to-text models ensuring dialect-accurate voice intake.

---

### 9. Cost Structure
*   **Technology & Infrastructure (Fixed/Semi-Variable):**
    *   Cloud database & spatial servers (Supabase/AWS PostGIS, Next.js hosting): ₹35,000/month.
    *   Voice ASR & LLM token API costs (Gemini Flash, Bhashini): ₹0.15 per voice intake session.
    *   SMS/WhatsApp notification gateways: ₹0.12 per transaction update.
*   **Field Operations & Coordination (Variable — Harvest Peak):**
    *   Seasonal Village Coordinators (Kisan Mitras) across 15 clusters for 30 days: ₹4,50,000.
    *   Physical moisture meter kits and scale onboarding incentives: ₹1,50,000.
*   **Compliance, Auditing & Administrative:**
    *   Satellite data licensing (Sentinel-2 processing pipeline / Copernicus API): Open access / ₹50,000 processing overhead.
    *   Legal escrow compliance, banking API fees, and audit accounting: ₹1,20,000 annually.
