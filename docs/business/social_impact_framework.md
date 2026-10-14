# Social Impact Framework & Sustainability Analysis
**Hack for Social Hackathon | Project: ParaliSetu**  
*Rigorous, Evidence-Based Impact Evaluation & Theory of Change*

---

## 1. Theory of Change (ToC) Framework

```
+--------------------------------------------------------------------------------------------------------------------+
|                                                  THEORY OF CHANGE                                                  |
+-------------------+--------------------+--------------------+-----------------------+------------------------------+
| INPUTS &          | KEY ACTIVITIES     | DIRECT OUTPUTS     | INTERMEDIATE          | LONG-TERM IMPACT             |
| RESOURCES         | (INTERVENTIONS)    | (DELIVERABLES)     | OUTCOMES              | (SYSTEMIC CHANGE)            |
+-------------------+--------------------+--------------------+-----------------------+------------------------------+
| • Vernacular Voice| • Digitally        | • 100,000 tonnes of| • 0 open-field fires  | • Clean Air for 50M+         |
|   Intake Engine   |   cluster small-   |   stubble collected|   across 50,000       |   citizens across North      |
|   (Punjabi/Hindi) |   holders into     |   & compressed.    |   participating acres.|   India (40% drop in peak    |
| • PostGIS Spatial |   contiguous runs. | • 1,200 small-     | • ₹10.0+ Crore direct |   winter smog events).       |
|   Matching Engine | • Dispatch balers  |   holders linked   |   farmer & rural crew | • 120,000 tCO₂e GHGs         |
| • Dharamkanta Web |   within 20 km.    |   to green buyers. |   cash payout via     |   abated annually.           |
|   Operations      | • Neutral weighment| • 100% digitalized |   Dharamkanta scale.  | • Viable Rural Bio-Economy:  |
|   Portal          |   logging at local |   gross/tare scale | • 2G ethanol & Bio-   |   15% increase in rural      |
| • Local Balers,   |   Dharamkanta.     |   tickets issued.  |   CNG digesters run   |   machinery utilization and  |
|   Tractors & CHCs | • Automated escrow | • Sentinel-2 post- |   at 95% capacity     |   new green-collar jobs for  |
| • Subsidized CRM  |   payout direct to |   harvest No-Burn  |   with zero feedstock |   rural youth.               |
|   Machinery Pools |   farmer bank acct.|   certificates.    |   shortages.          | • Soil organic carbon saved. |
+-------------------+--------------------+--------------------+-----------------------+------------------------------+
```

---

## 2. Core Social & Environmental Impact KPIs

| KPI # | Metric Name | Definition & Measurement Formula | Baseline (Current State) | ParaliSetu Pilot Target | ParaliSetu 3-Year Target |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **KPI 1** | **Residue Diverted from Burning** | Tonnes of dry baled paddy straw delivered to registered biomass off-takers. Measured via Dharamkanta certified weighbridge slips. | 0 Tonnes (90% burnt in open fields) | **25,000 Tonnes** *(Pilot - 1 District)* | **1,000,000 Tonnes** *(4 Districts)* |
| **KPI 2** | **GHG & Air Pollution Abatement** | Tonnes of Carbon Dioxide equivalent ($\text{tCO}_2\text{e}$) and kilograms of Particulate Matter ($\text{PM}_{2.5}$) prevented. *Factor: 1.2 tCO₂e and 7.1 kg PM2.5 per tonne stubble burnt.* | High emissions causing hazardous AQI 500+ | **30,000 tCO₂e** abated<br>**177,500 kg PM2.5** prevented | **1,200,000 tCO₂e** abated<br>**7.1M kg PM2.5** prevented |
| **KPI 3** | **Direct Farmer Income Created** | Net cash earnings or direct fuel/labor expenditure saved per acre by smallholder farmers. | -₹2,500/acre in machinery costs or penalty exposure | **₹1,200 – ₹1,800 / acre** net income / cost saved | **₹50+ Crore** transferred directly to smallholders |
| **KPI 4** | **Smallholder Coverage Rate** | Percentage of total bookings coming from marginal farmers owning $\le 4$ acres of land. | < 5% (Commercial balers historically serve only large 20+ acre farms) | **$\ge 60\%$ of total bookings** | **$\ge 75\%$ of total bookings** |
| **KPI 5** | **Baler Machine Utilization** | Productive hours baling per day during the 20-day window. Measured via GPS run times. | 4.5 hours/day (high idle time in road transit) | **7.5 hours/day** (+66% throughput) | **8.5 hours/day** |

---

## 3. Baseline Data Requirements & Practical Verification

