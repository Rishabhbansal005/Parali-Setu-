import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_beautiful_feasibility_risk_slide():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    slide_layout = prs.slide_layouts[6] # blank layout
    slide = prs.slides.add_slide(slide_layout)

    # ------------------ Curated Modern Color Palette ------------------
    BG_CANVAS = RGBColor(248, 250, 252)       # Slate 50 clean background
    CARD_BG = RGBColor(255, 255, 255)         # Pure White
    NAVY_HEADING = RGBColor(15, 23, 42)       # Slate 900
    NAVY_PRIMARY = RGBColor(30, 58, 138)      # Blue 900
    TEXT_DARK = RGBColor(30, 41, 59)          # Slate 800
    TEXT_BODY = RGBColor(51, 65, 85)          # Slate 700 (High contrast)
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

    # 0. Slide Background Canvas
    bg_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg_shape.fill.solid()
    bg_shape.fill.fore_color.rgb = BG_CANVAS
    bg_shape.line.fill.background()

    # ------------------ 1. Header Elements ------------------
    # 1.1 "Mist" Oval Badge
    badge = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.60), Inches(0.28), Inches(1.20), Inches(0.65))
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

    # 1.2 Title & Subtitle with Generous Line Height
    title_box = slide.shapes.add_textbox(Inches(1.95), Inches(0.22), Inches(8.30), Inches(0.85))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0

    p_t = tf_t.paragraphs[0]
    p_t.text = "Feasibility and Risk Analysis"
    p_t.font.bold = True
    p_t.font.size = Pt(27)
    p_t.font.color.rgb = NAVY_PRIMARY

    p_sub = tf_t.add_paragraph()
    p_sub.text = "Rigorous Technical & Operational Viability Paired with Multi-Tier Defensive Guardrails"
    p_sub.font.size = Pt(11.5)
    p_sub.font.color.rgb = TEXT_MUTED

    # 1.3 Hack for Social Cause Badge
    hack_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.50), Inches(0.28), Inches(2.25), Inches(0.65))
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

    # ------------------ 2. Two-Column Layout (Generous Breathing Room) ------------------
    # Left Zone: Feasibility (Width: 5.85")
    # Right Zone: Risk Mitigation (Width: 6.00")
    # Gutter Gap: 0.28"
    zone_top = Inches(1.15)
    zone_h = Inches(5.62)
    left_x = Inches(0.60)
    left_w = Inches(5.88)
    right_x = Inches(6.76)
    right_w = Inches(5.98)

    # ==================== ZONE 1: FEASIBILITY ASSESSMENT ====================
    # Outer Container
    card_left = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_x, zone_top, left_w, zone_h)
    card_left.fill.solid()
    card_left.fill.fore_color.rgb = CARD_BG
    card_left.line.color.rgb = BORDER_BLUE
    card_left.line.width = Pt(1.2)

    # Zone 1 Header
    tb_zh1 = slide.shapes.add_textbox(left_x + Inches(0.25), zone_top + Inches(0.18), left_w - Inches(0.50), Inches(0.50))
    tf_zh1 = tb_zh1.text_frame
    tf_zh1.word_wrap = True
    tf_zh1.margin_left = tf_zh1.margin_top = tf_zh1.margin_right = tf_zh1.margin_bottom = 0

    p_zh1 = tf_zh1.paragraphs[0]
    p_zh1.text = "✅  Feasibility Analysis of Solution"
    p_zh1.font.bold = True
    p_zh1.font.size = Pt(14.0)
    p_zh1.font.color.rgb = NAVY_PRIMARY

    p_zh1_sub = tf_zh1.add_paragraph()
    p_zh1_sub.text = "Empirically Grounded in Rural Field Operations, Optimization & Clean Energy"
    p_zh1_sub.font.bold = True
    p_zh1_sub.font.size = Pt(8.8)
    p_zh1_sub.font.color.rgb = PRIMARY_BLUE

    # 3 Large Feasibility Pillar Blocks (Vertical Stack)
    f_items = [
        {
            "icon": "🛠️",
            "title": "Technical Feasibility",
            "badge": "PROVEN IN TESTS",
            "badge_color": PRIMARY_BLUE,
            "badge_bg": BLUE_LIGHT,
            "headline": "Sub-2s Constraint Solver & Offline 17 MB Client",
            "bullets": [
                "Google OR-Tools CP-SAT solves multi-stop capacity, time-windows, and baler-truck-buyer matching in < 2.0 seconds.",
                "Ultra-light 17.03 MB split APK with SQLite cache operates seamlessly in low-connectivity rural 2G/3G zones."
            ],
            "source_label": "🔗 Source: Google OR-Tools & Flutter Engine",
            "source_url": "https://developers.google.com/optimization"
        },
        {
            "icon": "🚜",
            "title": "Operational Feasibility",
            "badge": "FIELD-VIABLE",
            "badge_color": GREEN_ACCENT,
            "badge_bg": GREEN_LIGHT,
            "headline": "De-Bottlenecking the Acute 15-Day Harvest Crunch",
            "bullets": [
                "Spatially clusters adjacent 2–4 acre fields into 25–40 acre contiguous runs, boosting baler run rates to 85%.",
                "Integrates existing rural assets: 1,500+ Custom Hiring Centers (CHCs) and village Dharamkanta scales without new hardware."
            ],
            "source_label": "🔗 Source: Punjab CRM Guidelines (agri.punjab.gov.in)",
            "source_url": "https://agri.punjab.gov.in"
        },
        {
            "icon": "📈",
            "title": "Economic Viability",
            "badge": "SELF-SUSTAINING",
            "badge_color": PURPLE_ACCENT,
            "badge_bg": PURPLE_LIGHT,
            "headline": "Robust Unit Economics for Farmers & Industrial Offtakers",
            "bullets": [
                "Delivered parali @ ₹1,500/t offers a 57% cost advantage over imported fossil fuels / coal (₹3,500/t parity).",
                "Replaces ₹15,000 burning fine liability with ₹2,500–₹3,000/acre net income + unlocks ₹1,000/acre ex-situ DBT subsidies."
            ],
            "source_label": "🔗 Source: MoPNG SATAT CBG Framework (mopng.gov.in)",
            "source_url": "https://mopng.gov.in"
        }
    ]

    block_y_start = zone_top + Inches(0.72)
    block_h = Inches(1.50)
    block_gap = Inches(0.12)

    for idx, f in enumerate(f_items):
        cur_by = block_y_start + idx * (block_h + block_gap)
        b_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_x + Inches(0.20), cur_by, left_w - Inches(0.40), block_h)
        b_box.fill.solid()
        b_box.fill.fore_color.rgb = f["badge_bg"]
        b_box.line.color.rgb = BORDER_CARD
        b_box.line.width = Pt(1.0)

        tb_fc = slide.shapes.add_textbox(left_x + Inches(0.32), cur_by + Inches(0.08), left_w - Inches(0.64), block_h - Inches(0.16))
        tf_fc = tb_fc.text_frame
        tf_fc.word_wrap = True
        tf_fc.margin_left = tf_fc.margin_top = tf_fc.margin_right = tf_fc.margin_bottom = 0

        # Title + Badge
        p_f1 = tf_fc.paragraphs[0]
        r_ficon = p_f1.add_run()
        r_ficon.text = f"{f['icon']} {f['title']}  "
        r_ficon.font.bold = True
        r_ficon.font.size = Pt(11.5)
        r_ficon.font.color.rgb = NAVY_HEADING

        r_fbadge = p_f1.add_run()
        r_fbadge.text = f"[{f['badge']}]"
        r_fbadge.font.bold = True
        r_fbadge.font.size = Pt(8.5)
        r_fbadge.font.color.rgb = f["badge_color"]

        # Headline
        p_f2 = tf_fc.add_paragraph()
        p_f2.text = f["headline"]
        p_f2.font.bold = True
        p_f2.font.size = Pt(9.8)
        p_f2.font.color.rgb = f["badge_color"]
        p_f2.space_before = Pt(2.0)
        p_f2.space_after = Pt(2.0)

        # Bullet 1
        p_b1 = tf_fc.add_paragraph()
        r_b1 = p_b1.add_run()
        r_b1.text = f"• {f['bullets'][0]}"
        r_b1.font.size = Pt(9.0)
        r_b1.font.color.rgb = TEXT_BODY
        p_b1.space_after = Pt(1.5)

        # Bullet 2
        p_b2 = tf_fc.add_paragraph()
        r_b2 = p_b2.add_run()
        r_b2.text = f"• {f['bullets'][1]}"
        r_b2.font.size = Pt(9.0)
        r_b2.font.color.rgb = TEXT_BODY
        p_b2.space_after = Pt(2.0)

        # Source link
        p_src = tf_fc.add_paragraph()
        r_slink = p_src.add_run()
        r_slink.text = f["source_label"]
        r_slink.font.bold = True
        r_slink.font.size = Pt(8.2)
        r_slink.font.color.rgb = f["badge_color"]
        r_slink.hyperlink.address = f["source_url"]


    # ==================== ZONE 2: RISKS & MITIGATION STRATEGIES ====================
    # Outer Container
    card_right = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_x, zone_top, right_w, zone_h)
    card_right.fill.solid()
    card_right.fill.fore_color.rgb = CARD_BG
    card_right.line.color.rgb = BORDER_ROSE
    card_right.line.width = Pt(1.2)

    # Zone 2 Header
    tb_zh2 = slide.shapes.add_textbox(right_x + Inches(0.25), zone_top + Inches(0.18), right_w - Inches(0.50), Inches(0.50))
    tf_zh2 = tb_zh2.text_frame
    tf_zh2.word_wrap = True
    tf_zh2.margin_left = tf_zh2.margin_top = tf_zh2.margin_right = tf_zh2.margin_bottom = 0

    p_zh2 = tf_zh2.paragraphs[0]
    p_zh2.text = "⚠️  Potential Challenges & Risk Mitigation"
    p_zh2.font.bold = True
    p_zh2.font.size = Pt(14.0)
    p_zh2.font.color.rgb = NAVY_PRIMARY

    p_zh2_sub = tf_zh2.add_paragraph()
    p_zh2_sub.text = "Proactive Guardrails Engineered Against Field Deadlocks, Fraud & Bias"
    p_zh2_sub.font.bold = True
    p_zh2_sub.font.size = Pt(8.8)
    p_zh2_sub.font.color.rgb = ROSE_ACCENT

    # 3 Big Risk Mitigation Cards
    r_items = [
        {
            "icon": "🌾",
            "name": "Agronomic Yield Discrepancy",
            "pill": "MITIGATED BY DESIGN",
            "pill_color": GREEN_ACCENT,
            "pill_bg": GREEN_LIGHT,
            "challenge": "Total biological residue (~3.6 t/acre) exceeds baler-recoverable straw (~2.0 t/acre). Farmers may expect payout on gross biomass and suspect foul play.",
            "strategy": "Dual-metric transparent UI displays both field residue & baler recovery factors (PR-126/Pusa-44). Payment is locked exclusively to physical certified weighbridge tickets.",
            "guardrail": "PAU yield coefficients in stubble_config.py + Dharamkanta gross/tare net settlement."
        },
        {
            "icon": "📱",
            "name": "Rural Digital Divide & Audio Noise",
            "pill": "FAIL-SAFE GUARDRAIL",
            "pill_color": PRIMARY_BLUE,
            "pill_bg": BLUE_LIGHT,
            "challenge": "Low smartphone literacy; heavy ambient tractor/combine acoustic noise causing vernacular speech-to-text transcription errors or dialect mismatches.",
            "strategy": "Voice intake triggers an explicit confirmation pop-up (*'Aapne bola: 4 Killa, Sahi hai?'*). Instant 1-tap manual UI fallback with steppers; zero blocked journeys.",
            "guardrail": "Mandatory farmer audio confirmation + full manual offline-capable fallback."
        },
        {
            "icon": "🏛️",
            "name": "Scale Fraud & Subsidy Tampering",
            "pill": "SATELLITE VERIFIED",
            "pill_color": PURPLE_ACCENT,
            "pill_bg": PURPLE_LIGHT,
            "challenge": "Paper weighbridge tickets forged by drivers; fake non-burning claims to pocket government ₹1,000/acre ex-situ subsidies without clearing straw.",
            "strategy": "Automated OCR cross-check (|Gross - Tare - Net| <= 0.02t) + dual confirmation. Remote Copernicus Sentinel-2 SWIR (ΔNBR < 0.10) independent satellite audit.",
            "guardrail": "Cryptographic Row-Level Security (RLS) + tamper-proof satellite No-Burn certificate."
        }
    ]

    for jdx, r in enumerate(r_items):
        cur_ry = block_y_start + jdx * (block_h + block_gap)
        r_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_x + Inches(0.20), cur_ry, right_w - Inches(0.40), block_h)
        r_box.fill.solid()
        r_box.fill.fore_color.rgb = r["pill_bg"]
        r_box.line.color.rgb = BORDER_CARD
        r_box.line.width = Pt(1.0)

        tb_rc = slide.shapes.add_textbox(right_x + Inches(0.32), cur_ry + Inches(0.08), right_w - Inches(0.64), block_h - Inches(0.16))
        tf_rc = tb_rc.text_frame
        tf_rc.word_wrap = True
        tf_rc.margin_left = tf_rc.margin_top = tf_rc.margin_right = tf_rc.margin_bottom = 0

        # Title + Pill
        p_r1 = tf_rc.paragraphs[0]
        r_ricon = p_r1.add_run()
        r_ricon.text = f"{r['icon']} {r['name']}  "
        r_ricon.font.bold = True
        r_ricon.font.size = Pt(11.5)
        r_ricon.font.color.rgb = NAVY_HEADING

        r_rpill = p_r1.add_run()
        r_rpill.text = f"[{r['pill']}]"
        r_rpill.font.bold = True
        r_rpill.font.size = Pt(8.5)
        r_rpill.font.color.rgb = r["pill_color"]

        # Challenge
        p_r2 = tf_rc.add_paragraph()
        r_ch_tag = p_r2.add_run()
        r_ch_tag.text = "⚠️ Potential Challenge: "
        r_ch_tag.font.bold = True
        r_ch_tag.font.size = Pt(9.0)
        r_ch_tag.font.color.rgb = ROSE_ACCENT
        r_ch_txt = p_r2.add_run()
        r_ch_txt.text = r["challenge"]
        r_ch_txt.font.size = Pt(8.8)
        r_ch_txt.font.color.rgb = TEXT_BODY
        p_r2.space_before = Pt(2.0)
        p_r2.space_after = Pt(2.0)

        # Mitigation Strategy
        p_r3 = tf_rc.add_paragraph()
        r_st_tag = p_r3.add_run()
        r_st_tag.text = "✅ Mitigation Strategy: "
        r_st_tag.font.bold = True
        r_st_tag.font.size = Pt(9.0)
        r_st_tag.font.color.rgb = GREEN_ACCENT
        r_st_txt = p_r3.add_run()
        r_st_txt.text = r["strategy"]
        r_st_txt.font.size = Pt(8.8)
        r_st_txt.font.color.rgb = TEXT_BODY
        p_r3.space_after = Pt(2.0)

        # Tech Guardrail
        p_r4 = tf_rc.add_paragraph()
        r_gd_tag = p_r4.add_run()
        r_gd_tag.text = "🛡️ Tech Guardrail: "
        r_gd_tag.font.bold = True
        r_gd_tag.font.size = Pt(8.5)
        r_gd_tag.font.color.rgb = PRIMARY_BLUE
        r_gd_txt = p_r4.add_run()
        r_gd_txt.text = r["guardrail"]
        r_gd_txt.font.size = Pt(8.2)
        r_gd_txt.font.color.rgb = TEXT_MUTED


    # ------------------ 3. Ground Truth Verification Bottom Strip ------------------
    verif_box = slide.shapes.add_textbox(Inches(0.60), Inches(6.88), Inches(12.13), Inches(0.24))
    tf_v = verif_box.text_frame
    tf_v.margin_left = tf_v.margin_top = tf_v.margin_right = tf_v.margin_bottom = 0
    p_v = tf_v.paragraphs[0]
    p_v.alignment = PP_ALIGN.CENTER

    r_vt = p_v.add_run()
    r_vt.text = "🔍 Official Verification Sources & Standards:  "
    r_vt.font.bold = True
    r_vt.font.size = Pt(8.5)
    r_vt.font.color.rgb = NAVY_PRIMARY

    sources_list = [
        ("Google OR-Tools CP-SAT (developers.google.com/optimization)", "https://developers.google.com/optimization"),
        ("PAU Stubble Soil Agronomy (pau.edu)", "https://www.pau.edu"),
        ("MoPNG SATAT CBG Scheme (mopng.gov.in)", "https://mopng.gov.in"),
        ("ESA Copernicus Sentinel-2 SWIR (sentinels.copernicus.eu)", "https://sentinels.copernicus.eu")
    ]

    for s_idx, (s_name, s_url) in enumerate(sources_list):
        if s_idx > 0:
            r_sep = p_v.add_run()
            r_sep.text = "  •  "
            r_sep.font.size = Pt(8.2)
            r_sep.font.color.rgb = TEXT_MUTED

        r_s = p_v.add_run()
        r_s.text = s_name
        r_s.font.size = Pt(8.2)
        r_s.font.bold = True
        r_s.font.color.rgb = PRIMARY_BLUE
        r_s.hyperlink.address = s_url

    # ------------------ 4. Footer ------------------
    footer_box = slide.shapes.add_textbox(Inches(0.60), Inches(7.18), Inches(12.13), Inches(0.22))
    tf_f = footer_box.text_frame
    tf_f.margin_left = tf_f.margin_top = tf_f.margin_right = tf_f.margin_bottom = 0
    p_f = tf_f.paragraphs[0]
    p_f.text = "@HSC submission- Template  |  ParaliSetu: Feasibility and Risk Analysis Matrix"
    p_f.font.size = Pt(8.5)
    p_f.font.color.rgb = TEXT_MUTED
    p_f.alignment = PP_ALIGN.CENTER

    # Save Presentation
    output_path = r"c:\Users\Rishabh Bansal\Downloads\Parali setu\Feasibility_and_Risk_Analysis_Slide.pptx"
    prs.save(output_path)
    print(f"Beautiful Feasibility & Risk slide saved successfully to {output_path}")

if __name__ == "__main__":
    build_beautiful_feasibility_risk_slide()
