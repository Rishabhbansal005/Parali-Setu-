import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_team_slide():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    slide_layout = prs.slide_layouts[6] # blank layout
    slide = prs.slides.add_slide(slide_layout)

    # ------------------ Color Palette ------------------
    BG_CANVAS = RGBColor(248, 250, 252)       # Slate 50 clean background
    CARD_BG = RGBColor(255, 255, 255)         # Pure White
    NAVY_PRIMARY = RGBColor(30, 58, 138)      # Blue 900
    NAVY_HEADING = RGBColor(15, 23, 42)       # Slate 900
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
    BORDER_CARD = RGBColor(226, 232, 240)     # Slate 200
    ORANGE_BADGE = RGBColor(234, 88, 12)      # Orange 600

    # 0. Slide Background Canvas
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

    # 1.2 Title & Subtitle with Generous Line Height
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
    p_sub.text = "Three-Tier Architectural Ownership, Challenges Overcome & Hackathon Journey"
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

    # ------------------ 2. Section 1: Three Team Member Cards ------------------
    card_top = Inches(1.12)
    card_h = Inches(3.85)
    card_w = Inches(3.86)
    card_gap = Inches(0.33)
    start_x = Inches(0.55)

    team_members = [
        {
            "name": "Rishabh Bansal",
            "role": "Lead Architect & Optimization Engineer",
            "part": "PART 1: CORE BRAIN & OPTIMIZATION",
            "accent": PRIMARY_BLUE,
            "light_bg": BLUE_LIGHT,
            "border": BORDER_BLUE,
            "icon": "⚡",
            "contributions": [
                ("FastAPI & PostGIS Gateway", "12 normalized RLS tables, spatial indexing & JWT security on Supabase."),
                ("Google OR-Tools CP-SAT", "Solves NP-hard multi-sided matching (Farmer-Baler-Truck-Buyer) in < 2.0s."),
                ("PAU Agronomic Formula", "Empirical matrix distinguishing biological (~3.6t) from baler recovery (~2.0t).")
            ],
            "challenge": "Solving NP-hard multi-stop capacity within a 15-day crunch without timeouts.",
            "mitigation": "Engineered 25–40 acre contiguous farm clustering with radius relaxation."
        },
        {
            "name": "Ravi Singh",
            "role": "Mobile Systems & Vernacular AI",
            "part": "PART 2: FARMER APP & VERNACULAR AI",
            "accent": GREEN_ACCENT,
            "light_bg": GREEN_LIGHT,
            "border": BORDER_GREEN,
            "icon": "📱",
            "contributions": [
                ("Flutter Trilingual Client", "Trilingual app (Punjabi/Hindi/English) with 17.03 MB split APK budget."),
                ("Vernacular Voice Pipeline", "Bhashini/Whisper STT with Gemini 1.5 entity parser for natural speech intake."),
                ("Offline-First Field Resilience", "Local SQLite caching and 100% deterministic manual UI fallback.")
            ],
            "challenge": "Ambient tractor/combine acoustic noise causing vernacular speech errors.",
            "mitigation": "Enforced mandatory audio confirmation readback (*'Aapne bola: 4 Killa, Sahi hai?'*)."
        },
        {
            "name": "Vaibhav Yadav",
            "role": "Web Platforms & Satellite / Anti-Fraud",
            "part": "PART 3: WEB PLATFORMS & AUDIT",
            "accent": PURPLE_ACCENT,
            "light_bg": PURPLE_LIGHT,
            "border": BORDER_PURPLE,
            "icon": "🛰️",
            "contributions": [
                ("Next.js Industrial Portals", "Command dashboards for Biomass Buyers (demand setting & pre-funded escrow)."),
                ("Dharamkanta Scale OCR", "Weighbridge intake with automated OCR and mathematical sanity validation."),
                ("Sentinel-2 SWIR Satellite", "Remote ΔNBR spectral burn audit to auto-issue tamper-proof No-Burn certs.")
            ],
            "challenge": "Physically impossible village field visits & risk of paper slip tampering.",
            "mitigation": "Remote sensing burn audit + (|Gross - Tare - Net| <= 0.02t) OCR validation lock."
        }
    ]

    for i, m in enumerate(team_members):
        cur_x = start_x + i * (card_w + card_gap)
        
        # Outer Card Container with soft background
        m_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cur_x, card_top, card_w, card_h)
        m_card.fill.solid()
        m_card.fill.fore_color.rgb = CARD_BG
        m_card.line.color.rgb = m["border"]
        m_card.line.width = Pt(1.5)

        # Header Accent Strip inside card
        strip = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cur_x + Inches(0.12), card_top + Inches(0.10), card_w - Inches(0.24), Inches(0.70))
        strip.fill.solid()
        strip.fill.fore_color.rgb = m["light_bg"]
        strip.line.color.rgb = m["border"]
        strip.line.width = Pt(0.8)

        # Strip Text: Name + Role + Division
        tb_st = slide.shapes.add_textbox(cur_x + Inches(0.20), card_top + Inches(0.12), card_w - Inches(0.40), Inches(0.66))
        tf_st = tb_st.text_frame
        tf_st.word_wrap = True
        tf_st.margin_left = tf_st.margin_top = tf_st.margin_right = tf_st.margin_bottom = 0

        p_name = tf_st.paragraphs[0]
        p_name.text = f"{m['icon']} {m['name']}"
        p_name.font.bold = True
        p_name.font.size = Pt(13.5)
        p_name.font.color.rgb = NAVY_HEADING

        p_role = tf_st.add_paragraph()
        r_r = p_role.add_run()
        r_r.text = m["role"]
        r_r.font.bold = True
        r_r.font.size = Pt(8.5)
        r_r.font.color.rgb = m["accent"]

        r_div = p_role.add_run()
        r_div.text = f"  [{m['part']}]"
        r_div.font.bold = True
        r_div.font.size = Pt(7.5)
        r_div.font.color.rgb = TEXT_MUTED

        # Inner Content Textbox below strip
        tb_m = slide.shapes.add_textbox(cur_x + Inches(0.20), card_top + Inches(0.88), card_w - Inches(0.40), card_h - Inches(0.96))
        tf_m = tb_m.text_frame
        tf_m.word_wrap = True
        tf_m.margin_left = tf_m.margin_top = tf_m.margin_right = tf_m.margin_bottom = 0

        # Section: Core Roles & Contributions
        p_chdr = tf_m.paragraphs[0]
        p_chdr.text = "🎯 Core Engineering Ownership:"
        p_chdr.font.bold = True
        p_chdr.font.size = Pt(8.8)
        p_chdr.font.color.rgb = NAVY_HEADING
        p_chdr.space_after = Pt(2.0)

        for head, desc in m["contributions"]:
            p_c = tf_m.add_paragraph()
            r_ch = p_c.add_run()
            r_ch.text = f"• {head}: "
            r_ch.font.bold = True
            r_ch.font.size = Pt(8.2)
            r_ch.font.color.rgb = TEXT_DARK

            r_cd = p_c.add_run()
            r_cd.text = desc
            r_cd.font.size = Pt(8.0)
            r_cd.font.color.rgb = TEXT_BODY
            p_c.space_after = Pt(2.5)

        # Section: Specific Challenge Overcome
        p_chal = tf_m.add_paragraph()
        r_ch_tag = p_chal.add_run()
        r_ch_tag.text = "⚠️ Key Challenge: "
        r_ch_tag.font.bold = True
        r_ch_tag.font.size = Pt(8.2)
        r_ch_tag.font.color.rgb = ROSE_ACCENT
        r_ch_txt = p_chal.add_run()
        r_ch_txt.text = m["challenge"]
        r_ch_txt.font.size = Pt(7.8)
        r_ch_txt.font.color.rgb = TEXT_BODY
        p_chal.space_before = Pt(3.0)
        p_chal.space_after = Pt(2.0)

        # Section: Strategy & Solution
        p_sol = tf_m.add_paragraph()
        r_sol_tag = p_sol.add_run()
        r_sol_tag.text = "✅ Overcome Via: "
        r_sol_tag.font.bold = True
        r_sol_tag.font.size = Pt(8.2)
        r_sol_tag.font.color.rgb = GREEN_ACCENT
        r_sol_txt = p_sol.add_run()
        r_sol_txt.text = m["mitigation"]
        r_sol_txt.font.size = Pt(7.8)
        r_sol_txt.font.color.rgb = TEXT_BODY

    # ------------------ 3. Section 2: Shared Hackathon Journey & Philosophy ------------------
    j_top = Inches(5.08)
    j_h = Inches(1.72)
    j_w = Inches(12.24)
    j_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, start_x, j_top, j_w, j_h)
    j_box.fill.solid()
    j_box.fill.fore_color.rgb = CARD_BG
    j_box.line.color.rgb = BORDER_CARD
    j_box.line.width = Pt(1.2)

    tb_j = slide.shapes.add_textbox(start_x + Inches(0.24), j_top + Inches(0.12), j_w - Inches(0.48), j_h - Inches(0.24))
    tf_j = tb_j.text_frame
    tf_j.word_wrap = True
    tf_j.margin_left = tf_j.margin_top = tf_j.margin_right = tf_j.margin_bottom = 0

    p_j1 = tf_j.paragraphs[0]
    p_j1.text = "🚀 Our Team Journey & Core Philosophy: \"Field Ground Truth Over AI Gimmicks\""
    p_j1.font.bold = True
    p_j1.font.size = Pt(12.0)
    p_j1.font.color.rgb = NAVY_PRIMARY

    p_j2 = tf_j.add_paragraph()
    p_j2.text = "Engineering a Pragmatic Multi-Sided Marketplace for North India's 2-Acre Smallholders"
    p_j2.font.bold = True
    p_j2.font.size = Pt(8.8)
    p_j2.font.color.rgb = PRIMARY_BLUE
    p_j2.space_after = Pt(4.0)

    # 3 Journey Highlights
    j_pillars = [
        ("🌾 Field-First Empathy", "Focused on the real crunch: 10–15 days before wheat sowing. Designed for low-literacy farmers with voice intake, zero complex submenus, and guaranteed weighbridge escrow cash payout."),
        ("🔬 Anti-Hallucination Guardrails", "Enforced 100% green test suites (pytest 21/21 backend & flutter test mobile). All stubble yields calculated deterministically using PAU formulas—never LLM invented numbers."),
        ("🌱 Circular Economy Impact", "Built to divert 20 MMT straw into clean SATAT Bio-CNG plants, transforming a $19B health crisis into ₹25,000+ seasonal wealth per 5-acre farming family.")
    ]

    for p_head, p_desc in j_pillars:
        p_jp = tf_j.add_paragraph()
        r_jh = p_jp.add_run()
        r_jh.text = f"• {p_head}: "
        r_jh.font.bold = True
        r_jh.font.size = Pt(8.5)
        r_jh.font.color.rgb = NAVY_HEADING

        r_jd = p_jp.add_run()
        r_jd.text = p_desc
        r_jd.font.size = Pt(8.2)
        r_jd.font.color.rgb = TEXT_BODY
        p_jp.space_after = Pt(2.5)

    # ------------------ 4. Ground Truth Verification Bottom Strip ------------------
    verif_box = slide.shapes.add_textbox(Inches(0.55), Inches(6.92), Inches(12.24), Inches(0.24))
    tf_v = verif_box.text_frame
    tf_v.margin_left = tf_v.margin_top = tf_v.margin_right = tf_v.margin_bottom = 0
    p_v = tf_v.paragraphs[0]
    p_v.alignment = PP_ALIGN.CENTER

    r_vt = p_v.add_run()
    r_vt.text = "🔍 Codebase Verification & Ground Truth:  "
    r_vt.font.bold = True
    r_vt.font.size = Pt(8.2)
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
            r_sep.font.size = Pt(8.0)
            r_sep.font.color.rgb = TEXT_MUTED

        r_s = p_v.add_run()
        r_s.text = s_name
        r_s.font.size = Pt(8.0)
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
    print(f"Polished Team slide saved successfully to {output_path}")

if __name__ == "__main__":
    build_team_slide()
