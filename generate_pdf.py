import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica-Bold", 8)
        self.setFillColor(colors.HexColor("#64748b"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(36, 11 * inch - 26, "ParaliSetu — 3.5 to 4.0 Min Video Demo Screenplay & Cue Sheet")
            self.drawRightString(8.5 * inch - 36, 11 * inch - 26, "SEVA First Innovation Challenge 2026")
            self.setStrokeColor(colors.HexColor("#cbd5e1"))
            self.setLineWidth(0.5)
            self.line(36, 11 * inch - 30, 8.5 * inch - 36, 11 * inch - 30)
            
        # Footer
        self.setFont("Helvetica", 8)
        footer_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(8.5 * inch - 36, 20, footer_text)
        self.drawString(36, 20, "Confidential & Proprietary — Team Mist (Reg ID: REG-001-OP) | Solo Innovator: Rishabh Bansal")
        self.setStrokeColor(colors.HexColor("#cbd5e1"))
        self.setLineWidth(0.5)
        self.line(36, 28, 8.5 * inch - 36, 28)
        
        self.restoreState()

def build_pdf(filename):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    primary_color = colors.HexColor("#1b4332")
    accent_color = colors.HexColor("#2d6a4f")
    dark_slate = colors.HexColor("#1e293b")
    quote_bg = colors.HexColor("#ecfdf5")
    quote_border = colors.HexColor("#10b981")

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=17,
        leading=21,
        textColor=primary_color
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#475569")
    )

    h1_style = ParagraphStyle(
        'ActHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=colors.white
    )

    timecode_style = ParagraphStyle(
        'TimecodeHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=accent_color
    )

    label_screen = ParagraphStyle(
        'LabelScreen',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor("#0369a1")
    )

    content_screen = ParagraphStyle(
        'ContentScreen',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=dark_slate
    )

    label_action = ParagraphStyle(
        'LabelAction',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor("#b45309")
    )

    content_action = ParagraphStyle(
        'ContentAction',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=dark_slate
    )

    label_dialogue = ParagraphStyle(
        'LabelDialogue',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=colors.HexColor("#065f46")
    )

    dialogue_text = ParagraphStyle(
        'DialogueText',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#0f172a")
    )

    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.white,
        alignment=1
    )

    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.5,
        textColor=dark_slate
    )

    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9.5,
        textColor=dark_slate
    )

    story = []

    # Title Banner
    story.append(Paragraph("🎬 PARALISETU — OFFICIAL VIDEO DEMO SCRIPT & CUE SHEET", title_style))
    story.append(Spacer(1, 2))
    meta_text = (
        "<b>Challenge:</b> SEVA First Innovation Challenge 2026 (DTU & Govt. of NCT of Delhi) &nbsp;|&nbsp; "
        "<b>Team:</b> Team Mist (Reg ID: REG-001-OP)<br/>"
        "<b>Solo Innovator:</b> Rishabh Bansal &nbsp;|&nbsp; "
        "<b>Target Video Runtime:</b> 3 Minutes 45 Seconds (225s | Target Window: 3:30 to 4:00)"
    )
    story.append(Paragraph(meta_text, subtitle_style))
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=1.5, color=primary_color, spaceAfter=8))

    # Master Timeline Table
    story.append(Paragraph("<b>⏱️ MASTER TIMELINE & ASSET MAPPING TABLE</b>", timecode_style))
    story.append(Spacer(1, 3))

    overview_data = [
        [
            Paragraph("Timecode", table_header),
            Paragraph("Section & Theme", table_header),
            Paragraph("Screen / Visual Asset to Show", table_header),
            Paragraph("Key Action / Spoken Dialogue Core", table_header)
        ],
        [
            Paragraph("<b>0:00 – 0:18</b>", table_cell),
            Paragraph("The Problem: Air Crisis", table_cell_bold),
            Paragraph("<code>docs/evidence/01_active_stubble_burning.jpg</code><br/><code>docs/evidence/03_seasonal_smog_haze.jpg</code>", table_cell),
            Paragraph("Sangrur field burning + Delhi smog; AQI > 500, $19B health cost.", table_cell)
        ],
        [
            Paragraph("<b>0:18 – 0:35</b>", table_cell),
            Paragraph("The Farmer's 15-Day Trap", table_cell_bold),
            Paragraph("<code>docs/evidence/02_unmanaged_straw_volume.jpg</code><br/><code>docs/evidence/04_satellite_fire_hotspots_map.jpg</code>", table_cell),
            Paragraph("3.6 t/acre straw volume, tight 15d wheat window, failure of ₹15k fines.", table_cell)
        ],
        [
            Paragraph("<b>0:35 – 0:55</b>", table_cell),
            Paragraph("Target Beneficiaries", table_cell_bold),
            Paragraph("<code>docs/evidence/11_farmer_using_app_in_field.jpg</code><br/><code>docs/evidence/12_weighbridge_scale_operation.jpg</code>", table_cell),
            Paragraph("3 core users: 2-acre farmers, baler contractors, industrial Bio-CNG plants.", table_cell)
        ],
        [
            Paragraph("<b>0:55 – 1:15</b>", table_cell),
            Paragraph("Solution Architecture", table_cell_bold),
            Paragraph("<code>docs/diagrams/architecture.png</code>", table_cell),
            Paragraph("4-sided cyber-physical bridge: App → OR-Tools → Weighbridge IoT → Satellite.", table_cell)
        ],
        [
            Paragraph("<b>1:15 – 1:40</b>", table_cell),
            Paragraph("Demo: Voice Intake", table_cell_bold),
            Paragraph("<b>Mirrored Phone Screen</b> (or <code>03_voice_vernacular_chips.png</code>)", table_cell),
            Paragraph("Tap mic, speak Punjabi/Hindi, Bhashini ASR normalizes '4 Killa' into ha.", table_cell)
        ],
        [
            Paragraph("<b>1:40 – 2:05</b>", table_cell),
            Paragraph("Demo: PAU Yield Math", table_cell_bold),
            Paragraph("<b>Mirrored Phone Screen</b> (or <code>05_field_details_calculate.png</code>)", table_cell),
            Paragraph("PAU formula: 14.4t total vs 8.0t recoverable @ ₹1,200/t = ₹9,600 price lock.", table_cell)
        ],
        [
            Paragraph("<b>2:05 – 2:25</b>", table_cell),
            Paragraph("Demo: Web Command Center", table_cell_bold),
            Paragraph("<b>Browser:</b> <code>http://localhost:3000</code> (Buyer Tab)", table_cell),
            Paragraph("PostGIS DBSCAN 35-acre cluster + Google OR-Tools CP-SAT fleet dispatch.", table_cell)
        ],
        [
            Paragraph("<b>2:25 – 2:40</b>", table_cell),
            Paragraph("Demo: Weighbridge IoT", table_cell_bold),
            Paragraph("<b>Browser:</b> <code>http://localhost:3000</code> (Weighbridge Tab)", table_cell),
            Paragraph("ESP32 RS-232 telemetry: 14.2t gross, 6.2t tare, HMAC SHA-256 tamper-proof.", table_cell)
        ],
        [
            Paragraph("<b>2:40 – 2:55</b>", table_cell),
            Paragraph("Demo: Satellite & Escrow", table_cell_bold),
            Paragraph("<b>Browser:</b> <code>http://localhost:3000</code> (KVK / Satellite Tab)", table_cell),
            Paragraph("Copernicus Sentinel-2 ΔNBR < 0.10 no-burn proof, instant UPI payout in <120s.", table_cell)
        ],
        [
            Paragraph("<b>2:55 – 3:30</b>", table_cell),
            Paragraph("Macro Potential Impact", table_cell_bold),
            Paragraph("<code>Impact_Potential_Slide.png</code>", table_cell),
            Paragraph("+₹25k farmer profit, 30M t CO₂ cut, 4.4 MMT Bio-CNG, 45M clean air.", table_cell)
        ],
        [
            Paragraph("<b>3:30 – 3:45</b>", table_cell),
            Paragraph("Team Mist Closing Call", table_cell_bold),
            Paragraph("<code>Team_Slide.png</code> (Title Slide & Repo)", table_cell),
            Paragraph("Solo Innovator Rishabh Bansal, DTU/Delhi Govt pitch, GitHub link.", table_cell)
        ]
    ]

    t_overview = Table(overview_data, colWidths=[65, 115, 175, 185])
    t_overview.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), primary_color),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
    ]))
    story.append(t_overview)
    story.append(Spacer(1, 8))

    def make_act_banner(title):
        data = [[Paragraph(f"<b>{title}</b>", h1_style)]]
        t = Table(data, colWidths=[540])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), primary_color),
            ('TOPPADDING', (0, 0), (-1, -1), 3),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
            ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ]))
        return t

    def make_scene_box(timecode, title, screen_text, action_text, dialogue_str):
        rows = [
            [Paragraph(f"<b>⏱️ {timecode} — {title}</b>", timecode_style), ""],
            [Paragraph("🖥️ <b>SCREEN:</b>", label_screen), Paragraph(screen_text, content_screen)],
            [Paragraph("🖱️ <b>ACTION:</b>", label_action), Paragraph(action_text, content_action)],
            [Paragraph("🎙️ <b>DIALOGUE:</b>", label_dialogue), Paragraph(f'"{dialogue_str}"', dialogue_text)]
        ]
        t = Table(rows, colWidths=[90, 450])
        t.setStyle(TableStyle([
            ('SPAN', (0, 0), (1, 0)),
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#f1f5f9")),
            ('BACKGROUND', (0, 1), (-1, 2), colors.HexColor("#f8fafc")),
            ('BACKGROUND', (0, 3), (-1, 3), quote_bg),
            ('LINELEFT', (0, 3), (0, 3), 3, quote_border),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('TOPPADDING', (0, 0), (-1, -1), 2.5),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
            ('LEFTPADDING', (0, 0), (-1, -1), 5),
            ('RIGHTPADDING', (0, 0), (-1, -1), 5),
            ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
            ('LINEBELOW', (0, 0), (-1, 0), 0.5, colors.HexColor("#cbd5e1")),
            ('LINEBELOW', (0, 1), (-1, 1), 0.5, colors.HexColor("#e2e8f0")),
            ('LINEBELOW', (0, 2), (-1, 2), 0.5, colors.HexColor("#e2e8f0")),
        ]))
        return t

    # ACT 1
    story.append(make_act_banner("ACT 1: THE PROBLEM & FIELD REALITY (0:00 – 0:35)"))
    story.append(Spacer(1, 3))
    story.append(make_scene_box(
        "0:00 – 0:18",
        "The Air Pollution Emergency",
        "Open high-res photo <code>docs/evidence/01_active_stubble_burning.jpg</code> in full-screen. After 10s, switch to <code>docs/evidence/03_seasonal_smog_haze.jpg</code>.",
        "Smooth slow-pan across flames and rising smoke. Overlay text: <i>Sangrur, Punjab · October 2026</i>.",
        "Every year in October, over twenty million tonnes of paddy straw are set on fire across Punjab and Haryana. Within forty-eight hours, dense toxic smog blankets North India, shooting the Air Quality Index beyond 500 and causing a 19-billion-dollar health emergency across Delhi and the National Capital Region."
    ))
    story.append(Spacer(1, 4))
    story.append(make_scene_box(
        "0:18 – 0:35",
        "The Farmer's 15-Day Trap",
        "Photo <code>docs/evidence/02_unmanaged_straw_volume.jpg</code> (straw heaps), followed by satellite fire map <code>docs/evidence/04_satellite_fire_hotspots_map.jpg</code>.",
        "Point cursor to massive 3.6 t/acre straw volume on the ground, then to red thermal fire anomaly clusters.",
        "Farmers do not burn stubble out of malice. An acre yields nearly 3.6 tonnes of bulky straw, and a farmer has barely a 15-day window to clear his fields before sowing wheat. Delaying wheat sowing drops his crop yield by 1.5 quintals per acre every week. Commercial balers ignore small, scattered plots, leaving farmers stranded. Government fines of 15,000 rupees only criminalized the farmer without solving the logistics bottleneck."
    ))
    story.append(Spacer(1, 6))

    # ACT 2
    story.append(make_act_banner("ACT 2: TARGET BENEFICIARIES (0:35 – 0:55)"))
    story.append(Spacer(1, 3))
    story.append(make_scene_box(
        "0:35 – 0:55",
        "The 3 Core Supply-Chain Users",
        "Side-by-side: <code>docs/evidence/11_farmer_using_app_in_field.jpg</code> (Farmer) and <code>docs/evidence/12_weighbridge_scale_operation.jpg</code> (Weighbridge Scale).",
        "Display 3 text badges: 1. Smallholder Farmers (2-4 Acres) | 2. Baler Contractors (Fuel Waste) | 3. Bio-CNG Plants (200t daily demand).",
        "We engineered ParaliSetu to solve this for three core users: First, smallholder farmers who cannot afford 15-lakh baler machines. Second, baler operators who waste 40% of their diesel driving empty between scattered plots. And third, industrial Bio-CNG plants that desperately need 200 tonnes of dry biomass daily but have no organized supply chain."
    ))
    story.append(Spacer(1, 6))

    # ACT 3
    story.append(make_act_banner("ACT 3: THE SOLUTION ARCHITECTURE (0:55 – 1:15)"))
    story.append(Spacer(1, 3))
    story.append(make_scene_box(
        "0:55 – 1:15",
        "The 4-Way Cyber-Physical Bridge",
        "Full-screen System Architecture Diagram: <code>docs/diagrams/architecture.png</code>.",
        "Trace mouse cursor smoothly from left to right: Farmer App → PostGIS & OR-Tools Solver → Weighbridge IoT → Satellite Escrow.",
        "ParaliSetu is an end-to-end cyber-physical supply chain and escrow marketplace. It connects smallholder farmers, baler contractors, local weighbridges, and industrial buyers into a single transparent, automated supply loop."
    ))
    story.append(Spacer(1, 6))

    # ACT 4 (Page break for clean demo layout)
    story.append(PageBreak())
    story.append(make_act_banner("ACT 4: LIVE WORKING DEMO — WORKING PROTOTYPE (1:15 – 2:55)"))
    story.append(Spacer(1, 3))

    story.append(make_scene_box(
        "1:15 – 1:40",
        "Demo Step 1: Mobile App & Vernacular Voice Intake",
        "<b>Live Phone Screen</b> mirrored via <code>Start_Phone_Screen_Mirror.bat</code> (or screenshot <code>03_voice_vernacular_chips.png</code>).",
        "Tap Language Selector (Punjabi/Hindi/English). Point out offline-first architecture. Tap pulsing mic button to show audio waveform and transcribed speech chip: '4 Killa, PR-126, 25 October'.",
        "Here is our live working Flutter mobile app. It is lightweight, sub-18 megabytes, and works offline-first so farmers in remote fields never get blocked. An illiterate farmer doesn't need to type. He simply taps the microphone and speaks in his native Punjabi or Hindi: '4 Killa, PR-126, 25 October'. The AI speech engine transcribes it and normalizes local units into standard hectares."
    ))
    story.append(Spacer(1, 4))

    story.append(make_scene_box(
        "1:40 – 2:05",
        "Demo Step 2: PAU Agronomic Stubble Valuation & Booking",
        "<b>Live Phone Screen</b> on Yield Calculator (or screenshot <code>05_field_details_calculate.png</code>).",
        "Scroll down to show calculation: 14.4 Tonnes biological vs 8.0 Tonnes baler-recoverable. Point to ₹9,600 guaranteed price lock. Tap green [Book Pickup] button.",
        "Next, our agronomic valuation engine applies authentic Punjab Agricultural University research. Instead of unrealistic estimates, we separate total biological residue of 14.4 tonnes from baler-recoverable straw of 8.0 tonnes at 55% pickup efficiency. The farmer locks in a guaranteed earning of 9,600 rupees upfront. With one tap, he books his pickup, and the buyer's pre-funded escrow is held."
    ))
    story.append(Spacer(1, 4))

    story.append(make_scene_box(
        "2:05 – 2:25",
        "Demo Step 3: Web Command Center (PostGIS DBSCAN & OR-Tools)",
        "<b>Browser Dashboard</b> at <code>http://localhost:3000</code> (Buyer Tab) or screenshot <code>06_buyer_command_center.png</code>.",
        "Point cursor to map showing scattered 2-acre plots merging into a contiguous 35-acre cluster (DBSCAN). Point to baler schedule solved by Google OR-Tools in <1.2s.",
        "Now, look at the Web Command Center. How do we make small farms viable for balers? Our PostGIS database runs spatial DBSCAN clustering to group scattered 2-acre parcels into a contiguous 35-acre commercial harvesting corridor. Then, our Google OR-Tools solver dispatches balers and trolleys along optimal routes in under 1.2 seconds, slashing empty travel distance by 66%."
    ))
    story.append(Spacer(1, 4))

    story.append(make_scene_box(
        "2:25 – 2:40",
        "Demo Step 4: Dharamkanta Hardware IoT Telemetry",
        "<b>Browser Dashboard</b> (Weighbridge Tab) or screenshot <code>07_dharamkanta_weighbridge.png</code>.",
        "Zoom into scale readings: Gross 14.20t, Tare 6.20t, Net 8.00t, Moisture 14.2%. Point to green HMAC-SHA256 Encrypted Telemetry lock.",
        "When the truck arrives at the Dharamkanta, our 4,200-rupee ESP32 IoT retrofit device taps directly into the scale's RS-232 serial port. It automatically reads gross and tare weights and digital moisture probe readings, cryptographically signing the ticket. This eliminates weighbridge paper tampering and ghost load fraud."
    ))
    story.append(Spacer(1, 4))

    story.append(make_scene_box(
        "2:40 – 2:55",
        "Demo Step 5: Copernicus Sentinel-2 Satellite Audit & Instant Escrow",
        "<b>Browser Dashboard</b> (KVK / Satellite Tab) or screenshot <code>08_kvk_satellite_audit.png</code>.",
        "Show Sentinel-2 SWIR infrared parcel scan: Delta NBR = 0.08 < 0.10. Click [Approve & Release Escrow]. Show green instant UPI success modal (₹9,600 in 48s).",
        "Finally, zero physical field inspections. European Space Agency Sentinel-2 satellites scan the parcel at 10-meter resolution. A Delta NBR score below 0.10 confirms zero burning occurred. The moment satellite verification clears, escrow instantly transfers 9,600 rupees straight into Sardar Amarjit Singh's bank account via UPI in under 120 seconds, along with an official government Green Certificate."
    ))
    story.append(Spacer(1, 6))

    # ACT 5 & 6
    story.append(make_act_banner("ACT 5 & 6: MACRO IMPACT & CLOSING PITCH (2:55 – 3:45)"))
    story.append(Spacer(1, 3))

    story.append(make_scene_box(
        "2:55 – 3:30",
        "Act 5: Macro Economic & Environmental Scale",
        "Full-screen slide: <code>Impact_Potential_Slide.png</code>.",
        "Zoom into the 4 metric cards: +₹25k farmer gain | 30M t CO₂ cut | 4.4 MMT Bio-CNG for SATAT | 45M protected citizens.",
        "The impact is monumental. For smallholders, a 5-acre farming family gains over 25,000 rupees in supplemental income instead of paying penalties. At national scale, diverting 20 million tonnes of straw produces 4.4 million tonnes of green Bio-CNG under the SATAT initiative, keeps 30 million tonnes of carbon emissions out of our skies, and shields 45 million citizens in Delhi NCR from toxic autumn smog."
    ))
    story.append(Spacer(1, 4))

    story.append(make_scene_box(
        "3:30 – 3:45",
        "Act 6: Team Mist & Visionary Close",
        "Full-screen slide: <code>Team_Slide.png</code> (Title Card, Reg ID: REG-001-OP, and GitHub URL).",
        "Hold still on the title card with clear innovator contact details and repo link. Fade out to black with gentle audio chime.",
        "I am Rishabh Bansal, representing Team Mist at the SEVA First Innovation Challenge 2026. ParaliSetu proves that with the right technology, we can eliminate stubble burning permanently. Thank you!"
    ))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF successfully built: {filename}")

if __name__ == "__main__":
    out_paths = [
        "C:/Users/Rishabh Bansal/Desktop/ParaliSetu_Video_Demo_Screenplay.pdf",
        "C:/Users/Rishabh Bansal/OneDrive/Desktop/ParaliSetu_Video_Demo_Screenplay.pdf",
        "c:/Users/Rishabh Bansal/Downloads/Parali setu/docs/ParaliSetu_Video_Demo_Screenplay.pdf"
    ]
    for p in out_paths:
        try:
            os.makedirs(os.path.dirname(p), exist_ok=True)
            build_pdf(p)
        except Exception as e:
            print(f"Error building {p}: {e}")
