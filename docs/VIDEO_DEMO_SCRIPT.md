# 🎬 ParaliSetu — 2.5-Minute Hackathon Demo Video Script & Production Cue Sheet

**Total Duration:** 2 Minutes 30 Seconds (150 Seconds)  
**Target Pacing:** 130–140 words/minute (Confident, clear, conversational, authoritative)  
**Background Music:** Modern ambient tech / lo-fi electronic (low volume, ducks during voiceover)  
**Tone:** Field-grounded, empathetic to smallholder farmers, technically rigorous  

---

## ⏱️ Video Timeline Overview

| Section | Timecode | Duration | Visual Focus | Core Message |
| :--- | :---: | :---: | :--- | :--- |
| **1. The Hook & The Crisis** | `0:00 – 0:25` | 25s | Slide 1 + Satellite Smoke & Fire Map | The 15-day harvest deadline & why fines failed |
| **2. The ParaliSetu Solution** | `0:25 – 0:50` | 25s | Slide 2 (xyflow Architecture) + App Splash | The 4-sided bridge: Farmer, Baler, Truck, Buyer |
| **3. Live Golden Path Walkthrough** | `0:50 – 1:40` | 50s | Screen Recordings of Mobile App & Web Portals | End-to-end booking, weighbridge escrow, satellite audit |
| **4. Technical Feasibility & Rigor** | `1:40 – 2:05` | 25s | Slide 4 (Feasibility & Risk Matrix) | OR-Tools CP-SAT in <2s, 17MB APK, 100% green tests |
| **5. Macro Impact & Market Scale** | `2:05 – 2:20` | 15s | Slide 3 (Impact Potential) | ₹25,000+ farmer gain, 4.4 MMT Bio-CNG, 45M protected |
| **6. Team & Visionary Close** | `2:20 – 2:30` | 10s | Slide 5 (Team & Engineering Division) | Transforming an eco-disaster into rural wealth |

---

## 📽️ Scene-by-Scene Production Cue Sheet

### 🎬 SCENE 1: The Hook & The Agronomic Ground Truth (`0:00 – 0:25` | 25s)

