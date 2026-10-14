import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_native_team_slide():
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
    p_t.text = "Team Composition & Engineering Division"
    p_t.font.bold = True
    p_t.font.size = Pt(27)
    p_t.font.color.rgb = NAVY_PRIMARY

    p_sub = tf_t.add_paragraph()
    p_sub.text = "Three-Tier Architecture Ownership, Real Field Challenges & Hackathon Build Journey"
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

    # ------------------ 2. Section 1: Three Team Member Cards (100% Native PPTX Shapes) ------------------
    card_top = Inches(1.12)
    card_h = Inches(3.92)
    card_w = Inches(3.86)
    card_gap = Inches(0.33)
    start_x = Inches(0.55)

    team_members = [
        {
            "monogram": "RB",
            "name": "Rishabh Bansal",
            "role": "Lead Architect & Optimization",
            "part": "PART 1: CORE BRAIN & OPTIMIZATION",
            "accent": PRIMARY_BLUE,
            "light_bg": BLUE_LIGHT,
            "border": BORDER_BLUE,
            "pills": "[FastAPI]  [Supabase PostGIS]  [OR-Tools]  [⚡ <2.0s Match]",
            "contributions": [
                ("Central Gateway & RLS", "Built 12 normalized PostgreSQL tables with PostGIS spatial indexing & JWT security."),
                ("Google OR-Tools CP-SAT", "Formulated NP-hard multi-sided CP-SAT solver (Farmer-Baler-Truck-Buyer)."),
                ("PAU Agronomic Engine", "Empirical matrix distinguishing biological total (~3.6t) vs baler recovery (~2.0t).")
            ],
            "challenge": "Multi-stop vehicle capacity deadlock under 15-day harvest crunch.",
            "mitigation": "25–40 acre contiguous farm clustering with progressive radius relaxation."
        },
        {
            "monogram": "RS",
            "name": "Ravi Singh",
            "role": "Mobile Systems & Vernacular AI",
            "part": "PART 2: FARMER APP & VERNACULAR AI",
            "accent": GREEN_ACCENT,
            "light_bg": GREEN_LIGHT,
            "border": BORDER_GREEN,
            "pills": "[Flutter 3.x]  [Bhashini STT]  [Gemini 1.5]  [📦 17.03 MB Split APK]",
            "contributions": [
                ("Trilingual Mobile Client", "Cross-platform Android app in Punjabi, Hindi & English for 2G/3G rural networks."),
                ("Vernacular Voice Pipeline", "Integrated Bhashini/Whisper STT with Gemini 1.5 entity parser for natural speech intake."),
                ("Offline-First Resilience", "Client-side SQLite cache and 100% deterministic manual UI fallback with steppers.")
            ],
            "challenge": "Heavy ambient tractor/combine acoustic noise causing vernacular STT errors.",
            "mitigation": "Enforced mandatory audio confirmation readback (\"4 Killa, Sahi hai?\")."
        },
        {
            "monogram": "VY",
            "name": "Vaibhav Yadav",
            "role": "Web Platforms & Satellite / Anti-Fraud",
            "part": "PART 3: INDUSTRIAL WEB & AUDIT",
            "accent": PURPLE_ACCENT,
            "light_bg": PURPLE_LIGHT,
            "border": BORDER_PURPLE,
            "pills": "[Next.js 14]  [TailwindCSS]  [Sentinel-2 SWIR]  [🛰️ ΔNBR < 0.10 Audit]",
            "contributions": [
                ("Buyer Command Portals", "Next.js dashboard for industrial Bio-CNG plants (demand quotas & escrow funding)."),
                ("Dharamkanta Scale OCR", "Mobile weighbridge ticket intake with OCR & scale integrity check (|G-T-N| <= 0.02t)."),
                ("Sentinel-2 SWIR Satellite", "Remote post-harvest burn audit to auto-issue tamper-proof No-Burn certificates.")
            ],
            "challenge": "Door-to-door village audits physically impossible across 3M hectares.",
            "mitigation": "Remote sensing burn audit + digital weighbridge escrow release."
        }
    ]

    for i, m in enumerate(team_members):
        cur_x = start_x + i * (card_w + card_gap)
        
        # 1. Native Outer Card Container
        m_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cur_x, card_top, card_w, card_h)
        m_card.fill.solid()
        m_card.fill.fore_color.rgb = CARD_BG
        m_card.line.color.rgb = m["border"]
        m_card.line.width = Pt(1.5)

        # 2. Monogram Avatar Badge (Native Rounded Rectangle)
        avatar = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cur_x + Inches(0.16), card_top + Inches(0.14), Inches(0.55), Inches(0.55))
        avatar.fill.solid()
        avatar.fill.fore_color.rgb = m["accent"]
        avatar.line.fill.background()
        tf_av = avatar.text_frame
        p_av = tf_av.paragraphs[0]
        p_av.text = m["monogram"]
        p_av.font.bold = True
        p_av.font.size = Pt(15)
        p_av.font.color.rgb = RGBColor(255, 255, 255)
        p_av.alignment = PP_ALIGN.CENTER

        # 3. Member Name & Role Textbox
        tb_nr = slide.shapes.add_textbox(cur_x + Inches(0.80), card_top + Inches(0.10), card_w - Inches(0.92), Inches(0.60))
        tf_nr = tb_nr.text_frame
        tf_nr.word_wrap = True
        tf_nr.margin_left = tf_nr.margin_top = tf_nr.margin_right = tf_nr.margin_bottom = 0

        p_name = tf_nr.paragraphs[0]
        p_name.text = m["name"]
        p_name.font.bold = True
        p_name.font.size = Pt(14)
        p_name.font.color.rgb = NAVY_HEADING

        p_role = tf_nr.add_paragraph()
        p_role.text = m["role"]
        p_role.font.bold = True
        p_role.font.size = Pt(8.5)
        p_role.font.color.rgb = m["accent"]

        # 4. Division Pill Badge (Native Rounded Rectangle)
        div_pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cur_x + Inches(0.16), card_top + Inches(0.76), Inches(2.70), Inches(0.24))
        div_pill.fill.solid()
        div_pill.fill.fore_color.rgb = m["light_bg"]
        div_pill.line.color.rgb = m["border"]
        div_pill.line.width = Pt(0.8)
        tf_dp = div_pill.text_frame
        p_dp = tf_dp.paragraphs[0]
        p_dp.text = m["part"]
        p_dp.font.bold = True
        p_dp.font.size = Pt(7.2)
        p_dp.font.color.rgb = m["accent"]
        p_dp.alignment = PP_ALIGN.CENTER

        # 5. Tech Stack Pills Box
        tb_pills = slide.shapes.add_textbox(cur_x + Inches(0.16), card_top + Inches(1.04), card_w - Inches(0.32), Inches(0.24))
        tf_pills = tb_pills.text_frame
        tf_pills.margin_left = tf_pills.margin_top = tf_pills.margin_right = tf_pills.margin_bottom = 0
        p_pills = tf_pills.paragraphs[0]
        p_pills.text = m["pills"]
        p_pills.font.bold = True
        p_pills.font.size = Pt(7.4)
        p_pills.font.color.rgb = TEXT_DARK

        # 6. Section Header Textbox
        tb_sec = slide.shapes.add_textbox(cur_x + Inches(0.16), card_top + Inches(1.30), card_w - Inches(0.32), Inches(0.20))
        tf_sec = tb_sec.text_frame
        tf_sec.margin_left = tf_sec.margin_top = tf_sec.margin_right = tf_sec.margin_bottom = 0
        p_sec = tf_sec.paragraphs[0]
        p_sec.text = "🎯 CORE TECHNICAL OWNERSHIP"
        p_sec.font.bold = True
        p_sec.font.size = Pt(8.0)
        p_sec.font.color.rgb = NAVY_HEADING

        # 7. Contributions Bullets Textbox
        tb_con = slide.shapes.add_textbox(cur_x + Inches(0.16), card_top + Inches(1.50), card_w - Inches(0.32), Inches(1.30))
        tf_con = tb_con.text_frame
        tf_con.word_wrap = True
        tf_con.margin_left = tf_con.margin_top = tf_con.margin_right = tf_con.margin_bottom = 0

        for b_idx, (head, desc) in enumerate(m["contributions"]):
            bp = tf_con.paragraphs[0] if b_idx == 0 else tf_con.add_paragraph()
            r_h = bp.add_run()
            r_h.text = f"• {head}: "
            r_h.font.bold = True
            r_h.font.size = Pt(7.6)
            r_h.font.color.rgb = TEXT_DARK

            r_d = bp.add_run()
            r_d.text = desc
            r_d.font.size = Pt(7.4)
            r_d.font.color.rgb = TEXT_BODY
            bp.space_after = Pt(2.0)

        # 8. Challenge Callout Box (Native Rounded Rectangle)
        c_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cur_x + Inches(0.16), card_top + Inches(2.88), card_w - Inches(0.32), Inches(0.44))
        c_box.fill.solid()
        c_box.fill.fore_color.rgb = ROSE_LIGHT
        c_box.line.color.rgb = BORDER_ROSE
        c_box.line.width = Pt(0.8)
        tf_cb = c_box.text_frame
        tf_cb.word_wrap = True
        tf_cb.margin_left = Inches(0.08)
        tf_cb.margin_right = Inches(0.08)
        tf_cb.margin_top = Inches(0.04)
        p_cb = tf_cb.paragraphs[0]
        r_cbt = p_cb.add_run()
        r_cbt.text = "⚠️ Challenge: "
        r_cbt.font.bold = True
        r_cbt.font.size = Pt(7.4)
        r_cbt.font.color.rgb = ROSE_ACCENT
        r_cbtxt = p_cb.add_run()
        r_cbtxt.text = m["challenge"]
        r_cbtxt.font.size = Pt(7.2)
        r_cbtxt.font.color.rgb = RGBColor(159, 18, 57) # Rose 900

        # 9. Solution Callout Box (Native Rounded Rectangle)
        s_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cur_x + Inches(0.16), card_top + Inches(3.38), card_w - Inches(0.32), Inches(0.44))
        s_box.fill.solid()
        s_box.fill.fore_color.rgb = GREEN_LIGHT
        s_box.line.color.rgb = BORDER_GREEN
        s_box.line.width = Pt(0.8)
        tf_sb = s_box.text_frame
        tf_sb.word_wrap = True
        tf_sb.margin_left = Inches(0.08)
        tf_sb.margin_right = Inches(0.08)
        tf_sb.margin_top = Inches(0.04)
        p_sb = tf_sb.paragraphs[0]
        r_sbt = p_sb.add_run()
        r_sbt.text = "✅ Overcome: "
        r_sbt.font.bold = True
        r_sbt.font.size = Pt(7.4)
        r_sbt.font.color.rgb = GREEN_ACCENT
        r_sbtxt = p_sb.add_run()
        r_sbtxt.text = m["mitigation"]
        r_sbtxt.font.size = Pt(7.2)
        r_sbtxt.font.color.rgb = RGBColor(6, 95, 70) # Emerald 800

    # ------------------ 3. Section 2: Shared Hackathon Journey & Roadmap (100% Native Shapes) ------------------
    j_top = Inches(5.16)
    j_h = Inches(1.68)
    j_w = Inches(12.24)
    
    # Outer Journey Container Box
    j_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, start_x, j_top, j_w, j_h)
    j_box.fill.solid()
    j_box.fill.fore_color.rgb = CARD_BG
    j_box.line.color.rgb = BORDER_CARD
    j_box.line.width = Pt(1.2)

    # Journey Title & Tagline Textbox
    tb_jh = slide.shapes.add_textbox(start_x + Inches(0.20), j_top + Inches(0.08), j_w - Inches(0.40), Inches(0.35))
    tf_jh = tb_jh.text_frame
    tf_jh.margin_left = tf_jh.margin_top = tf_jh.margin_right = tf_jh.margin_bottom = 0

    p_jh1 = tf_jh.paragraphs[0]
    r_j1 = p_jh1.add_run()
    r_j1.text = "🚀 Our Hackathon Journey: \"Field Ground Truth Over AI Gimmicks\""
    r_j1.font.bold = True
    r_j1.font.size = Pt(11.5)
    r_j1.font.color.rgb = NAVY_PRIMARY

    r_jspace = p_jh1.add_run()
    r_jspace.text = "   |   "
    r_jspace.font.size = Pt(9.0)
    r_jspace.font.color.rgb = TEXT_MUTED

    r_j2 = p_jh1.add_run()
    r_j2.text = "Engineered for Punjab's 2-Acre Smallholders with End-to-End Test Verification"
    r_j2.font.bold = True
    r_j2.font.size = Pt(8.8)
    r_j2.font.color.rgb = PRIMARY_BLUE

    # 3 Phase Cards with Connecting Arrows (All Native Shapes!)
    step_w = Inches(3.52)
    step_h = Inches(1.08)
    step_y = j_top + Inches(0.48)
    arrow_w = Inches(0.38)
    arrow_gap = Inches(0.14)

    phases = [
        ("🌾 PHASE 1: FIELD EMPATHY", "Agronomic Ground Truth", "Focused on the real crunch: 10–15 days before wheat sowing. Researched PAU trials: 3.6t total vs 2.0t baler recoverable straw.", PRIMARY_BLUE, BLUE_LIGHT, BORDER_BLUE),
        ("⚙️ PHASE 2: ALGORITHMIC CO-DESIGN", "OR-Tools & Voice Loop", "Formulated CP-SAT spatial clustering in <2.0s; built vernacular speech intake with mandatory audio confirmation modal.", GREEN_ACCENT, GREEN_LIGHT, BORDER_GREEN),
        ("🌱 PHASE 3: PRODUCTION IMPACT", "Circular Green Wealth", "100% green tests (pytest 21/21 & flutter). Connecting farmers to SATAT Bio-CNG plants: turning smoke into ₹25k+ income.", PURPLE_ACCENT, PURPLE_LIGHT, BORDER_PURPLE)
    ]

    for p_idx, (p_tag, p_head, p_desc, p_accent, p_bg, p_border) in enumerate(phases):
        p_x = start_x + Inches(0.20) + p_idx * (step_w + arrow_w + 2 * arrow_gap)
        
        # Step Card Shape
        s_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, p_x, step_y, step_w, step_h)
        s_card.fill.solid()
        s_card.fill.fore_color.rgb = BG_CANVAS
        s_card.line.color.rgb = BORDER_CARD
        s_card.line.width = Pt(1.0)

        tb_sc = slide.shapes.add_textbox(p_x + Inches(0.12), step_y + Inches(0.06), step_w - Inches(0.24), step_h - Inches(0.12))
        tf_sc = tb_sc.text_frame
        tf_sc.word_wrap = True
        tf_sc.margin_left = tf_sc.margin_top = tf_sc.margin_right = tf_sc.margin_bottom = 0

        # Phase Badge
        p_sc1 = tf_sc.paragraphs[0]
        p_sc1.text = p_tag
        p_sc1.font.bold = True
        p_sc1.font.size = Pt(7.5)
        p_sc1.font.color.rgb = p_accent

        # Title
        p_sc2 = tf_sc.add_paragraph()
        p_sc2.text = p_head
        p_sc2.font.bold = True
        p_sc2.font.size = Pt(9.5)
        p_sc2.font.color.rgb = NAVY_HEADING
        p_sc2.space_before = Pt(1.0)
        p_sc2.space_after = Pt(1.5)

        # Description
        p_sc3 = tf_sc.add_paragraph()
        p_sc3.text = p_desc
        p_sc3.font.size = Pt(7.4)
        p_sc3.font.color.rgb = TEXT_BODY

        # Connecting Arrow (between cards)
        if p_idx < 2:
            arr_x = p_x + step_w + arrow_gap
            arr = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, arr_x, step_y + Inches(0.38), arrow_w, Inches(0.28))
            arr.fill.solid()
            arr.fill.fore_color.rgb = BORDER_CARD
            arr.line.fill.background()

    # ------------------ 4. Ground Truth Verification Bottom Strip ------------------
    verif_box = slide.shapes.add_textbox(Inches(0.55), Inches(6.92), Inches(12.24), Inches(0.24))
    tf_v = verif_box.text_frame
    tf_v.margin_left = tf_v.margin_top = tf_v.margin_right = tf_v.margin_bottom = 0
    p_v = tf_v.paragraphs[0]
    p_v.alignment = PP_ALIGN.CENTER

    r_vt = p_v.add_run()
    r_vt.text = "🔍 Ground Truth Standards:  "
    r_vt.font.bold = True
    r_vt.font.size = Pt(8.0)
    r_vt.font.color.rgb = NAVY_PRIMARY

    sources_list = [
        ("GitHub Repository (Rishabhbansal005/Parali-setu)", "https://github.com/Rishabhbansal005/Parali-setu"),
        ("Google OR-Tools CP-SAT (developers.google.com/optimization)", "https://developers.google.com/optimization"),
        ("ESA Copernicus Sentinel-2 (sentinels.copernicus.eu)", "https://sentinels.copernicus.eu"),
        ("MoPNG SATAT Scheme (mopng.gov.in)", "https://mopng.gov.in")
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

    # ------------------ 5. Footer ------------------
    footer_box = slide.shapes.add_textbox(Inches(0.55), Inches(7.18), Inches(12.24), Inches(0.22))
    tf_f = footer_box.text_frame
    tf_f.margin_left = tf_f.margin_top = tf_f.margin_right = tf_f.margin_bottom = 0
    p_f = tf_f.paragraphs[0]
    p_f.text = "@HSC submission- Template  |  ParaliSetu: Team Composition, Roles & Engineering Journey"
    p_f.font.size = Pt(8.5)
    p_f.font.color.rgb = TEXT_MUTED
    p_f.alignment = PP_ALIGN.CENTER

    # Save Presentation
    output_path = r"c:\Users\Rishabh Bansal\Downloads\Parali setu\Team_Slide.pptx"
    prs.save(output_path)
    print(f"Native Team PPTX saved successfully to {output_path}")

if __name__ == "__main__":
    build_native_team_slide()