To maintain credibility with judges and environmental auditors, ParaliSetu uses **dual-layer independent verification**:
1.  **Physical Layer (Dharamkanta Weighbridge):**
    *   No payment is released on estimates. Every truck is weighed empty (Tare) and full (Gross) at a state-registered weighbridge.
    *   The digital weighbridge ticket records: Truck Plate Number, Farmer Booking ID, Gross Tonnes, Tare Tonnes, and Net Weight.
2.  **Remote Sensing Layer (Copernicus Sentinel-2 SWIR NBR Audit):**
    *   *Normalized Burn Ratio (NBR):* $\text{NBR} = \frac{\text{NIR} - \text{SWIR}}{\text{NIR} + \text{SWIR}}$.
    *   Pre-harvest baseline image vs. post-harvest image (Day 15).
    *   A sudden drop in NBR ($\Delta \text{NBR} > 0.15$) accompanied by a thermal anomaly indicates an open fire.
    *   Fields with verified zero fire signatures automatically receive an **In-App No-Burn Certificate**, shared with the local Sub-Divisional Magistrate (SDM) and Agriculture Officer to exempt the farmer from state penalties.

---

## 4. Equity, Inclusion & Beneficiary Accessibility

*   **Vernacular & Illiteracy Inclusion:** 
    *   According to rural literacy surveys in Punjab/Haryana, over 40% of smallholder farmers over age 45 struggle with complex digital form interfaces.
    *   ParaliSetu incorporates an **offline-first Voice Intake engine** in Punjabi and Hindi. Farmers tap a single large microphone icon and speak naturally. The app confirms verbally and displays high-contrast visual chips.
*   **Neutralizing the "Small Farm Penalty":**
    *   Commercial balers routinely reject 2-acre plots because maneuvering large 75 HP tractors into isolated corners causes net fuel losses.
    *   ParaliSetu’s PostGIS spatial clustering aggregates neighboring 1–3 acre plots into a single **"Virtual 40-Acre Farm"**, guaranteeing baler access to the smallest plots on equal terms.
*   **Protection of Tenant Farmers (*Pattedars*):**
    *   Over 30% of Punjab cropland is cultivated by informal tenant farmers without registered land titles.
    *   ParaliSetu attaches bookings to the **phone number and GPS field boundary**, ensuring the actual tiller of the soil receives the cash payment and clearance service, regardless of land title disputes.

---

## 5. Potential Unintended Consequences & Rigorous Safeguards

| Potential Unintended Consequence | Why It Could Occur | ParaliSetu Engineering & Policy Safeguard |
| :--- | :--- | :--- |
| **1. Soil Nutrient Depletion** | Completely removing all straw year after year can deplete soil Organic Carbon (SOC), Potassium ($K$), and Phosphorus ($P$). | **Agronomic Yield Cap (58% Recovery Rate):** The app explicitly calibrates balers to harvest only upper cut straw (~2.0 t/acre), leaving the lower 25–35 cm rooted stubble to decompose naturally and replenish soil microbial carbon. |
| **2. Bale Moisture Dispute at Factory Gate** | Stubble baled with high moisture (>18%) degrades in factory storage and can cause biological spontaneous combustion. | **Pre-Dispatch Digital Moisture Validation:** Local tractor crews are equipped with ₹2,500 handheld digital pin probe moisture meters. Slips record moisture percentage before truck dispatch. |
| **3. Machine Breakdown Bottlenecks** | If a baler breaks down during the peak 15-day window, panic-stricken farmers may burn their fields to avoid wheat sowing delays. | **Dynamic Dynamic Re-Routing (CP-SAT Solver):** If a baler reports an in-app mechanical fault, the backend automatically cascades the unserviced cluster to the nearest secondary baler within an expanded 25 km radius within 6 hours. |
| **4. Rural Wage Disruption** | Farm labor historically hired for manual straw cutting might face seasonal income loss. | **Labor Role Integration:** Traditional manual crews are registered as certified loader and baler-assist crews, earning higher structured day rates for mechanical bale loading and stack tarping. |

---

## 6. Pilot Validation Plan (Tarn Taran & Sangrur Phase 1)

*   **Pilot Location:** Sangrur & Tarn Taran districts, Punjab (epicenter of paddy stubble fires in North India).
*   **Target Scope:** 15 Village Clusters, 250 Smallholder Farmers, 10 Custom Hiring Centre Balers, and 1 SATAT Bio-CNG Plant (Verbio Sangrur).
*   **Timeline:** 30 Days (October 10 – November 10).
*   **Success Criteria:**
    *   $\ge 90\%$ of registered smallholder acreage cleared within 72 hours of combine harvest.
    *   Zero field fire infractions recorded by Sentinel-2 over participating coordinates.
    *   Average payout time: Under 24 hours from Dharamkanta weighment.
    *   Farmer Net Promoter Score (NPS) $\ge +75$.