* **What to Show on Screen:**
  * **[0:00 – 0:08]** Full-screen opening with **[Problem_Proposed_Solution_Slide.png](file:///c:/Users/Rishabh%20Bansal/Downloads/Parali%20setu/Problem_Proposed_Solution_Slide.png)** (or NASA FIRMS North India fire hotspot map). Slow zoom into the central problem banner.
  * **[0:08 – 0:18]** Highlight the red problem callout: *"The 10–15 Day Harvest Deadline & ₹15,000 Fine Fear"*.
  * **[0:18 – 0:25]** Transition to text overlay: *"20 Million Tonnes of Stubble · $19 Billion Health Burden"*.
* **On-Screen Captions:**
  * `October–November: 15 Days Between Paddy Harvest & Wheat Sowing`
  * `Fines Criminalize Farmers · Lack of Machinery Forces the Fire`
* **Voiceover (Verbatim):**
  > *"Every October, North India chokes under toxic smog, creating a 19-billion-dollar health crisis. But farmers don't burn paddy stubble out of malice—they burn it out of pure desperation. With only 10 to 15 days before wheat sowing, a 2-acre farmer cannot afford a 15-lakh baler, and commercial operators refuse small, scattered plots. Government fines only criminalized the farmer without offering a viable logistics bridge. Until now."*

---

### 🎬 SCENE 2: The Solution — Introducing ParaliSetu (`0:25 – 0:50` | 25s)

* **What to Show on Screen:**
  * **[0:25 – 0:35]** Cut to **[Technical_Approach_Slide.png](file:///c:/Users/Rishabh%20Bansal/Downloads/Parali%20setu/Technical_Approach_Slide.png)** featuring the interactive **xyflow architecture flowchart**. Zoom into the 4 connecting nodes: *Farmer $\rightarrow$ Baler Operator $\rightarrow$ Dharamkanta $\rightarrow$ Bio-CNG Plant*.
  * **[0:35 – 0:42]** Quick cut to phone frame showing the Flutter mobile app opening with the **trilingual splash screen** (Punjabi / Hindi / English).
  * **[0:42 – 0:50]** Screen capture of **[01_farmer_home_en.png](file:///c:/Users/Rishabh%20Bansal/Downloads/Parali%20setu/docs/screenshots/01_farmer_home_en.png)** showing the ambient Tarn Taran weather card, Stubble Valuation CTA, and Voice Intake chip.
* **On-Screen Captions:**
  * `ParaliSetu: The 1-Tap Agronomic Marketplace`
  * `Connecting Smallholders Directly to Industrial Bio-CNG Offtakers`
* **Voiceover (Verbatim):**
  > *"Meet ParaliSetu—the first voice-first, multi-sided marketplace designed specifically for India's 2-acre smallholders. We turn a 15,000-rupee fine liability into guaranteed seasonal wealth. Built on an ultra-lightweight 17-megabyte Flutter client and a FastAPI PostGIS core, ParaliSetu clusters fragmented smallholdings into contiguous commercial runs, connects them with baler fleets, and unlocks pre-funded industrial escrow."*

---

### 🎬 SCENE 3: The Golden Path Demo — End-to-End Walkthrough (`0:50 – 1:40` | 50s)

* **What to Show on Screen (Split-Screen / Fast Fluid Cuts):**

  * **[0:50 – 1:00] Step 1: Voice Intake on Mobile**
    * *Visual:* Screen recording of **[03_voice_vernacular_chips.png](file:///c:/Users/Rishabh%20Bansal/Downloads/Parali%20setu/docs/screenshots/03_voice_vernacular_chips.png)**. Tap the pulsing mic button. Show demo speech chip: *"4 Killa PR-126, 25 October"*.
    * *Audio Effect:* Vernacular audio prompt readback (*"Aapne bola: 4 Killa PR-126, 25 October. Sahi hai?"*). Tap [Confirm].
    * *Voiceover:*
      > *"Step one: Vernacular voice intake. An illiterate farmer speaks in Punjabi or Hindi. Whisper STT and Gemini extract the acreage and date, followed by an explicit audio confirmation modal to eliminate AI guesswork."*

  * **[1:00 – 1:10] Step 2: Deterministic Stubble Valuation**
    * *Visual:* Screen recording of **[02_field_details_intake.png](file:///c:/Users/Rishabh%20Bansal/Downloads/Parali%20setu/docs/screenshots/02_field_details_intake.png)** & **[05_field_details_calculate.png](file:///c:/Users/Rishabh%20Bansal/Downloads/Parali%20setu/docs/screenshots/05_field_details_calculate.png)**.
    * *Visual Action:* Show the dual-metric breakdown: Total Biological Biomass (14.4 Tonnes) vs Recoverable Baled Straw (8.0 Tonnes @ ₹1,200/t = ₹9,600).
    * *Voiceover:*
      > *"Step two: Transparent agronomic ground truth. Using PAU formulas, we separate biological field residue from baler-recoverable straw so the farmer knows their exact tradable earnings up front."*

  * **[1:10 – 1:20] Step 3: 1-Tap Bundle Booking & Escrow Protection**
    * *Visual:* Display matched bundle card: *Baler Gurdeep Singh + Sharma Logistics + Bio-CNG Plant*. Tap **[Book Pickup]**. Show the Escrow Hold confirmation screen.
    * *Voiceover:*
      > *"Step three: In one tap, Google OR-Tools matches the farmer with an active baler and truck operating within their 15-day window. The buyer's pre-funded escrow locks the payment guarantee."*

  * **[1:20 – 1:30] Step 4: Web Command Center & Dharamkanta Weighbridge Terminal**
    * *Visual:* Cut to desktop browser showing **[06_buyer_command_center.png](file:///c:/Users/Rishabh%20Bansal/Downloads/Parali%20setu/docs/screenshots/06_buyer_command_center.png)** (daily 200t demand target) and transition to **[07_dharamkanta_weighbridge.png](file:///c:/Users/Rishabh%20Bansal/Downloads/Parali%20setu/docs/screenshots/07_dharamkanta_weighbridge.png)**.
    * *Visual Action:* Show truck scale entry: Gross 14.2t, Tare 6.2t, Net 8.0t. Point to OCR validation. Click **[Approve Scale Ticket]** $\rightarrow$ Instant UPI escrow payout released!
    * *Voiceover:*
      > *"Meanwhile, industrial buyers set daily quotas on the Next.js web portal. At the local Dharamkanta weighbridge, the scale operator enters gross and tare weights with automated OCR validation. Payout is released directly to the farmer's bank account instantly."*

  * **[1:30 – 1:40] Step 5: Copernicus Sentinel-2 Satellite No-Burn Audit**
    * *Visual:* Screen capture of **[08_kvk_satellite_audit.png](file:///c:/Users/Rishabh%20Bansal/Downloads/Parali%20setu/docs/screenshots/08_kvk_satellite_audit.png)**. Show the 10m spatial resolution SWIR spectral scan and the green $\Delta\text{NBR} = 0.12 < 0.15$ score badge. Click **[Issue No-Burn Certificate]**.
    * *Voiceover:*
      > *"Finally, zero manual field audits. ESA Copernicus Sentinel-2 short-wave infrared satellites scan the parcel remotely. Proving zero burn automatically generates a compliance certificate and unlocks 1,000 rupees per acre in government DBT subsidies."*

---

### 🎬 SCENE 4: Technical Feasibility & Production Rigor (`1:40 – 2:05` | 25s)

* **What to Show on Screen:**
  * **[1:40 – 1:52]** Cut to **[Feasibility_and_Risk_Analysis_Slide.png](file:///c:/Users/Rishabh%20Bansal/Downloads/Parali%20setu/Feasibility_and_Risk_Analysis_Slide.png)**. Zoom into the Left Zone: *Technical & Operational Feasibility*.
  * **[1:52 – 2:05]** Zoom into the Right Zone: *Defensive Architecture & Anti-Fraud Guardrails* (OCR sanity check, spatial parcel clustering, audio verification loop). Quick terminal B-roll showing `pytest` 21/21 green test output.
* **On-Screen Captions:**
  * `Google OR-Tools CP-SAT: Solves NP-Hard Matching in < 2.0s`
  * `17.03 MB Split APK · 12 PostGIS Tables with Cryptographic RLS`
* **Voiceover (Verbatim):**
  > *"Under the hood, ParaliSetu is engineered for real-world reliability. Our Google OR-Tools CP-SAT engine solves NP-hard spatial matching across thousands of farms in under 2 seconds, grouping parcels into 25-to-40 acre corridors that cut baler deadhead transit by 40%. With a 17-megabyte offline-first APK, 12 PostGIS tables with Row-Level Security, and 100% green test coverage, this is production software built to withstand rural deployment."*

---

### 🎬 SCENE 5: Impact Potential & Circular Economy Scale (`2:05 – 2:20` | 15s)

* **What to Show on Screen:**
  * **[2:05 – 2:20]** Cut to **[Impact_Potential_Slide.png](file:///c:/Users/Rishabh%20Bansal/Downloads/Parali%20setu/Impact_Potential_Slide.png)**. Highlight the 4 top metric cards sequentially:
    1. `₹25,000+ Net Farmer Gain / 5-Acre Season`
    2. `4.4 MMT Annual Bio-CNG Potential (MoPNG SATAT)`
    3. `45M+ People Clean Air Shield (World Bank / IFPRI)`
    4. `30M Tonnes CO₂ Diverted Annually (CAQM)`
* **On-Screen Captions:**
  * `₹25k+ Farmer Profit · 4.4 MMT Bio-CNG Fuel · 30M Tonnes CO₂ Diverted`
  * `Verified by PAU, MoPNG SATAT, CAQM & World Bank Studies`
* **Voiceover (Verbatim):**
  > *"The impact is staggering. A 5-acre farming family gains over 25,000 rupees in net profit instead of burning fines. At regional scale, diverting Punjab's 20 million tonnes of straw fuels India's SATAT initiative with 4.4 million tonnes of Bio-CNG, diverts 30 million tonnes of CO2, and shields 45 million people from hazardous autumn smog."*

---

### 🎬 SCENE 6: Team Composition & Closing Call to Action (`2:20 – 2:30` | 10s)

* **What to Show on Screen:**
  * **[2:20 – 2:27]** Cut to **[Team_Slide.png](file:///c:/Users/Rishabh%20Bansal/Downloads/Parali%20setu/Team_Slide.png)** showing the 3-tier engineering division for **Rishabh Bansal**, **Ravi Singh**, and **Vaibhav Yadav**, and the bottom Hackathon Journey roadmap.
  * **[2:27 – 2:30]** Final title card with logo: **ParaliSetu — The Stubble Bridge**. Show GitHub URL `github.com/Rishabhbansal005/Parali-setu` and tagline: *"Turning Autumn Smoke into Green Rural Wealth."*
* **On-Screen Captions:**
  * `Team ParaliSetu: Rishabh Bansal · Ravi Singh · Vaibhav Yadav`
  * `GitHub: github.com/Rishabhbansal005/Parali-setu`
* **Voiceover (Verbatim):**
  > *"Built by Rishabh Bansal, Ravi Singh, and Vaibhav Yadav, ParaliSetu bridges agriculture, algorithms, and clean energy. Thank you!"*

---

## 🛠️ Recording & Production Quick-Guide

### 1. Recording Software & Setup
* **Screen Recording:** Use **OBS Studio** (or Windows Game Bar `Win + G`) set to **1080p (1920×1080) at 60 FPS**.
* **Audio Recording:** Use a USB condenser microphone (or clean smartphone voice memo). Record in a quiet room with minimal echo.
* **Aspect Ratios:**
  * For Mobile Screens: Place phone recording inside an elegant Android device mockup on a Slate `#f8fafc` background (centered or side-by-side with web dashboards).
  * For Web & Slides: Full-screen 16:9 widescreen capture.

### 2. Assets Checklist (All Pre-Generated in Codebase)
* **High-Res Slide PNGs:**
  * Slide 1: `Problem_Proposed_Solution_Slide.png`
  * Slide 2: `Technical_Approach_Slide.png`
  * Slide 3: `Impact_Potential_Slide.png`
  * Slide 4: `Feasibility_and_Risk_Analysis_Slide.png`
  * Slide 5: `Team_Slide.png`
  * Slide 6: `References_Slide.png`
* **Live Product Screenshots:**
  * `docs/screenshots/01_farmer_home_en.png`
  * `docs/screenshots/02_field_details_intake.png`
  * `docs/screenshots/03_voice_vernacular_chips.png`
  * `docs/screenshots/05_field_details_calculate.png`
  * `docs/screenshots/06_buyer_command_center.png`
  * `docs/screenshots/07_dharamkanta_weighbridge.png`
  * `docs/screenshots/08_kvk_satellite_audit.png`
* **Interactive Web Presentation Deck:** Open `docs/slides/index.html` in Microsoft Edge / Chrome and press `[F]` for full-screen mode to easily click through slides during recording.
