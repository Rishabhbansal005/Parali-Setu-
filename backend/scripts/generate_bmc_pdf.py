import os
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

pdf_path = r"c:\Users\Rishabh Bansal\Downloads\Parali setu\docs\business\ParaliSetu_Business_Model_Canvas.pdf"
doc = SimpleDocTemplate(
    pdf_path,
    pagesize=landscape(letter),
    leftMargin=24,
    rightMargin=24,
    topMargin=20,
    bottomMargin=20
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    'DocTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=14,
    leading=16,
    textColor=colors.HexColor('#065f46')
)

subtitle_style = ParagraphStyle(
    'DocSubTitle',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=8,
    leading=10,
    textColor=colors.HexColor('#475569')
)

box_title = ParagraphStyle(
    'BoxTitle',
    parent=styles['Normal'],
    fontName='Helvetica-Bold',
    fontSize=8.5,
    leading=11,
    textColor=colors.HexColor('#047857')
)

body = ParagraphStyle(
    'BoxBody',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=6.8,
    leading=8.5,
    textColor=colors.HexColor('#1e293b')
)

bullet = ParagraphStyle(
    'BoxBullet',
    parent=styles['Normal'],
    fontName='Helvetica',
    fontSize=6.6,
    leading=8.2,
    textColor=colors.HexColor('#334155'),
    leftIndent=6
)

# Header
header_data = [
    [
        Paragraph("<b>ParaliSetu — Business Model Canvas</b><br/><font color='#047857' size='8'>AI-Driven Hyperlocal Stubble Supply Chain, Baler Fleet Logistics & Escrow Marketplace</font>", title_style),
        Paragraph("<b>Hackathon:</b> Hack for Social | <b>Theme:</b> Environment & Sustainability<br/><b>Repository:</b> github.com/Rishabhbansal005/Parali-setu | <b>Target:</b> Punjab & Haryana", subtitle_style)
    ]
]
header_table = Table(header_data, colWidths=[480, 260])
header_table.setStyle(TableStyle([
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
]))

# 9 Blocks Content
kp_text = """
<b>8. KEY PARTNERS</b><br/>
• <b>Industrial Offtakers:</b> Bio-CNG (SATAT scheme, e.g. Verbio Sangrur), 2G ethanol (IOCL Panipat), & biomass boilers.<br/>
• <b>Custom Hiring Centres (CHCs):</b> Subsidized machinery pools with idle balers/rakes.<br/>
• <b>Baler & Tractor Operators:</b> Rural transport entrepreneurs.<br/>
• <b>Village Dharamkanta:</b> Neutral independent weighbridges.<br/>
• <b>Institutions:</b> Punjab & Haryana Agri Depts, KVKs, CAQM.
"""

ka_text = """
<b>6. KEY ACTIVITIES</b><br/>
• <b>PostGIS Spatial Clustering:</b> Grouping smallholdings into contiguous 35-acre runs.<br/>
• <b>Vernacular Voice AI:</b> Punjabi/Hindi speech-to-booking pipeline.<br/>
• <b>Weighbridge Escrow Integration:</b> Scale ticket verification & automated T+1 ACH/UPI bank payouts.
"""

kr_text = """
<b>7. KEY RESOURCES</b><br/>
• <b>Proprietary Tech:</b> PostGIS spatial engine & Indic speech model.<br/>
• <b>PAU Agronomic Formula:</b> Calibrated yield factors (2.0 t/acre baler recovery).<br/>
• <b>Ecosystem Network:</b> 500+ baler fleet directory & SATAT off-taker contracts.
"""

vp_text = """
<b>2. VALUE PROPOSITIONS</b><br/>
• <b>Smallholder Farmers (1–4 Acres):</b><br/>
  - <b>Free field clearing</b> in 48–72h before wheat sowing.<br/>
  - <b>₹1,200–₹1,800/acre net income</b> (₹650/tonne direct payout).<br/>
  - Zero CAQM pollution fines + In-App No-Burn Certificate.<br/><br/>
• <b>Baler & Tractor Aggregators:</b><br/>
  - Contiguous 30-acre runs eliminate transit deadhead miles.<br/>
  - <b>+32% diesel fuel efficiency</b> and maximized seasonal revenue.<br/><br/>
• <b>Industrial Biomass Buyers:</b><br/>
  - Predictable, moisture-tested daily feedstock schedule.<br/>
  - Eliminates costly digester & boiler shutdowns.
"""

cr_text = """
<b>4. CUSTOMER RELATIONSHIPS</b><br/>
• <b>Voice-First Simplicity:</b> Zero learning curve for illiterate farmers.<br/>
• <b>Dharamkanta Scale Transparency:</b> Weight verified locally before dispatch.<br/>
• <b>SMS & WhatsApp Slips:</b> Instant payment receipts for basic phone users.
"""

