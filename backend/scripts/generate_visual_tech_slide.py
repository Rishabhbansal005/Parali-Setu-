import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    slide_layout = prs.slide_layouts[6] # blank layout
    slide = prs.slides.add_slide(slide_layout)

    # ------------------ Color Palette ------------------
    BG_COLOR = RGBColor(248, 250, 252)       # Slate 50
    CARD_BG = RGBColor(255, 255, 255)        # Pure White
    NAVY_TITLE = RGBColor(30, 58, 138)       # Blue 900
    TEXT_DARK = RGBColor(15, 23, 42)         # Slate 900
    TEXT_MUTED = RGBColor(100, 116, 139)     # Slate 500
    PRIMARY_BLUE = RGBColor(37, 99, 235)     # Blue 600
    BORDER_LIGHT = RGBColor(226, 232, 240)   # Slate 200
    BORDER_ACCENT = RGBColor(191, 219, 254)  # Blue 200
    ORANGE_BADGE = RGBColor(234, 88, 12)     # Orange 600
    GREEN_ACCENT = RGBColor(5, 150, 105)     # Emerald 600
    PURPLE_ACCENT = RGBColor(124, 58, 237)   # Purple 600
    ROSE_ACCENT = RGBColor(225, 29, 72)      # Rose 600

    # 0. Slide Background
    bg_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg_shape.fill.solid()
    bg_shape.fill.fore_color.rgb = BG_COLOR
    bg_shape.line.fill.background()

    # ------------------ 1. Header Elements ------------------
    # 1.1 "Mist" Badge
    badge_left, badge_top, badge_w, badge_h = Inches(0.55), Inches(0.35), Inches(1.25), Inches(0.65)
    badge = slide.shapes.add_shape(MSO_SHAPE.OVAL, badge_left, badge_top, badge_w, badge_h)
    badge.fill.solid()
    badge.fill.fore_color.rgb = RGBColor(254, 215, 170)
    badge.line.color.rgb = ORANGE_BADGE
    badge.line.width = Pt(1.5)
    tf = badge.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Mist"
    p.font.bold = True
    p.font.size = Pt(17)
    p.font.color.rgb = RGBColor(154, 52, 18)
    p.alignment = PP_ALIGN.CENTER

    # 1.2 Title & Subtitle
    title_box = slide.shapes.add_textbox(Inches(1.95), Inches(0.30), Inches(8.40), Inches(0.85))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0

    p_t = tf_t.paragraphs[0]
    p_t.text = "Technical Approach"
    p_t.font.bold = True
    p_t.font.size = Pt(27)
    p_t.font.color.rgb = NAVY_TITLE

    p_sub = tf_t.add_paragraph()
    p_sub.text = "Interactive Architecture & Flowchart (xyflow Engine), Production Stack Rationale & Deliverables"
    p_sub.font.size = Pt(11.5)
    p_sub.font.color.rgb = TEXT_MUTED

    # 1.3 Hack for Social Cause Badge
    hack_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.55), Inches(0.35), Inches(2.25), Inches(0.65))
    hack_box.fill.solid()
    hack_box.fill.fore_color.rgb = CARD_BG
    hack_box.line.color.rgb = BORDER_LIGHT
    hack_box.line.width = Pt(1.5)
    tf_h = hack_box.text_frame
    p_h = tf_h.paragraphs[0]
    p_h.text = "Hack for Social Cause"
    p_h.font.bold = True
    p_h.font.size = Pt(11.5)
    p_h.font.color.rgb = TEXT_DARK
    p_h.alignment = PP_ALIGN.CENTER

    # ------------------ 2. Top Hero: xyflow Architecture Flowchart ------------------
    hero_l, hero_t, hero_w, hero_h = Inches(0.55), Inches(1.22), Inches(12.25), Inches(3.04)
    hero_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, hero_l, hero_t, hero_w, hero_h)
    hero_card.fill.solid()
    hero_card.fill.fore_color.rgb = CARD_BG
    hero_card.line.color.rgb = BORDER_ACCENT
    hero_card.line.width = Pt(1.2)

    # Hero Header inside container
    hh_box = slide.shapes.add_textbox(Inches(0.75), Inches(1.30), Inches(8.80), Inches(0.30))
    tf_hh = hh_box.text_frame
    tf_hh.word_wrap = True
    tf_hh.margin_left = tf_hh.margin_top = tf_hh.margin_right = tf_hh.margin_bottom = 0
    p_hh = tf_hh.paragraphs[0]
    p_hh.text = "🌐 End-to-End System Architecture & Operational Pipeline Flowchart"
    p_hh.font.bold = True
    p_hh.font.size = Pt(12.5)
    p_hh.font.color.rgb = NAVY_TITLE

    # Small xyflow engine badge on top right of hero container
    arch_badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.85), Inches(1.28), Inches(2.75), Inches(0.28))
    arch_badge.fill.solid()
    arch_badge.fill.fore_color.rgb = RGBColor(239, 246, 255) # Blue 50
    arch_badge.line.color.rgb = RGBColor(191, 219, 254)
    arch_badge.line.width = Pt(1.0)
    tf_ab = arch_badge.text_frame
    p_ab = tf_ab.paragraphs[0]
    p_ab.text = "⚡ Built with xyflow / react-flow"
    p_ab.font.bold = True
    p_ab.font.size = Pt(9.5)
    p_ab.font.color.rgb = PRIMARY_BLUE
    p_ab.alignment = PP_ALIGN.CENTER

    # Clean frame container for the xyflow diagram
    flow_frame_l, flow_frame_t, flow_frame_w, flow_frame_h = Inches(0.70), Inches(1.64), Inches(7.55), Inches(2.50)
    flow_frame = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, flow_frame_l, flow_frame_t, flow_frame_w, flow_frame_h)
    flow_frame.fill.solid()
    flow_frame.fill.fore_color.rgb = RGBColor(248, 250, 252) # Slate 50 dot canvas
    flow_frame.line.color.rgb = BORDER_LIGHT
    flow_frame.line.width = Pt(1.0)

    # Insert Crisp Zero-Overlap xyflow Diagram
    xyflow_img_path = r"c:\Users\Rishabh Bansal\Downloads\Parali setu\docs\diagrams\xyflow_arch_shot.png"
    if os.path.exists(xyflow_img_path):
        slide.shapes.add_picture(xyflow_img_path, Inches(0.72), Inches(1.66), Inches(7.51), Inches(2.46))

    # Right Side of Hero: Real UI Artifacts Panel
    ui_panel_l, ui_panel_t, ui_panel_w, ui_panel_h = Inches(8.40), Inches(1.64), Inches(4.25), Inches(2.50)
    ui_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, ui_panel_l, ui_panel_t, ui_panel_w, ui_panel_h)
    ui_card.fill.solid()
    ui_card.fill.fore_color.rgb = RGBColor(248, 250, 252) # Slate 50
    ui_card.line.color.rgb = BORDER_LIGHT
    ui_card.line.width = Pt(1.0)

    # UI Panel Title
    ui_title_box = slide.shapes.add_textbox(Inches(8.55), Inches(1.72), Inches(3.95), Inches(0.24))
    tf_ut = ui_title_box.text_frame
    tf_ut.margin_left = tf_ut.margin_top = tf_ut.margin_right = tf_ut.margin_bottom = 0
    p_ut = tf_ut.paragraphs[0]
    p_ut.text = "📱 Live Application Interfaces (Field Verified)"
    p_ut.font.bold = True
    p_ut.font.size = Pt(10.5)
    p_ut.font.color.rgb = TEXT_DARK

    # Mobile App Thumbnail (scaled down cleanly so label NEVER collides)
    mob_img_path = r"c:\Users\Rishabh Bansal\Downloads\Parali setu\docs\diagrams\thumb_mobile.png"
    if os.path.exists(mob_img_path):
        slide.shapes.add_picture(mob_img_path, Inches(8.55), Inches(2.00), Inches(0.88), Inches(1.62))
        
        # Label below mobile
        lbl_box = slide.shapes.add_textbox(Inches(8.45), Inches(3.68), Inches(1.08), Inches(0.38))
        tf_lbl = lbl_box.text_frame
        tf_lbl.word_wrap = True
        tf_lbl.margin_left = tf_lbl.margin_top = tf_lbl.margin_right = tf_lbl.margin_bottom = 0
        p_l = tf_lbl.paragraphs[0]
        p_l.text = "Farmer Voice UI\n(hi-IN / pa-IN)"
        p_l.font.size = Pt(7.5)
        p_l.font.bold = True
        p_l.font.color.rgb = PRIMARY_BLUE
        p_l.alignment = PP_ALIGN.CENTER

    # Scale Terminal Thumbnail
    scale_img_path = r"c:\Users\Rishabh Bansal\Downloads\Parali setu\docs\diagrams\thumb_scale.png"
    if os.path.exists(scale_img_path):
        slide.shapes.add_picture(scale_img_path, Inches(9.60), Inches(2.00), Inches(2.90), Inches(0.96))
        
        # Details below Scale terminal (Punchy, non-text-heavy bullets)
        scale_desc_box = slide.shapes.add_textbox(Inches(9.60), Inches(3.06), Inches(2.90), Inches(1.00))
        tf_sd = scale_desc_box.text_frame
        tf_sd.word_wrap = True
        tf_sd.margin_left = tf_sd.margin_top = tf_sd.margin_right = tf_sd.margin_bottom = 0
        
        p1 = tf_sd.paragraphs[0]
        p1.text = "⚖️ Dharamkanta IoT Scale Terminal"
        p1.font.bold = True
        p1.font.size = Pt(9.0)
        p1.font.color.rgb = GREEN_ACCENT

        p2 = tf_sd.add_paragraph()
        p2.text = "• RS-232 serial hook logs certified Gross & Tare\n• Net Weight triggers automated UPI escrow payout\n• Zero fraud: Eliminates fake paper slips"
        p2.font.size = Pt(8.0)
        p2.font.color.rgb = TEXT_DARK
        p2.space_before = Pt(2.0)

    # ------------------ 3. Bottom Section: 3 Balanced Columns (Decluttered & Clean) ------------------
    b_top = Inches(4.38)
    b_h = Inches(2.70)

    # ================= Column 1: Tech Stack WITH "WHY WE USED IT" (Punchy, Not Text-Heavy) =================
    col1_l, col1_w = Inches(0.55), Inches(5.35)
    c1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, col1_l, b_top, col1_w, b_h)
    c1.fill.solid()
    c1.fill.fore_color.rgb = CARD_BG
    c1.line.color.rgb = BORDER_ACCENT
    c1.line.width = Pt(1.2)

    c1_title_box = slide.shapes.add_textbox(col1_l + Inches(0.18), b_top + Inches(0.10), col1_w - Inches(0.36), Inches(0.36))
    tf_c1t = c1_title_box.text_frame
    tf_c1t.word_wrap = True
    tf_c1t.margin_left = tf_c1t.margin_top = tf_c1t.margin_right = tf_c1t.margin_bottom = 0

    p_c1t = tf_c1t.paragraphs[0]
    p_c1t.text = "🛠️ Production Tech Stack & Architectural Rationale"
    p_c1t.font.bold = True
    p_c1t.font.size = Pt(11.5)
    p_c1t.font.color.rgb = NAVY_TITLE

    p_c1sub = tf_c1t.add_paragraph()
    p_c1sub.text = "Why Each Technology Was Chosen for Real-World Deployment"
    p_c1sub.font.size = Pt(8.0)
    p_c1sub.font.color.rgb = PRIMARY_BLUE
    p_c1sub.font.bold = True

    # Concise, punchy tech entries (NO TEXT WALLS)
    tech_box = slide.shapes.add_textbox(col1_l + Inches(0.18), b_top + Inches(0.48), col1_w - Inches(0.36), Inches(2.15))
    tf_tech = tech_box.text_frame
    tf_tech.word_wrap = True
    tf_tech.margin_left = tf_tech.margin_top = tf_tech.margin_right = tf_tech.margin_bottom = 0

    tech_items = [
        ("Flutter 3.13 (Dart)", "60 FPS on sub-₹7k rural phones • Offline Noto Gurmukhi/Hindi font bundle • Lightweight APK"),
        ("FastAPI 0.142 (Python 3.12)", "Asynchronous ASGI scale for telemetry • Zero-overhead C-bindings to Google OR-Tools & PostGIS"),
        ("PostgreSQL 15 + PostGIS", "Native ST_DWithin spatial indexing clusters smallholder parcels within 25 km baler radius • RLS security"),
        ("Google OR-Tools CP-SAT", "Solves 4-party NP-hard dispatch in <500ms • Enforces tight 10–15 day post-harvest window"),
        ("Copernicus Sentinel-2 SWIR", "10m satellite ΔNBR < 0.15 spectral scan • Remote, tamper-proof burn verification without site inspectors")
    ]

    for idx, (title, why_text) in enumerate(tech_items):
        p = tf_tech.paragraphs[0] if idx == 0 else tf_tech.add_paragraph()
        run_title = p.add_run()
        run_title.text = f"• {title}: "
        run_title.font.bold = True
        run_title.font.size = Pt(8.5)
        run_title.font.color.rgb = TEXT_DARK

        run_why = p.add_run()
        run_why.text = f"Why: {why_text}"
        run_why.font.size = Pt(7.8)
        run_why.font.color.rgb = RGBColor(71, 85, 105) # Slate 600
        p.space_after = Pt(2.2)

    # ================= Column 2: Extent of AI Tools Used (Punchy, Clean) =================
    col2_l, col2_w = Inches(6.05), Inches(3.55)
    c2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, col2_l, b_top, col2_w, b_h)
    c2.fill.solid()
    c2.fill.fore_color.rgb = CARD_BG
    c2.line.color.rgb = BORDER_LIGHT
    c2.line.width = Pt(1.2)

    c2_title_box = slide.shapes.add_textbox(col2_l + Inches(0.18), b_top + Inches(0.10), col2_w - Inches(0.36), Inches(0.36))
    tf_c2t = c2_title_box.text_frame
    tf_c2t.word_wrap = True
    tf_c2t.margin_left = tf_c2t.margin_top = tf_c2t.margin_right = tf_c2t.margin_bottom = 0

    p_c2t = tf_c2t.paragraphs[0]
    p_c2t.text = "🤖 Extent of AI Tools & Innovations"
    p_c2t.font.bold = True
    p_c2t.font.size = Pt(11.5)
    p_c2t.font.color.rgb = NAVY_TITLE

    p_c2sub = tf_c2t.add_paragraph()
    p_c2sub.text = "Algorithmic Solvers & Satellite Remote Sensing"
    p_c2sub.font.size = Pt(8.0)
    p_c2sub.font.color.rgb = PURPLE_ACCENT
    p_c2sub.font.bold = True

    ai_box = slide.shapes.add_textbox(col2_l + Inches(0.18), b_top + Inches(0.50), col2_w - Inches(0.36), Inches(2.15))
    tf_ai = ai_box.text_frame
    tf_ai.word_wrap = True
    tf_ai.margin_left = tf_ai.margin_top = tf_ai.margin_right = tf_ai.margin_bottom = 0

    ai_items = [
        ("Google OR-Tools CP-SAT:", " Solves 4-party combinatorial dispatch, vehicle routing, and machine capacity limits."),
        ("Sentinel-2 Spectral Engine:", " Calculates ΔNBR (<0.15 threshold) to verify zero burn for ₹1,000/acre DBT subsidy."),
        ("Vernacular Voice NLP:", " Normalizes colloquial spoken numbers and land units (killa, bigha) into GeoJSON."),
        ("Antigravity AI Co-Pilot:", " Autonomous TDD engineering with 100% green test suite (35 pytest + 20 flutter tests).")
    ]

    for idx, (title, desc) in enumerate(ai_items):
        p = tf_ai.paragraphs[0] if idx == 0 else tf_ai.add_paragraph()
        run_t = p.add_run()
        run_t.text = f"★ {title}"
        run_t.font.bold = True
        run_t.font.size = Pt(8.5)
        run_t.font.color.rgb = PURPLE_ACCENT

        run_d = p.add_run()
        run_d.text = desc
        run_d.font.size = Pt(7.8)
        run_d.font.color.rgb = TEXT_DARK
        p.space_after = Pt(3.8)

    # ================= Column 3: Prototype Deliverables & Live Links =================
    col3_l, col3_w = Inches(9.75), Inches(3.05)
    c3 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, col3_l, b_top, col3_w, b_h)
    c3.fill.solid()
    c3.fill.fore_color.rgb = CARD_BG
    c3.line.color.rgb = BORDER_LIGHT
    c3.line.width = Pt(1.2)

    c3_title_box = slide.shapes.add_textbox(col3_l + Inches(0.16), b_top + Inches(0.10), col3_w - Inches(0.32), Inches(0.35))
    tf_c3t = c3_title_box.text_frame
    tf_c3t.margin_left = tf_c3t.margin_top = tf_c3t.margin_right = tf_c3t.margin_bottom = 0
    p_c3t = tf_c3t.paragraphs[0]
    p_c3t.text = "🚀 Project Deliverables"
    p_c3t.font.bold = True
    p_c3t.font.size = Pt(11.5)
    p_c3t.font.color.rgb = NAVY_TITLE

    # Small Box 1: GitHub Link
    gh_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, col3_l + Inches(0.15), b_top + Inches(0.45), col3_w - Inches(0.30), Inches(0.98))
    gh_box.fill.solid()
    gh_box.fill.fore_color.rgb = RGBColor(241, 245, 249) # Slate 100
    gh_box.line.color.rgb = RGBColor(148, 163, 184)     # Slate 400
    gh_box.line.width = Pt(1.2)

    tf_gh = gh_box.text_frame
    tf_gh.word_wrap = True
    tf_gh.margin_left = tf_gh.margin_top = tf_gh.margin_right = tf_gh.margin_bottom = Inches(0.08)

    p_gh1 = tf_gh.paragraphs[0]
    p_gh1.text = "🐙 GitHub Repository (Source Code)"
    p_gh1.font.bold = True
    p_gh1.font.size = Pt(9.2)
    p_gh1.font.color.rgb = TEXT_DARK

    p_gh2 = tf_gh.add_paragraph()
    p_gh2.text = "github.com/Rishabhbansal005/Parali-setu"
    p_gh2.font.bold = True
    p_gh2.font.size = Pt(8.2)
    p_gh2.font.color.rgb = PRIMARY_BLUE

    p_gh3 = tf_gh.add_paragraph()
    p_gh3.text = "MIT Licensed • 100% Green Test Suite"
    p_gh3.font.size = Pt(7.2)
    p_gh3.font.color.rgb = TEXT_MUTED

    # Small Box 2: Demo Video Link
    demo_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, col3_l + Inches(0.15), b_top + Inches(1.52), col3_w - Inches(0.30), Inches(1.10))
    demo_box.fill.solid()
    demo_box.fill.fore_color.rgb = RGBColor(255, 241, 242) # Rose 50
    demo_box.line.color.rgb = RGBColor(251, 113, 133)     # Rose 400
    demo_box.line.width = Pt(1.2)

    tf_dm = demo_box.text_frame
    tf_dm.word_wrap = True
    tf_dm.margin_left = tf_dm.margin_top = tf_dm.margin_right = tf_dm.margin_bottom = Inches(0.08)

    p_dm1 = tf_dm.paragraphs[0]
    p_dm1.text = "🎬 Working Demo Video Link"
    p_dm1.font.bold = True
    p_dm1.font.size = Pt(9.2)
    p_dm1.font.color.rgb = ROSE_ACCENT

    p_dm2 = tf_dm.add_paragraph()
    p_dm2.text = "[ Paste Video URL / QR Code Here ]"
    p_dm2.font.bold = True
    p_dm2.font.size = Pt(8.2)
    p_dm2.font.color.rgb = RGBColor(190, 18, 60) # Rose 700

    p_dm3 = tf_dm.add_paragraph()
    p_dm3.text = "3-Min Golden Path Walkthrough:\nVoice Intake ➔ AI Match ➔ Scale ➔ UPI"
    p_dm3.font.size = Pt(7.2)
    p_dm3.font.color.rgb = TEXT_DARK

    # ------------------ 4. Footer ------------------
    footer_box = slide.shapes.add_textbox(Inches(0.55), Inches(7.18), Inches(12.25), Inches(0.28))
    tf_f = footer_box.text_frame
    tf_f.margin_left = tf_f.margin_top = tf_f.margin_right = tf_f.margin_bottom = 0
    p_f = tf_f.paragraphs[0]
    p_f.text = "@HSC submission- Template  |  ParaliSetu: Technical Architecture & Field-Verified Methodology"
    p_f.font.size = Pt(9)
    p_f.font.color.rgb = TEXT_MUTED
    p_f.alignment = PP_ALIGN.CENTER

    # Save Presentation
    output_path = r"c:\Users\Rishabh Bansal\Downloads\Parali setu\Technical_Approach_Slide.pptx"
    prs.save(output_path)
    print(f"Slide saved successfully to {output_path}")

if __name__ == "__main__":
    build_presentation()
