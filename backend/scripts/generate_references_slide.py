import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_references_slide():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    slide_layout = prs.slide_layouts[6] # completely blank layout
    slide = prs.slides.add_slide(slide_layout)

    # ------------------ Color Palette ------------------
    BG_CANVAS = RGBColor(248, 250, 252)       # Slate 50
    CARD_BG = RGBColor(255, 255, 255)         # Pure White
    NAVY_PRIMARY = RGBColor(30, 58, 138)      # Blue 900
    NAVY_HEADING = RGBColor(15, 23, 42)       # Slate 900
    TEXT_DARK = RGBColor(30, 41, 59)          # Slate 800
    TEXT_BODY = RGBColor(51, 65, 85)          # Slate 700
    TEXT_MUTED = RGBColor(100, 116, 139)      # Slate 500
    
    PRIMARY_BLUE = RGBColor(37, 99, 235)      # Blue 600
    BLUE_LIGHT = RGBColor(239, 246, 255)      # Blue 50
    BORDER_BLUE = RGBColor(191, 219, 254)     # Blue 200
    
    GREEN_ACCENT = RGBColor(5, 150, 105)      # Emerald 600
    GREEN_LIGHT = RGBColor(236, 253, 245)     # Emerald 50
    BORDER_GREEN = RGBColor(167, 243, 208)    # Emerald 200
    
    PURPLE_ACCENT = RGBColor(124, 58, 237)    # Purple 600
    PURPLE_LIGHT = RGBColor(245, 243, 255)    # Purple 50
    BORDER_PURPLE = RGBColor(221, 214, 254)   # Purple 200
    
    ROSE_ACCENT = RGBColor(225, 29, 72)       # Rose 600
    ROSE_LIGHT = RGBColor(255, 241, 242)      # Rose 50
    BORDER_ROSE = RGBColor(254, 205, 211)     # Rose 200

    BORDER_CARD = RGBColor(226, 232, 240)     # Slate 200
    ORANGE_BADGE = RGBColor(234, 88, 12)      # Orange 600

    # 0. Native Slide Background Canvas
    bg_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg_shape.fill.solid()
    bg_shape.fill.fore_color.rgb = BG_CANVAS
    bg_shape.line.fill.background()

    # ------------------ 1. Header Elements ------------------
    # 1.1 "Mist" Oval Badge
    badge = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.55), Inches(0.26), Inches(1.20), Inches(0.65))
    badge.fill.solid()
    badge.fill.fore_color.rgb = RGBColor(254, 215, 170)
    badge.line.color.rgb = ORANGE_BADGE
    badge.line.width = Pt(1.5)
    tf_b = badge.text_frame
    p_b = tf_b.paragraphs[0]
    p_b.text = "Mist"
    p_b.font.bold = True
    p_b.font.size = Pt(17)
    p_b.font.color.rgb = RGBColor(154, 52, 18)
    p_b.alignment = PP_ALIGN.CENTER

    # 1.2 Title & Subtitle Textbox
    title_box = slide.shapes.add_textbox(Inches(1.90), Inches(0.20), Inches(8.40), Inches(0.85))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0

    p_t = tf_t.paragraphs[0]
    p_t.text = "References"
    p_t.font.bold = True
    p_t.font.size = Pt(28)
    p_t.font.color.rgb = NAVY_PRIMARY

    p_sub = tf_t.add_paragraph()
    p_sub.text = "Authoritative Research, Government Portals, Statutory Directives & Technical Foundations"
    p_sub.font.size = Pt(11.5)
    p_sub.font.color.rgb = TEXT_MUTED

    # 1.3 Hack for Social Cause Badge
    hack_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.55), Inches(0.26), Inches(2.25), Inches(0.65))
    hack_box.fill.solid()
    hack_box.fill.fore_color.rgb = CARD_BG
    hack_box.line.color.rgb = BORDER_CARD
    hack_box.line.width = Pt(1.5)
    tf_h = hack_box.text_frame
    p_h = tf_h.paragraphs[0]
    p_h.text = "Hack for Social Cause"
    p_h.font.bold = True
    p_h.font.size = Pt(11.5)
    p_h.font.color.rgb = NAVY_HEADING
    p_h.alignment = PP_ALIGN.CENTER

    # ------------------ 2. Four Structured Reference Category Cards (2x2 Grid) ------------------
    col_w = Inches(5.96)
    gutter_x = Inches(0.32)
    left_c1 = Inches(0.55)
    left_c2 = left_c1 + col_w + gutter_x

    row1_t = Inches(1.15)
    row1_h = Inches(2.72)
    row2_t = Inches(4.00)
    row2_h = Inches(2.82)

    categories = [
        # Card 1: Top-Left (Agronomic Ground Truth)
        {
            "x": left_c1, "y": row1_t, "w": col_w, "h": row1_h,
            "title": "🌾 Agronomic & Soil Science Ground Truth",
            "accent": GREEN_ACCENT, "light_bg": GREEN_LIGHT, "border": BORDER_GREEN,
            "entries": [
                {
                    "name": "Punjab Agricultural University (PAU Ludhiana)",
                    "url_label": "Official Portal: pau.edu",
                    "url": "https://www.pau.edu",
                    "domain": "Dept. of Soil Science & Farm Machinery",
                    "data": "Field trial benchmark: 8.5–9.5 t/ha biological residue (~3.6 t/acre) vs 55–60% baler recovery efficiency (~2.0 t/acre). Verified destruction of 33 kg N-P-K-S nutrients per tonne of burned straw."
                },
                {
                    "name": "ICAR-IARI (Indian Agricultural Research Institute)",
                    "url_label": "Official Portal: icar.org.in",
                    "url": "https://icar.org.in",
                    "domain": "Agricultural Biomass & Physics Division",
                    "data": "Crop residue coefficients: Harvest Index (HI ≈ 0.45–0.50) and 1.15–1.25 grain-to-straw ratio establishing ParaliSetu's deterministic yield estimation model."
                }
            ]
        },
        # Card 2: Top-Right (Statutory & Government Schemes)
        {
            "x": left_c2, "y": row1_t, "w": col_w, "h": row1_h,
            "title": "🏛️ Statutory Directives & Clean Energy Schemes",
            "accent": PRIMARY_BLUE, "light_bg": BLUE_LIGHT, "border": BORDER_BLUE,
            "entries": [
                {
                    "name": "Ministry of Petroleum & Natural Gas — SATAT Scheme",
                    "url_label": "Official Portal: gobardhan.sbm.gov.in (MoPNG SATAT)",
                    "url": "https://gobardhan.sbm.gov.in",
                    "domain": "Compressed Bio-Gas (CBG) Unified Registration",
                    "data": "National policy framework establishing ₹1,500–₹2,000/t commercial straw value, 220 kg CBG yield per tonne dry straw, and 4.4 MMT clean Bio-CNG national potential."
                },
                {
                    "name": "Commission for Air Quality Management (CAQM) & Punjab CRM",
                    "url_label": "Portals: caqm.nic.in  •  agri.punjab.gov.in",
                    "url": "https://caqm.nic.in",
                    "domain": "Statutory NCR Oversight & Agriculture Dept.",
                    "data": "Mandatory 5–10% thermal plant biomass co-firing; 50–80% capital subsidies for Custom Hiring Centers (CHCs); ₹1,000/acre ex-situ DBT subsidies and NGT OA 118/2013 penalties."
                }
            ]
        },
        # Card 3: Bottom-Left (Health & Macro-Economic Studies)
        {
            "x": left_c1, "y": row2_t, "w": col_w, "h": row2_h,
            "title": "🩺 Epidemiological Health & Economic Burden",
            "accent": ROSE_ACCENT, "light_bg": ROSE_LIGHT, "border": BORDER_ROSE,
            "entries": [
                {
                    "name": "World Bank & IFPRI Respiratory Health Study",
                    "url_label": "Full Open-Access Paper: pmc.ncbi.nlm.nih.gov/articles/PMC6693809",
                    "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC6693809/",
                    "domain": "Intl. Journal of Epidemiology (Oxford Univ. Press / PMC)",
                    "data": "Groundbreaking study proving 3-fold higher acute respiratory infection risk from crop burning and $35B annual economic loss, establishing the urgent need for ex-situ stubble markets."
                },
                {
                    "name": "World Bank / Clean Air Macroeconomic Valuation",
                    "url_label": "Official Portal: worldbank.org",
                    "url": "https://www.worldbank.org",
                    "domain": "South Asia Environment & Economic Reports",
                    "data": "Quantified $19 Billion (~₹1.5 Lakh Crore) annual macro-economic drain across Delhi-NCR and Indo-Gangetic Plains from hospitalizations, treatments, and lost workforce productivity."
                }
            ]
        },
        # Card 4: Bottom-Right (Algorithms, Space & Open Source)
        {
            "x": left_c2, "y": row2_t, "w": col_w, "h": row2_h,
            "title": "⚡ Algorithmic, Remote Sensing & Software Stack",
            "accent": PURPLE_ACCENT, "light_bg": PURPLE_LIGHT, "border": BORDER_PURPLE,
            "entries": [
                {
                    "name": "Google OR-Tools CP-SAT Optimization Engine",
                    "url_label": "Guide: developers.google.com/optimization/cp/cp_solver",
                    "url": "https://developers.google.com/optimization/cp/cp_solver",
                    "domain": "Operations Research & Constraint Programming",
                    "data": "CP-SAT mathematical formulation resolving multi-stop vehicle capacity, 25km operating radiuses, and 15-day harvest windows in < 2.0s to eliminate baler deadhead transit."
                },
                {
                    "name": "ESA Copernicus Sentinel-2 MSI & ParaliSetu Core Repo",
                    "url_label": "Docs: sentiwiki.copernicus.eu/web/sentinel-2  •  Code: github.com",
                    "url": "https://sentiwiki.copernicus.eu/web/sentinel-2",
                    "domain": "Level-2A SWIR Band 12 & NIR Band 8 (ΔNBR < 0.10)",
                    "data": "Automated post-harvest spectral burn audit issuing tamper-proof No-Burn certificates. Full open-source codebase: 12 PostGIS tables, Flutter client (17MB), and 100% test coverage."
                }
            ]
        }
    ]

    for card in categories:
        # Outer Card Container (Native Shape)
        c_shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, card["x"], card["y"], card["w"], card["h"])
        c_shape.fill.solid()
        c_shape.fill.fore_color.rgb = CARD_BG
        c_shape.line.color.rgb = card["border"]
        c_shape.line.width = Pt(1.5)

        # Header Pill Strip (Native Shape)
        strip_h = Inches(0.36)
        c_strip = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, card["x"] + Inches(0.12), card["y"] + Inches(0.10), card["w"] - Inches(0.24), strip_h)
        c_strip.fill.solid()
        c_strip.fill.fore_color.rgb = card["light_bg"]
        c_strip.line.color.rgb = card["border"]
        c_strip.line.width = Pt(0.8)

        tf_cs = c_strip.text_frame
        tf_cs.word_wrap = True
        tf_cs.margin_left = Inches(0.10)
        tf_cs.margin_top = Inches(0.04)
        p_ch = tf_cs.paragraphs[0]
        p_ch.text = card["title"]
        p_ch.font.bold = True
        p_ch.font.size = Pt(10.0)
        p_ch.font.color.rgb = card["accent"]

        # Content Textbox inside card
        tb_c = slide.shapes.add_textbox(card["x"] + Inches(0.16), card["y"] + Inches(0.50), card["w"] - Inches(0.32), card["h"] - Inches(0.58))
        tf_c = tb_c.text_frame
        tf_c.word_wrap = True
        tf_c.margin_left = tf_c.margin_top = tf_c.margin_right = tf_c.margin_bottom = 0

        for e_idx, e in enumerate(card["entries"]):
            # Entry Title
            pe_1 = tf_c.paragraphs[0] if e_idx == 0 else tf_c.add_paragraph()
            r_ename = pe_1.add_run()
            r_ename.text = f"{e_idx + 1}. {e['name']}"
            r_ename.font.bold = True
            r_ename.font.size = Pt(9.0)
            r_ename.font.color.rgb = NAVY_HEADING

            # Clickable URL & Department
            pe_2 = tf_c.add_paragraph()
            r_elink = pe_2.add_run()
            r_elink.text = f"🔗 {e['url_label']}"
            r_elink.font.bold = True
            r_elink.font.size = Pt(7.8)
            r_elink.font.color.rgb = card["accent"]
            r_elink.hyperlink.address = e["url"]

            r_edom = pe_2.add_run()
            r_edom.text = f"  ({e['domain']})"
            r_edom.font.size = Pt(7.2)
            r_edom.font.color.rgb = TEXT_MUTED

            # Ground truth data extracted
            pe_3 = tf_c.add_paragraph()
            r_edata = pe_3.add_run()
            r_edata.text = f"• Verified Fact: {e['data']}"
            r_edata.font.size = Pt(7.4)
            r_edata.font.color.rgb = TEXT_BODY
            pe_3.space_after = Pt(4.0)

    # ------------------ 3. Ground Truth Verification Bottom Strip ------------------
    verif_box = slide.shapes.add_textbox(Inches(0.55), Inches(6.92), Inches(12.24), Inches(0.24))
    tf_v = verif_box.text_frame
    tf_v.margin_left = tf_v.margin_top = tf_v.margin_right = tf_v.margin_bottom = 0
    p_v = tf_v.paragraphs[0]
    p_v.alignment = PP_ALIGN.CENTER

    r_vt = p_v.add_run()
    r_vt.text = "🔍 Direct Statutory & Research Portals:  "
    r_vt.font.bold = True
    r_vt.font.size = Pt(8.0)
    r_vt.font.color.rgb = NAVY_PRIMARY

    sources_list = [
        ("PAU Agronomy (pau.edu)", "https://www.pau.edu"),
        ("MoPNG GOBARdhan (gobardhan.sbm.gov.in)", "https://gobardhan.sbm.gov.in"),
        ("PMC Study (pmc.ncbi.nlm.nih.gov)", "https://pmc.ncbi.nlm.nih.gov/articles/PMC6693809/"),
        ("OR-Tools CP-SAT (developers.google.com)", "https://developers.google.com/optimization/cp/cp_solver"),
        ("SentiWiki Sentinel-2 (sentiwiki.copernicus.eu)", "https://sentiwiki.copernicus.eu/web/sentinel-2"),
        ("GitHub Repo (Rishabhbansal005)", "https://github.com/Rishabhbansal005/Parali-setu")
    ]

    for s_idx, (s_name, s_url) in enumerate(sources_list):
        if s_idx > 0:
            r_sep = p_v.add_run()
            r_sep.text = "  •  "
            r_sep.font.size = Pt(7.8)
            r_sep.font.color.rgb = TEXT_MUTED

        r_s = p_v.add_run()
        r_s.text = s_name
        r_s.font.size = Pt(7.8)
        r_s.font.bold = True
        r_s.font.color.rgb = PRIMARY_BLUE
        r_s.hyperlink.address = s_url

    # ------------------ 4. Footer ------------------
    footer_box = slide.shapes.add_textbox(Inches(0.55), Inches(7.18), Inches(12.24), Inches(0.22))
    tf_f = footer_box.text_frame
    tf_f.margin_left = tf_f.margin_top = tf_f.margin_right = tf_f.margin_bottom = 0
    p_f = tf_f.paragraphs[0]
    p_f.text = "@HSC submission- Template  |  ParaliSetu: Comprehensive Research Citations & Verification Directory"
    p_f.font.size = Pt(8.5)
    p_f.font.color.rgb = TEXT_MUTED
    p_f.alignment = PP_ALIGN.CENTER

    # Save Presentation
    output_path = r"c:\Users\Rishabh Bansal\Downloads\Parali setu\References_Slide.pptx"
    prs.save(output_path)
    print(f"Native References PPTX saved successfully to {output_path}")

if __name__ == "__main__":
    build_references_slide()