ch_text = """
<b>3. CHANNELS</b><br/>
• <b>Flutter Mobile App:</b> Lightweight 17MB Android app with offline voice fallback.<br/>
• <b>Next.js Operations Web Portal:</b> Scale ticket logging & buyer command center.<br/>
• <b>Village Physical Nodes:</b> Custom Hiring Centres (CHCs) & Dharamkanta kiosks.
"""

cs_text = """
<b>1. CUSTOMER SEGMENTS</b><br/>
• <b>Primary Beneficiaries:</b><br/>
  Small & marginal farmers (1–4 acres) facing 15-day harvest deadline. <b>Pays ₹0.</b><br/><br/>
• <b>Paying Customers:</b><br/>
  Bio-CNG (CBG) refineries under <b>SATAT mandatory blending (1% to 5%)</b>, 2G ethanol plants, and industrial boilers.<br/><br/>
• <b>Supply Operators:</b><br/>
  Custom Hiring Centre (CHC) baler owners & rural tractor fleets.
"""

cost_text = """
<b>9. COST STRUCTURE</b><br/>
• <b>Technology & Platform (Fixed):</b> Supabase PostGIS cloud DB, Next.js hosting: ₹35,000/mo. Voice Whisper/Gemini ASR tokens: ₹0.27/intake.<br/>
• <b>Field Operations (Variable Peak):</b> Village Cluster Coordinators (Kisan Mitras) across 15 pilot clusters. Handheld moisture testers (₹2,500/unit).<br/>
• <b>Compliance & Audits:</b> Sentinel-2 satellite processing overhead & banking escrow transaction fees.
"""

rev_text = """
<b>5. REVENUE STREAMS & FINANCIAL MODEL</b><br/>
• <b>Primary B2B Take-Rate:</b> ₹150 / Tonne (5.8% commission on ₹2,600 delivered gate price paid by buyers; <b>0% farmer fee</b>).<br/>
• <b>Baler Optimization SaaS:</b> ₹40 / Tonne software fee for pre-clustered contiguous runs.<br/>
• <b>Enterprise ESG Data:</b> Traceability & Scope 3 carbon audit fees for Oil Marketing Companies.<br/>
• <b>Financial Viability:</b> Break-even at 20,000 Tonnes (~10,000 acres). <b>Year 3 Target: ₹15.0 Cr Revenue | ₹12.6 Cr EBITDA.</b>
"""

# Build Table Data
col_w = 740 / 5.0 # 148 each
row1_h = 175
row2_h = 175
bottom_h = 105

# Layout:
# Col 0: KP (row1+row2)
# Col 1: KA (row1), KR (row2)
# Col 2: VP (row1+row2)
# Col 3: CR (row1), CH (row2)
# Col 4: CS (row1+row2)

grid_data = [
    [
        Paragraph(kp_text, body),
        Paragraph(ka_text, body),
        Paragraph(vp_text, body),
        Paragraph(cr_text, body),
        Paragraph(cs_text, body),
    ],
    [
        "", # merged with KP
        Paragraph(kr_text, body),
        "", # merged with VP
        Paragraph(ch_text, body),
        "", # merged with CS
    ],
    [
        Paragraph(cost_text, body),
        "",
        "",
        Paragraph(rev_text, body),
        ""
    ]
]

grid_table = Table(grid_data, colWidths=[148, 148, 148, 148, 148], rowHeights=[175, 175, 105])
grid_table.setStyle(TableStyle([
    ('SPAN', (0,0), (0,1)), # KP spans row 0-1
    ('SPAN', (2,0), (2,1)), # VP spans row 0-1
    ('SPAN', (4,0), (4,1)), # CS spans row 0-1
    ('SPAN', (0,2), (2,2)), # Cost spans col 0-2
    ('SPAN', (3,2), (4,2)), # Revenue spans col 3-4

    ('BACKGROUND', (0,0), (-1,-1), colors.white),
    ('BACKGROUND', (2,0), (2,1), colors.HexColor('#f0fdf4')), # VP green tint
    ('BACKGROUND', (3,2), (4,2), colors.HexColor('#f0fdf4')), # Rev green tint

    ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor('#059669')),
    ('INNERGRID', (0,0), (-1,-1), 0.75, colors.HexColor('#cbd5e1')),
    
    ('TOPPADDING', (0,0), (-1,-1), 6),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('LEFTPADDING', (0,0), (-1,-1), 6),
    ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
]))

elements = [
    header_table,
    Spacer(1, 4),
    grid_table
]

doc.build(elements)
print(f"SUCCESS: Generated {pdf_path} (size: {os.path.getsize(pdf_path)} bytes)")
