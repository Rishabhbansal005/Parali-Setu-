import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_clean_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    slide = prs.slides.add_slide(prs.slide_layouts[6])

    # -------------------------------------------------------------
    # 1. CLEAN REFINED PALETTE (Minimalist & Breathable)
    # -------------------------------------------------------------
    BG_CANVAS        = RGBColor(250, 252, 255)  # Crisp soft canvas (#FAFCFF)
    CARD_BG          = RGBColor(255, 255, 255)  # Pure White
    CARD_BORDER      = RGBColor(226, 232, 240)  # Slate-200
    TEXT_TITLE       = RGBColor(15, 23, 42)     # Slate-900 (#0F172A)
    TEXT_SUBTITLE    = RGBColor(71, 85, 105)    # Slate-600 (#475569)
    TEXT_BODY        = RGBColor(51, 65, 85)     # Slate-700 (#334155)
    TEXT_MUTED       = RGBColor(100, 116, 139)  # Slate-500 (#64748B)

    # Accent Colors
    RED_ACCENT       = RGBColor(225, 29, 72)    # Rose-600
    RED_BG           = RGBColor(255, 241, 242)  # Rose-50
    GREEN_ACCENT     = RGBColor(5, 150, 105)    # Emerald-600
    GREEN_BG         = RGBColor(236, 253, 245)  # Emerald-50
    BLUE_ACCENT      = RGBColor(29, 78, 216)    # Blue-700
    BLUE_BG          = RGBColor(239, 246, 255)  # Blue-50
    AMBER_ACCENT     = RGBColor(180, 83, 9)     # Amber-700
    AMBER_BG         = RGBColor(254, 243, 199)  # Amber-100

    # Background Canvas
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = BG_CANVAS
    bg.line.fill.background()

    # -------------------------------------------------------------
    # 2. HEADER SECTION (Clean, uncluttered, airy)
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

    # Title & Subtitle Box
    title_box = slide.shapes.add_textbox(Inches(2.35), Inches(0.25), Inches(7.8), Inches(0.85))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    p_t = tf_t.paragraphs[0]
    p_t.text = "Problem – Proposed Solution"
    p_t.font.name = "Segoe UI"
    p_t.font.size = Pt(26)
    p_t.font.bold = True
    p_t.font.color.rgb = RGBColor(30, 58, 138)

    p_sub = tf_t.add_paragraph()
    p_sub.text = "ParaliSetu: Voice-First Agronomic Supply Chain & Dual-Verification Marketplace"
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
    # 3-COLUMN CLEAN CARD ARCHITECTURE (Height: 5.65 in)
    # -------------------------------------------------------------
    cards_y = Inches(1.25)
    cards_h = Inches(5.65)

    # =============================================================
    # COLUMN 1: THE CORE PROBLEM (Width: 3.70 in)
    # =============================================================
    c1_x = Inches(0.70)
    c1_w = Inches(3.70)

    card1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c1_x, cards_y, c1_w, cards_h)
    card1.fill.solid()
    card1.fill.fore_color.rgb = CARD_BG
    card1.line.color.rgb = CARD_BORDER
    card1.line.width = Pt(1)

    # Header Ribbon
    h1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c1_x, cards_y, c1_w, Inches(0.55))
    h1.fill.solid()
    h1.fill.fore_color.rgb = RED_BG
    h1.line.fill.background()
    tf_h1 = h1.text_frame
    tf_h1.vertical_anchor = MSO_ANCHOR.MIDDLE
    p_h1 = tf_h1.paragraphs[0]
    p_h1.text = "🚨  The Core Problem"
    p_h1.font.name = "Segoe UI"
    p_h1.font.size = Pt(14)
    p_h1.font.bold = True
    p_h1.font.color.rgb = RED_ACCENT

    # Clean Stat KPI Badges (Clean horizontal bars instead of heavy boxes)
    kpi_data = [
        ("20M Tonnes", "Burned Annually", "Choking North India in seasonal toxic smog"),
        ("10–15 Days", "Sowing Deadline", "Yield loss if wheat sowing is delayed"),
        ("₹15,000 Fine", "Punitive Penalty", "Farmers penalized with zero viable alternative")
    ]
    curr_y1 = cards_y + Inches(0.70)
    for num, tag, note in kpi_data:
        # Mini clean bar
        bar = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c1_x + Inches(0.2), curr_y1, c1_w - Inches(0.4), Inches(0.68))
        bar.fill.solid()
        bar.fill.fore_color.rgb = RGBColor(254, 242, 242)
        bar.line.fill.background()
        tf_b = bar.text_frame
        tf_b.word_wrap = True
        tf_b.margin_left = Inches(0.15)
        tf_b.margin_top = Inches(0.06)
        p_b1 = tf_b.paragraphs[0]
        p_b1.text = f"{num}  ·  {tag}"
        p_b1.font.name = "Segoe UI"
        p_b1.font.size = Pt(12)
        p_b1.font.bold = True
        p_b1.font.color.rgb = RED_ACCENT
        p_b2 = tf_b.add_paragraph()
        p_b2.text = note
        p_b2.font.name = "Segoe UI"
        p_b2.font.size = Pt(8.8)
        p_b2.font.color.rgb = TEXT_BODY
        curr_y1 += Inches(0.78)

    # Core Pain Points (Clean bullets, NO nested boxes)
    tb_prob = slide.shapes.add_textbox(c1_x + Inches(0.2), curr_y1 + Inches(0.1), c1_w - Inches(0.4), Inches(2.2))
    tf_pr = tb_prob.text_frame
    tf_pr.word_wrap = True
    tf_pr.margin_left = 0
    tf_pr.margin_right = 0
    
    p_pr_title = tf_pr.paragraphs[0]
    p_pr_title.text = "Why Traditional Clearing Fails:"
    p_pr_title.font.name = "Segoe UI"
    p_pr_title.font.size = Pt(11)
    p_pr_title.font.bold = True
    p_pr_title.font.color.rgb = TEXT_TITLE
    p_pr_title.space_after = Pt(8)

    pain_points = [
        ("The 15-Day Rush Trap", "Burning is the only instant, zero-cost method a farmer has before wheat planting."),
        ("Smallholder Exclusion", "Commercial balers refuse scattered 2–4 acre fields due to machine transit costs."),
        ("Broken Off-take Link", "Bio-CNG plants (SATAT policy) need straw, but lack direct rural procurement.")
    ]
    for p_head, p_desc in pain_points:
        p_pt = tf_pr.add_paragraph()
        p_pt.text = f"• {p_head}: "
        p_pt.font.name = "Segoe UI"
        p_pt.font.size = Pt(9.5)
        p_pt.font.bold = True
        p_pt.font.color.rgb = TEXT_TITLE
        
        # Add normal weight description
        run = p_pt.add_run()
        run.text = p_desc
        run.font.name = "Segoe UI"
        run.font.size = Pt(9.2)
        run.font.bold = False
        run.font.color.rgb = TEXT_MUTED
        p_pt.space_after = Pt(8)

    # =============================================================
    # COLUMN 2: PROPOSED SOLUTION (HERO CENTER, Width: 4.40 in)
    # =============================================================
    c2_x = Inches(4.55)
    c2_w = Inches(4.30)

    card2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c2_x, cards_y, c2_w, cards_h)
    card2.fill.solid()
    card2.fill.fore_color.rgb = CARD_BG
    card2.line.color.rgb = GREEN_ACCENT
    card2.line.width = Pt(1.5)

    # Header Ribbon
    h2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c2_x, cards_y, c2_w, Inches(0.55))
    h2.fill.solid()
    h2.fill.fore_color.rgb = GREEN_BG
    h2.line.fill.background()
    tf_h2 = h2.text_frame
    tf_h2.vertical_anchor = MSO_ANCHOR.MIDDLE
    p_h2 = tf_h2.paragraphs[0]
    p_h2.text = "🌱  Proposed Solution: ParaliSetu"
    p_h2.font.name = "Segoe UI"
    p_h2.font.size = Pt(14)
    p_h2.font.bold = True
    p_h2.font.color.rgb = GREEN_ACCENT

    # Hero Tagline
    sub_tag = slide.shapes.add_textbox(c2_x + Inches(0.2), cards_y + Inches(0.60), c2_w - Inches(0.4), Inches(0.35))
    tf_st = sub_tag.text_frame
    p_st = tf_st.paragraphs[0]
    p_st.text = "5-Step Connected Operational Journey"
    p_st.font.name = "Segoe UI"
    p_st.font.size = Pt(11)
    p_st.font.bold = True
    p_st.font.color.rgb = TEXT_MUTED

    # 5 Streamlined Process Steps (Clean, airy cards with subtle pills)
    clean_steps = [
        ("01", "Voice Intake", "Farmer speaks parcel & variety in Punjabi/Hindi; receives instant affirmation card.", GREEN_BG, GREEN_ACCENT),
        ("02", "Agronomic Valuation", "PAU math estimates recoverable baled straw (~2.0 t/acre) and fair farmer earnings.", BLUE_BG, BLUE_ACCENT),
        ("03", "Contiguous Cluster Dispatch", "Clusters adjacent 2-acre parcels into 30-acre runs for commercial balers & trucks.", BLUE_BG, BLUE_ACCENT),
        ("04", "Scale Weighment & Escrow", "Certified Dharamkanta net scale ticket instantly releases pre-funded escrow cash.", GREEN_BG, GREEN_ACCENT),
        ("05", "Satellite No-Burn Audit", "Sentinel-2 spectral scan confirms zero field burning; issues official KVK certificate.", AMBER_BG, AMBER_ACCENT)
    ]
    curr_y2 = cards_y + Inches(0.95)
    for idx, (num, step_name, step_detail, s_bg, s_color) in enumerate(clean_steps):
        s_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c2_x + Inches(0.2), curr_y2, c2_w - Inches(0.4), Inches(0.80))
        s_card.fill.solid()
        s_card.fill.fore_color.rgb = s_bg
        s_card.line.fill.background()
        
        # Pill
        pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c2_x + Inches(0.32), curr_y2 + Inches(0.12), Inches(0.45), Inches(0.25))
        pill.fill.solid()
        pill.fill.fore_color.rgb = s_color
        pill.line.fill.background()
        tf_pl = pill.text_frame
        tf_pl.vertical_anchor = MSO_ANCHOR.MIDDLE
        p_pl = tf_pl.paragraphs[0]
        p_pl.text = num
        p_pl.font.name = "Segoe UI"
        p_pl.font.size = Pt(9.5)
        p_pl.font.bold = True
        p_pl.font.color.rgb = RGBColor(255, 255, 255)
        p_pl.alignment = PP_ALIGN.CENTER

        # Text Frame
        tf_step = s_card.text_frame
        tf_step.word_wrap = True
        tf_step.margin_left = Inches(0.65)
        tf_step.margin_top = Inches(0.08)
        p_sname = tf_step.paragraphs[0]
        p_sname.text = step_name
        p_sname.font.name = "Segoe UI"
        p_sname.font.size = Pt(11)
        p_sname.font.bold = True
        p_sname.font.color.rgb = s_color

        p_sdet = tf_step.add_paragraph()
        p_sdet.text = step_detail
        p_sdet.font.name = "Segoe UI"
        p_sdet.font.size = Pt(8.8)
        p_sdet.font.color.rgb = TEXT_BODY

        if idx < 4:
            arrow = slide.shapes.add_shape(MSO_SHAPE.DOWN_ARROW, c2_x + (c2_w / 2) - Inches(0.07), curr_y2 + Inches(0.80), Inches(0.14), Inches(0.11))
            arrow.fill.solid()
            arrow.fill.fore_color.rgb = RGBColor(203, 213, 225)
            arrow.line.fill.background()

        curr_y2 += Inches(0.92)

    # =============================================================
    # COLUMN 3: HOW IT ADDRESSES & UNIQUENESS (Width: 3.75 in)
    # =============================================================
    c3_x = Inches(9.00)
    c3_w = Inches(3.70)

    card3 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c3_x, cards_y, c3_w, cards_h)
    card3.fill.solid()
    card3.fill.fore_color.rgb = CARD_BG
    card3.line.color.rgb = CARD_BORDER
    card3.line.width = Pt(1)

    # Top Ribbon (Blue)
    h3 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c3_x, cards_y, c3_w, Inches(0.55))
    h3.fill.solid()
    h3.fill.fore_color.rgb = BLUE_BG
    h3.line.fill.background()
    tf_h3 = h3.text_frame
    tf_h3.vertical_anchor = MSO_ANCHOR.MIDDLE
    p_h3 = tf_h3.paragraphs[0]
    p_h3.text = "🎯  Addressing The Crisis"
    p_h3.font.name = "Segoe UI"
    p_h3.font.size = Pt(14)
    p_h3.font.bold = True
    p_h3.font.color.rgb = BLUE_ACCENT

    # Clean Impact Points (No heavy nested boxes, just clean rows)
    tb_imp = slide.shapes.add_textbox(c3_x + Inches(0.2), cards_y + Inches(0.65), c3_w - Inches(0.4), Inches(1.8))
    tf_imp = tb_imp.text_frame
    tf_imp.word_wrap = True
    tf_imp.margin_left = 0
    tf_imp.margin_right = 0
    
    impacts = [
        ("Waste to Wealth", "Converts fine into ₹1,800–₹3,200/acre net profit (₹10,000+ for a 4-acre field)."),
        ("Solves 15-Day Rush", "Cluster dispatch guarantees rapid clearance before wheat sowing deadline."),
        ("Zero Payment Default", "Buyer escrow locked upfront; eliminates chronic factory payment delays.")
    ]
    for idx, (imp_title, imp_desc) in enumerate(impacts):
        p_im = tf_imp.paragraphs[0] if idx == 0 else tf_imp.add_paragraph()
        p_im.text = f"✔  {imp_title}: "
        p_im.font.name = "Segoe UI"
        p_im.font.size = Pt(9.8)
        p_im.font.bold = True
        p_im.font.color.rgb = GREEN_ACCENT if idx == 0 else (BLUE_ACCENT if idx == 1 else AMBER_ACCENT)
        run = p_im.add_run()
        run.text = imp_desc
        run.font.name = "Segoe UI"
        run.font.size = Pt(9.0)
        run.font.bold = False
        run.font.color.rgb = TEXT_BODY
        p_im.space_after = Pt(7)

    # Clean Divider Ribbon: Innovation & Uniqueness
    div_rib = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, c3_x + Inches(0.2), cards_y + Inches(2.65), c3_w - Inches(0.4), Inches(0.38))
    div_rib.fill.solid()
    div_rib.fill.fore_color.rgb = AMBER_BG
    div_rib.line.fill.background()
    tf_div = div_rib.text_frame
    tf_div.vertical_anchor = MSO_ANCHOR.MIDDLE
    p_dv = tf_div.paragraphs[0]
    p_dv.text = "⭐  Innovation & Uniqueness (Our Moat)"
    p_dv.font.name = "Segoe UI"
    p_dv.font.size = Pt(11)
    p_dv.font.bold = True
    p_dv.font.color.rgb = AMBER_ACCENT

    # 4 Breakthrough Points (Clean, readable text list - ZERO TECH STACK)
    tb_inn = slide.shapes.add_textbox(c3_x + Inches(0.2), cards_y + Inches(3.10), c3_w - Inches(0.4), Inches(2.4))
    tf_inn = tb_inn.text_frame
    tf_inn.word_wrap = True
    tf_inn.margin_left = 0
    tf_inn.margin_right = 0
    
    unique_points = [
        ("Contiguous Parcel Clustering", "Aggregates scattered 2-acre parcels into profitable 30-acre commercial baling blocks so contractors stop refusing smallholders."),
        ("Zero-Literacy Audio Protocol", "Native spoken dialect intake with an instant visual-audio affirmation card, eliminating digital and literacy barriers."),
        ("Dual Physical + Satellite Trust", "Fuses physical scale certification (instant cash) with satellite spectral burn auditing (unlocks govt subsidies)."),
        ("Zero Capex Deployment", "Operates entirely on standard mobile devices and existing rural weighbridge scales without expensive proprietary hardware.")
    ]
    for idx, (u_title, u_desc) in enumerate(unique_points):
        p_un = tf_inn.paragraphs[0] if idx == 0 else tf_inn.add_paragraph()
        p_un.text = f"★  {u_title}: "
        p_un.font.name = "Segoe UI"
        p_un.font.size = Pt(9.5)
        p_un.font.bold = True
        p_un.font.color.rgb = TEXT_TITLE
        run = p_un.add_run()
        run.text = u_desc
        run.font.name = "Segoe UI"
        run.font.size = Pt(8.6)
        run.font.bold = False
        run.font.color.rgb = TEXT_MUTED
        p_un.space_after = Pt(7)

    # -------------------------------------------------------------
    # 4. FOOTER
    # -------------------------------------------------------------
    footer = slide.shapes.add_textbox(Inches(0.7), Inches(7.05), Inches(12.0), Inches(0.30))
    tf_f = footer.text_frame
    p_f = tf_f.paragraphs[0]
    p_f.text = "@HSC submission- Template  |  ParaliSetu: Transforming North India's Stubble Crisis into Agricultural Wealth"
    p_f.font.name = "Segoe UI"
    p_f.font.size = Pt(9)
    p_f.font.color.rgb = TEXT_MUTED
    p_f.alignment = PP_ALIGN.CENTER

    out_path = r"C:\Users\Rishabh Bansal\Downloads\Parali setu\Problem_Proposed_Solution_Slide.pptx"
    prs.save(out_path)
    print(f"Clean, decluttered presentation saved: {out_path}")

if __name__ == "__main__":
    create_clean_deck()
