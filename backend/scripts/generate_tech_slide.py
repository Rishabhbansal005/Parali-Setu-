import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_tech_approach_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    # -------------------------------------------------------------
    # 1. COLOR PALETTE (Clean, modern tech aesthetic)
    # -------------------------------------------------------------
    BG_CANVAS        = RGBColor(250, 252, 255)  # #FAFCFF soft canvas
    CARD_BG          = RGBColor(255, 255, 255)  # Pure White
    CARD_BORDER      = RGBColor(226, 232, 240)  # Slate-200
    TEXT_TITLE       = RGBColor(15, 23, 42)     # Slate-900 (#0F172A)
    TEXT_BODY        = RGBColor(51, 65, 85)     # Slate-700 (#334155)
    TEXT_MUTED       = RGBColor(100, 116, 139)  # Slate-500 (#64748B)

    # Accent Colors
    BLUE_HEADER      = RGBColor(30, 58, 138)    # Blue-900
    BLUE_ACCENT      = RGBColor(37, 99, 235)    # Blue-600
    BLUE_BG          = RGBColor(239, 246, 255)  # Blue-50
    BLUE_BORDER      = RGBColor(191, 219, 254)  # Blue-200

    GREEN_ACCENT     = RGBColor(5, 150, 105)    # Emerald-600
    GREEN_BG         = RGBColor(236, 253, 245)  # Emerald-50
    GREEN_BORDER     = RGBColor(167, 243, 208)  # Emerald-200

    PURPLE_ACCENT    = RGBColor(126, 34, 206)   # Purple-700
    PURPLE_BG        = RGBColor(250, 245, 255)  # Purple-50
    PURPLE_BORDER    = RGBColor(233, 213, 255)  # Purple-200

    AMBER_ACCENT     = RGBColor(180, 83, 9)     # Amber-700
    AMBER_BG         = RGBColor(254, 243, 199)  # Amber-100
    AMBER_BORDER     = RGBColor(253, 230, 138)  # Amber-200

    RED_ACCENT       = RGBColor(225, 29, 72)    # Rose-600
    RED_BG           = RGBColor(255, 241, 242)  # Rose-50

    # Background Canvas
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG_CANVAS
    bg.line.fill.background()

    # -------------------------------------------------------------
    # 2. TOP HEADER SECTION
    # -------------------------------------------------------------
    # Left Oval "Mist" Badge
    mist_badge = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.8), Inches(0.35), Inches(1.3), Inches(0.52))
    mist_badge.fill.solid()
    mist_badge.fill.fore_color.rgb = RGBColor(254, 215, 170)
    mist_badge.line.color.rgb = RGBColor(249, 115, 22)
    mist_badge.line.width = Pt(1.5)
    tf_m = mist_badge.text_frame
    tf_m.vertical_anchor = MSO_ANCHOR.MIDDLE
    p_m = tf_m.paragraphs[0]
    p_m.text = "Mist"
    p_m.font.name = "Segoe UI"
    p_m.font.size = Pt(13)
    p_m.font.bold = True
    p_m.font.color.rgb = RGBColor(154, 52, 18)
    p_m.alignment = PP_ALIGN.CENTER

    # Title & Subtitle
    title_box = slide.shapes.add_textbox(Inches(2.35), Inches(0.25), Inches(7.8), Inches(0.85))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = "Technical Approach"
    p_t.font.name = "Segoe UI"
    p_t.font.size = Pt(26)
    p_t.font.bold = True
    p_t.font.color.rgb = BLUE_HEADER

    p_sub = tf_t.add_paragraph()
    p_sub.text = "Architecture, Production Technology Stack, Implementation Flow & AI Integration"
    p_sub.font.name = "Segoe UI"
    p_sub.font.size = Pt(11.5)
    p_sub.font.bold = True
    p_sub.font.color.rgb = TEXT_MUTED

    # Top-Right Badge
    hsc_pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.6), Inches(0.35), Inches(2.0), Inches(0.48))
    hsc_pill.fill.solid()
    hsc_pill.fill.fore_color.rgb = CARD_BG
    hsc_pill.line.color.rgb = CARD_BORDER
    hsc_pill.line.width = Pt(1)
    tf_hsc = hsc_pill.text_frame
    tf_hsc.vertical_anchor = MSO_ANCHOR.MIDDLE
    p_hsc = tf_hsc.paragraphs[0]
    p_hsc.text = "Hack for Social Cause"
    p_hsc.font.name = "Segoe UI"
    p_hsc.font.size = Pt(10.5)
    p_hsc.font.bold = True
    p_hsc.font.color.rgb = TEXT_TITLE
    p_hsc.alignment = PP_ALIGN.CENTER

    # -------------------------------------------------------------
    # 3. 3-COLUMN MODULAR CARD LAYOUT (Height: 5.65 in)
    # -------------------------------------------------------------
    cards_y = Inches(1.25)
    cards_h = Inches(5.65)

    # =============================================================
    # COLUMN 1: TECH STACK & ARCHITECTURE (Width: 3.70 in)
    # =============================================================
    c1_x = Inches(0.70)
    c1_w = Inches(3.70)

    card1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c1_x, cards_y, c1_w, cards_h)
    card1.fill.solid()
    card1.fill.fore_color.rgb = CARD_BG
    card1.line.color.rgb = CARD_BORDER
    card1.line.width = Pt(1)

    # Ribbon
    h1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c1_x, cards_y, c1_w, Inches(0.52))
    h1.fill.solid()
    h1.fill.fore_color.rgb = BLUE_BG
    h1.line.fill.background()
    tf_h1 = h1.text_frame
    tf_h1.vertical_anchor = MSO_ANCHOR.MIDDLE
    p_h1 = tf_h1.paragraphs[0]
    p_h1.text = "🛠️  Production Technology Stack"
    p_h1.font.name = "Segoe UI"
    p_h1.font.size = Pt(13)
    p_h1.font.bold = True
    p_h1.font.color.rgb = BLUE_ACCENT

    # 4 Clean Tech Stack Chips
    stack_items = [
        ("Mobile App", "Flutter 3.13 (Dart)", "Trilingual (EN/HI/PA), offline Noto fonts, secure storage"),
        ("Backend Gateway", "FastAPI (Python 3.12)", "Asynchronous ASGI, 19 REST endpoints, PyJWT auth"),
        ("Operations Web", "Next.js 15 (React 19)", "TypeScript, Turbopack, Tailwind CSS, Web Speech API"),
        ("Spatial Database", "PostgreSQL + PostGIS", "12 normalized tables, PostGIS GIS spatial indexing, RLS")
    ]
    curr_y1 = cards_y + Inches(0.66)
    for layer, tech, note in stack_items:
        chip = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c1_x + Inches(0.18), curr_y1, c1_w - Inches(0.36), Inches(0.68))
        chip.fill.solid()
        chip.fill.fore_color.rgb = RGBColor(248, 250, 252)
        chip.line.color.rgb = CARD_BORDER
        chip.line.width = Pt(1)
        tf_c = chip.text_frame
        tf_c.word_wrap = True
        tf_c.margin_left = Inches(0.12)
        tf_c.margin_top = Inches(0.06)
        p_c1 = tf_c.paragraphs[0]
        p_c1.text = f"{layer}  ·  {tech}"
        p_c1.font.name = "Segoe UI"
        p_c1.font.size = Pt(10.5)
        p_c1.font.bold = True
        p_c1.font.color.rgb = TEXT_TITLE
        p_c2 = tf_c.add_paragraph()
        p_c2.text = note
        p_c2.font.name = "Segoe UI"
        p_c2.font.size = Pt(8.5)
        p_c2.font.color.rgb = TEXT_MUTED
        curr_y1 += Inches(0.76)

    # Sub-header: System Architecture Highlights
    tb_arch = slide.shapes.add_textbox(c1_x + Inches(0.18), curr_y1 + Inches(0.06), c1_w - Inches(0.36), Inches(1.8))
    tf_ar = tb_arch.text_frame
    tf_ar.word_wrap = True
    tf_ar.margin_left = 0
    tf_ar.margin_right = 0
    p_at = tf_ar.paragraphs[0]
    p_at.text = "Architecture Highlights:"
    p_at.font.name = "Segoe UI"
    p_at.font.size = Pt(11)
    p_at.font.bold = True
    p_at.font.color.rgb = TEXT_TITLE
    p_at.space_after = Pt(6)

    arch_points = [
        ("Decoupled Micro-Tier", "Mobile, Web, and FastAPI services communicate via REST & JWT tokens."),
        ("PostGIS Geofencing", "Spatial queries cluster nearby farm parcels within a 25 km baler radius."),
        ("Enterprise Security", "Hardware keystore encryption on device; Row-Level Security (RLS) in DB.")
    ]
    for a_t, a_d in arch_points:
        p_ap = tf_ar.add_paragraph()
        p_ap.text = f"✔ {a_t}: "
        p_ap.font.name = "Segoe UI"
        p_ap.font.size = Pt(9.2)
        p_ap.font.bold = True
        p_ap.font.color.rgb = BLUE_ACCENT
        run = p_ap.add_run()
        run.text = a_d
        run.font.name = "Segoe UI"
        run.font.size = Pt(8.6)
        run.font.bold = False
        run.font.color.rgb = TEXT_MUTED
        p_ap.space_after = Pt(6)

    # =============================================================
    # COLUMN 2: METHODOLOGY & PROCESS FLOW (Width: 4.30 in)
    # =============================================================
    c2_x = Inches(4.55)
    c2_w = Inches(4.30)

    card2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c2_x, cards_y, c2_w, cards_h)
    card2.fill.solid()
    card2.fill.fore_color.rgb = CARD_BG
    card2.line.color.rgb = GREEN_ACCENT
    card2.line.width = Pt(1.5)

    h2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c2_x, cards_y, c2_w, Inches(0.52))
    h2.fill.solid()
    h2.fill.fore_color.rgb = GREEN_BG
    h2.line.fill.background()
    tf_h2 = h2.text_frame
    tf_h2.vertical_anchor = MSO_ANCHOR.MIDDLE
    p_h2 = tf_h2.paragraphs[0]
    p_h2.text = "🔄  Implementation Flow & Methodology"
    p_h2.font.name = "Segoe UI"
    p_h2.font.size = Pt(13)
    p_h2.font.bold = True
    p_h2.font.color.rgb = GREEN_ACCENT

    # 4-Stage Architectural Pipeline
    flow_steps = [
        ("Phase 1: Vernacular Ingestion", "Speech-to-Text captures spoken Punjabi/Hindi; NLP extracts acres, variety, and harvest date with confirmation UI.", GREEN_BG, GREEN_ACCENT),
        ("Phase 2: Combinatorial Matching", "Google OR-Tools CP-SAT solver optimizes 4-sided assignment (Farmer ↔ Baler ↔ Truck ↔ Buyer) under time & capacity limits.", BLUE_BG, BLUE_ACCENT),
        ("Phase 3: Scale Gate & Escrow Settlement", "Rural Dharamkanta weighbridge logs certified gross & tare slips; pre-funded buyer escrow releases instant cash.", GREEN_BG, GREEN_ACCENT),
        ("Phase 4: Satellite Spectral Audit", "Copernicus Sentinel-2 dNBR index compares pre vs post harvest SWIR bands (<0.15 threshold) to issue No-Burn Certificate.", AMBER_BG, AMBER_ACCENT)
    ]
    curr_y2 = cards_y + Inches(0.66)
    for idx, (p_title, p_desc, p_bg, p_col) in enumerate(flow_steps):
        f_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c2_x + Inches(0.18), curr_y2, c2_w - Inches(0.36), Inches(0.88))
        f_card.fill.solid()
        f_card.fill.fore_color.rgb = p_bg
        f_card.line.color.rgb = CARD_BORDER
        f_card.line.width = Pt(1)

        tf_f = f_card.text_frame
        tf_f.word_wrap = True
        tf_f.margin_left = Inches(0.15)
        tf_f.margin_top = Inches(0.08)
        p_ft = tf_f.paragraphs[0]
        p_ft.text = p_title
        p_ft.font.name = "Segoe UI"
        p_ft.font.size = Pt(10.5)
        p_ft.font.bold = True
        p_ft.font.color.rgb = p_col

        p_fd = tf_f.add_paragraph()
        p_fd.text = p_desc
        p_fd.font.name = "Segoe UI"
        p_fd.font.size = Pt(8.5)
        p_fd.font.color.rgb = TEXT_BODY

        if idx < 3:
            arrow = slide.shapes.add_shape(MSO_SHAPE.DOWN_ARROW, c2_x + (c2_w / 2) - Inches(0.07), curr_y2 + Inches(0.88), Inches(0.14), Inches(0.11))
            arrow.fill.solid()
            arrow.fill.fore_color.rgb = RGBColor(203, 213, 225)
            arrow.line.fill.background()

        curr_y2 += Inches(1.00)

    # Methodology Badge (Quality & TDD)
    tdd_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c2_x + Inches(0.18), curr_y2 + Inches(0.06), c2_w - Inches(0.36), Inches(0.68))
    tdd_box.fill.solid()
    tdd_box.fill.fore_color.rgb = RGBColor(248, 250, 252)
    tdd_box.line.color.rgb = CARD_BORDER
    tdd_box.line.width = Pt(1)
    tf_td = tdd_box.text_frame
    tf_td.word_wrap = True
    tf_td.margin_left = Inches(0.15)
    tf_td.margin_top = Inches(0.06)
    p_t1 = tf_td.paragraphs[0]
    p_t1.text = "🧪 Quality Assurance: 100% Green Test Coverage"
    p_t1.font.name = "Segoe UI"
    p_t1.font.size = Pt(9.8)
    p_t1.font.bold = True
    p_t1.font.color.rgb = GREEN_ACCENT
    p_t2 = tf_td.add_paragraph()
    p_t2.text = "35/35 backend pytest tests passed · 20/20 mobile flutter widget tests passed · 0 lint errors."
    p_t2.font.name = "Segoe UI"
    p_t2.font.size = Pt(8.3)
    p_t2.font.color.rgb = TEXT_MUTED

    # =============================================================
    # COLUMN 3: AI USAGE & DELIVERABLE LINKS (Width: 3.70 in)
    # =============================================================
    c3_x = Inches(9.00)
    c3_w = Inches(3.70)

    card3 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c3_x, cards_y, c3_w, cards_h)
    card3.fill.solid()
    card3.fill.fore_color.rgb = CARD_BG
    card3.line.color.rgb = CARD_BORDER
    card3.line.width = Pt(1)

    # Ribbon
    h3 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c3_x, cards_y, c3_w, Inches(0.52))
    h3.fill.solid()
    h3.fill.fore_color.rgb = PURPLE_BG
    h3.line.fill.background()
    tf_h3 = h3.text_frame
    tf_h3.vertical_anchor = MSO_ANCHOR.MIDDLE
    p_h3 = tf_h3.paragraphs[0]
    p_h3.text = "🤖  Extent of AI Usage & Deliverables"
    p_h3.font.name = "Segoe UI"
    p_h3.font.size = Pt(13)
    p_h3.font.bold = True
    p_h3.font.color.rgb = PURPLE_ACCENT

    # AI Usage Points
    tb_ai = slide.shapes.add_textbox(c3_x + Inches(0.18), cards_y + Inches(0.60), c3_w - Inches(0.36), Inches(2.6))
    tf_ai = tb_ai.text_frame
    tf_ai.word_wrap = True
    tf_ai.margin_left = 0
    tf_ai.margin_right = 0
    p_ait = tf_ai.paragraphs[0]
    p_ait.text = "AI Engines & Tools Integrated:"
    p_ait.font.name = "Segoe UI"
    p_ait.font.size = Pt(11)
    p_ait.font.bold = True
    p_ait.font.color.rgb = TEXT_TITLE
    p_ait.space_after = Pt(6)

    ai_tools = [
        ("Google OR-Tools CP-SAT", "Constraint solver optimization engine solving multi-objective farmer-baler-truck routing."),
        ("Sentinel-2 Spectral Engine", "Automated dNBR formula calculation verifying zero burn scars on field parcels."),
        ("Vernacular Voice NLP", "Extracts Punjabi Gurmukhi & Hindi crop numbers into structured JSON entities."),
        ("AI Co-Pilot Engineering", "Claude 4.6 & Gemini 3.8 via Google Antigravity IDE for architecture, tests & localization.")
    ]
    for ai_name, ai_role in ai_tools:
        p_ai = tf_ai.add_paragraph()
        p_ai.text = f"★ {ai_name}: "
        p_ai.font.name = "Segoe UI"
        p_ai.font.size = Pt(9.2)
        p_ai.font.bold = True
        p_ai.font.color.rgb = PURPLE_ACCENT
        run = p_ai.add_run()
        run.text = ai_role
        run.font.name = "Segoe UI"
        run.font.size = Pt(8.4)
        run.font.bold = False
        run.font.color.rgb = TEXT_MUTED
        p_ai.space_after = Pt(5)

    # -------------------------------------------------------------
    # TWO DEDICATED ACTION BOXES (GitHub & Demo Video) - User Request!
    # -------------------------------------------------------------
    box_y = cards_y + Inches(3.40)

    # 1. GITHUB REPOSITORY BOX
    gh_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c3_x + Inches(0.18), box_y, c3_w - Inches(0.36), Inches(0.96))
    gh_box.fill.solid()
    gh_box.fill.fore_color.rgb = RGBColor(241, 245, 249) # slate-100
    gh_box.line.color.rgb = RGBColor(148, 163, 184)       # slate-400
    gh_box.line.width = Pt(1.5)
    tf_gh = gh_box.text_frame
    tf_gh.word_wrap = True
    tf_gh.margin_left = Inches(0.14)
    tf_gh.margin_top = Inches(0.08)
    p_gh1 = tf_gh.paragraphs[0]
    p_gh1.text = "🐙  GitHub Repository (Source Code)"
    p_gh1.font.name = "Segoe UI"
    p_gh1.font.size = Pt(10.5)
    p_gh1.font.bold = True
    p_gh1.font.color.rgb = TEXT_TITLE

    p_gh2 = tf_gh.add_paragraph()
    p_gh2.text = "github.com/Rishabhbansal005/Parali-setu"
    p_gh2.font.name = "Segoe UI"
    p_gh2.font.size = Pt(9.2)
    p_gh2.font.bold = True
    p_gh2.font.color.rgb = BLUE_ACCENT

    p_gh3 = tf_gh.add_paragraph()
    p_gh3.text = "100% Green test suites · MIT License · Complete API docs"
    p_gh3.font.name = "Segoe UI"
    p_gh3.font.size = Pt(7.8)
    p_gh3.font.color.rgb = TEXT_MUTED

    # 2. WORKING DEMO VIDEO BOX
    vid_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c3_x + Inches(0.18), box_y + Inches(1.08), c3_w - Inches(0.36), Inches(0.96))
    vid_box.fill.solid()
    vid_box.fill.fore_color.rgb = RGBColor(254, 242, 242) # rose-50
    vid_box.line.color.rgb = RGBColor(251, 113, 133)      # rose-400
    vid_box.line.width = Pt(1.5)
    tf_vd = vid_box.text_frame
    tf_vd.word_wrap = True
    tf_vd.margin_left = Inches(0.14)
    tf_vd.margin_top = Inches(0.08)
    p_vd1 = tf_vd.paragraphs[0]
    p_vd1.text = "🎬  Working Prototype Demo Video"
    p_vd1.font.name = "Segoe UI"
    p_vd1.font.size = Pt(10.5)
    p_vd1.font.bold = True
    p_vd1.font.color.rgb = RED_ACCENT

    p_vd2 = tf_vd.add_paragraph()
    p_vd2.text = "[ Paste Video Link / YouTube / Drive URL Here ]"
    p_vd2.font.name = "Segoe UI"
    p_vd2.font.size = Pt(9.2)
    p_vd2.font.bold = True
    p_vd2.font.color.rgb = RED_ACCENT

    p_vd3 = tf_vd.add_paragraph()
    p_vd3.text = "End-to-End Walkthrough: Voice Intake ➔ Escrow ➔ Satellite Audit"
    p_vd3.font.name = "Segoe UI"
    p_vd3.font.size = Pt(7.8)
    p_vd3.font.color.rgb = TEXT_MUTED

    # -------------------------------------------------------------
    # 4. FOOTER
    # -------------------------------------------------------------
    footer = slide.shapes.add_textbox(Inches(0.7), Inches(7.05), Inches(12.0), Inches(0.30))
    tf_f = footer.text_frame
    p_f = tf_f.paragraphs[0]
    p_f.text = "@HSC submission- Template  |  ParaliSetu: Technical Architecture & Methodology"
    p_f.font.name = "Segoe UI"
    p_f.font.size = Pt(9)
    p_f.font.color.rgb = TEXT_MUTED
    p_f.alignment = PP_ALIGN.CENTER

    out_path = r"C:\Users\Rishabh Bansal\Downloads\Parali setu\Technical_Approach_Slide.pptx"
    prs.save(out_path)
    print(f"Technical Approach slide generated successfully: {out_path}")

if __name__ == "__main__":
    create_tech_approach_deck()
