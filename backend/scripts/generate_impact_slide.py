import os
import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def build_impact_slide():
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
    AMBER_ACCENT = RGBColor(217, 119, 6)     # Amber 600

    # 0. Slide Background Canvas
    bg_shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg_shape.fill.solid()
    bg_shape.fill.fore_color.rgb = BG_COLOR
    bg_shape.line.fill.background()

    # ------------------ 1. Header Elements ------------------
    # 1.1 "Mist" Badge
    badge_left, badge_top, badge_w, badge_h = Inches(0.55), Inches(0.30), Inches(1.25), Inches(0.65)
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
    title_box = slide.shapes.add_textbox(Inches(1.95), Inches(0.24), Inches(8.40), Inches(0.85))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0

    p_t = tf_t.paragraphs[0]
    p_t.text = "Impact Potential"
    p_t.font.bold = True
    p_t.font.size = Pt(28)
    p_t.font.color.rgb = NAVY_TITLE

    p_sub = tf_t.add_paragraph()
    p_sub.text = "Socio-Economic Value Creation, Clean Air Economics & Multi-Stakeholder Matrix"
    p_sub.font.size = Pt(11.5)
    p_sub.font.color.rgb = TEXT_MUTED

    # 1.3 Hack for Social Cause Badge
    hack_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(10.55), Inches(0.30), Inches(2.25), Inches(0.65))
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

    # ------------------ 2. Section 1: 4 Key Impact Metric Tiles (With Verified Sources) ------------------
    tile_top = Inches(1.14)
    tile_h = Inches(0.92)
    tile_w = Inches(2.95)
    tile_gap = Inches(0.15)
    tile_start_x = Inches(0.55)

    metrics = [
        ("₹25,000+", "Net Farmer Gain / 5-Acre Season", "Straw Sales (₹15k) + Subsidy (₹5k) + Soil (₹10k)", "Source: PAU Agronomy & Punjab CRM", "https://www.pau.edu", GREEN_ACCENT, RGBColor(236, 253, 245)),
        ("4.4 MMT", "Annual Bio-CNG Fuel Potential", "Substitutes ~$2.5B in crude & fossil fuel imports", "Source: MoPNG SATAT (mopng.gov.in)", "https://mopng.gov.in", PRIMARY_BLUE, RGBColor(239, 246, 255)),
        ("45M+ People", "Clean Air & Healthcare Shield", "Stops 35–45% severe PM2.5 seasonal smog surge", "Source: World Bank / IFPRI (dyz022)", "https://www.ifpri.org", PURPLE_ACCENT, RGBColor(245, 243, 255)),
        ("30M Tonnes", "Annual CO₂ Diverted from Skies", "Converts 20 MMT parali into circular green wealth", "Source: CAQM Annual Report", "https://caqm.nic.in", ROSE_ACCENT, RGBColor(255, 241, 242))
    ]

    for i, (val, title, sub, src_label, src_url, accent_c, bg_c) in enumerate(metrics):
        cur_x = tile_start_x + i * (tile_w + tile_gap)
        m_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cur_x, tile_top, tile_w, tile_h)
        m_card.fill.solid()
        m_card.fill.fore_color.rgb = bg_c
        m_card.line.color.rgb = accent_c
        m_card.line.width = Pt(1.0)

        tb = slide.shapes.add_textbox(cur_x + Inches(0.12), tile_top + Inches(0.05), tile_w - Inches(0.24), tile_h - Inches(0.10))
        tf_m = tb.text_frame
        tf_m.word_wrap = True
        tf_m.margin_left = tf_m.margin_top = tf_m.margin_right = tf_m.margin_bottom = 0

        p1 = tf_m.paragraphs[0]
        p1.text = val
        p1.font.bold = True
        p1.font.size = Pt(16.0)
        p1.font.color.rgb = accent_c

        p2 = tf_m.add_paragraph()
        p2.text = title
        p2.font.bold = True
        p2.font.size = Pt(8.2)
        p2.font.color.rgb = TEXT_DARK

        p3 = tf_m.add_paragraph()
        p3.text = sub
        p3.font.size = Pt(7.0)
        p3.font.color.rgb = TEXT_MUTED

        p4 = tf_m.add_paragraph()
        r_src = p4.add_run()
        r_src.text = f"🔗 {src_label}"
        r_src.font.bold = True
        r_src.font.size = Pt(6.8)
        r_src.font.color.rgb = accent_c
        r_src.hyperlink.address = src_url

    # ------------------ 3. Section 2: 3 Core Pillars of Impact ------------------
    pillars_top = Inches(2.14)
    pillars_h = Inches(2.68)
    pillar_w = Inches(3.98)
    pillar_gap = Inches(0.15)

    pillars_data = [
        {
            "icon": "💰",
            "title": "Economic Impact on Farmers",
            "subtitle": "Turns Threat of ₹15k Fines into Guaranteed Profit",
            "accent": GREEN_ACCENT,
            "source": "PAU Agronomy & NGT Order OA 118/2013",
            "source_url": "https://www.pau.edu",
            "bullets": [
                ("Converts Liability to Income", "Replaces ₹15k fine risk with ₹2,500–₹3,000/acre in direct straw sales (2.0 t/acre @ ₹1,500/t)."),
                ("Instant Escrow Cash Payout", "Certified weighbridge net weight slip automatically releases UPI funds to farmer account."),
                ("Direct ₹1,000/acre Ex-Situ DBT", "Copernicus Sentinel-2 No-Burn certificate unlocks government ex-situ subsidy without delays."),
                ("Preserves Soil N-P-K-S", "Halts burning of 33 kg N-P-K-S per tonne of straw; saves farmers ₹2,000/acre in extra fertilizer.")
            ]
        },
        {
            "icon": "🌿",
            "title": "Public Health & Clean Energy",
            "subtitle": "Solving the $19B Indo-Gangetic Smog Crisis",
            "accent": PRIMARY_BLUE,
            "source": "World Bank & ICRIER Air Pollution Study (2021)",
            "source_url": "https://www.ifpri.org",
            "bullets": [
                ("Averts Seasonal Smog (AQI 450+)", "Stops post-monsoon smoke plume contributing 35–45% of Delhi-NCR's critical PM2.5 spike."),
                ("Protects 45M+ North Indians", "Averts ~₹1.5 Lakh Crore ($19B) annual respiratory disease, hospitalizations & lost worker output."),
                ("Fuels India's Bio-CNG Economy", "Supplies SATAT CBG plants (1t straw = 220kg green gas); cuts LNG imports by ~$2.5B annually."),
                ("Halts Microbial Soil Death", "Protects beneficial subterranean earthworms and bacteria killed by 400°C surface fire heat.")
            ]
        },
        {
            "icon": "🏛️",
            "title": "Governance & Sovereign Trust",
            "subtitle": "Automated Compliance Without Corrupt Bureaucracy",
            "accent": PURPLE_ACCENT,
            "source": "ESA Copernicus Sentinel-2 & CAQM Guidelines",
            "source_url": "https://caqm.nic.in",
            "bullets": [
                ("Zero Physical Field Audits", "100% remote Copernicus Sentinel-2 SWIR satellite scan (ΔNBR < 0.15) eliminates manual bias."),
                ("Tamper-Proof Scale Logging", "Direct RS-232 serial weighbridge integration eliminates corruptible paper weight slips."),
                ("CAQM & DAO Oversight Portal", "Real-time district administrative map tracking diverted biomass, fire counts & verified DBT."),
                ("Row-Level Security (RLS)", "Cryptographic data isolation across 12 relational database tables ensures complete auditability.")
            ]
        }
    ]

    for j, p_data in enumerate(pillars_data):
        cur_px = tile_start_x + j * (pillar_w + pillar_gap)
        p_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cur_px, pillars_top, pillar_w, pillars_h)
        p_card.fill.solid()
        p_card.fill.fore_color.rgb = CARD_BG
        p_card.line.color.rgb = BORDER_ACCENT
        p_card.line.width = Pt(1.2)

        # Header Box
        tb_ph = slide.shapes.add_textbox(cur_px + Inches(0.18), pillars_top + Inches(0.08), pillar_w - Inches(0.36), Inches(0.40))
        tf_ph = tb_ph.text_frame
        tf_ph.word_wrap = True
        tf_ph.margin_left = tf_ph.margin_top = tf_ph.margin_right = tf_ph.margin_bottom = 0

        pp1 = tf_ph.paragraphs[0]
        pp1.text = f"{p_data['icon']} {p_data['title']}"
        pp1.font.bold = True
        pp1.font.size = Pt(11.5)
        pp1.font.color.rgb = NAVY_TITLE

        pp2 = tf_ph.add_paragraph()
        pp2.text = p_data['subtitle']
        pp2.font.bold = True
        pp2.font.size = Pt(7.8)
        pp2.font.color.rgb = p_data['accent']

        # Bullets Box
        tb_pb = slide.shapes.add_textbox(cur_px + Inches(0.18), pillars_top + Inches(0.48), pillar_w - Inches(0.36), Inches(1.85))
        tf_pb = tb_pb.text_frame
        tf_pb.word_wrap = True
        tf_pb.margin_left = tf_pb.margin_top = tf_pb.margin_right = tf_pb.margin_bottom = 0

        for b_idx, (b_head, b_desc) in enumerate(p_data["bullets"]):
            bp = tf_pb.paragraphs[0] if b_idx == 0 else tf_pb.add_paragraph()
            r_h = bp.add_run()
            r_h.text = f"• {b_head}: "
            r_h.font.bold = True
            r_h.font.size = Pt(8.2)
            r_h.font.color.rgb = TEXT_DARK

            r_d = bp.add_run()
            r_d.text = b_desc
            r_d.font.size = Pt(7.5)
            r_d.font.color.rgb = RGBColor(71, 85, 105) # Slate 600
            bp.space_after = Pt(1.8)

        # Citation Tag inside card
        tb_psrc = slide.shapes.add_textbox(cur_px + Inches(0.18), pillars_top + Inches(2.42), pillar_w - Inches(0.36), Inches(0.20))
        tf_psrc = tb_psrc.text_frame
        tf_psrc.margin_left = tf_psrc.margin_top = tf_psrc.margin_right = tf_psrc.margin_bottom = 0
        p_csrc = tf_psrc.paragraphs[0]
        r_csrc = p_csrc.add_run()
        r_csrc.text = f"📋 Citation: {p_data['source']}"
        r_csrc.font.bold = True
        r_csrc.font.size = Pt(7.0)
        r_csrc.font.color.rgb = p_data['accent']
        r_csrc.hyperlink.address = p_data['source_url']

    # ------------------ 4. Section 3: Multi-Stakeholder Matrix ------------------
    sh_top = Inches(4.90)
    sh_h = Inches(1.98)
    sh_w = Inches(12.25)
    sh_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, tile_start_x, sh_top, sh_w, sh_h)
    sh_card.fill.solid()
    sh_card.fill.fore_color.rgb = CARD_BG
    sh_card.line.color.rgb = BORDER_LIGHT
    sh_card.line.width = Pt(1.2)

    # Matrix Title
    tb_smt = slide.shapes.add_textbox(tile_start_x + Inches(0.18), sh_top + Inches(0.08), sh_w - Inches(0.36), Inches(0.30))
    tf_smt = tb_smt.text_frame
    tf_smt.word_wrap = True
    tf_smt.margin_left = tf_smt.margin_top = tf_smt.margin_right = tf_smt.margin_bottom = 0

    p_smt1 = tf_smt.paragraphs[0]
    p_smt1.text = "👥 Multi-Stakeholder Value Matrix: Tailored for Every Actor in the Value Chain"
    p_smt1.font.bold = True
    p_smt1.font.size = Pt(11.0)
    p_smt1.font.color.rgb = NAVY_TITLE

    p_smt2 = tf_smt.add_paragraph()
    p_smt2.text = "Eliminating Friction Across the Entire Agronomic Supply Chain (Direct Farmer to Industrial Offtaker)"
    p_smt2.font.bold = True
    p_smt2.font.size = Pt(7.8)
    p_smt2.font.color.rgb = PRIMARY_BLUE

    # 4 Stakeholder Cards inside the container
    sc_y = sh_top + Inches(0.42)
    sc_h = Inches(1.48)
    sc_w = Inches(2.93)
    sc_gap = Inches(0.12)
    sc_start_x = tile_start_x + Inches(0.14)

    stakeholders = [
        {
            "icon": "🚜",
            "name": "Smallholder Farmers (Kisaan)",
            "role": "Target Beneficiary (2–5 Acre Holdings)",
            "pain": "15-day deadline before wheat sowing; fear of ₹15,000 fines; commercial balers refuse small parcels.",
            "gain": "Voice-first intake (hi/pa); automatic smallholder parcel clustering; instant UPI escrow cash payout.",
            "color": GREEN_ACCENT,
            "bg": RGBColor(236, 253, 245)
        },
        {
            "icon": "⚙️",
            "name": "Baler & Fleet Operators",
            "role": "Custom Hiring Centers & Aggregators",
            "pain": "Deadhead travel costs for 2-acre parcels; under-utilized ₹15L machinery during tight 20-day peak.",
            "gain": "OR-Tools groups neighboring farms into 25–40 acre contiguous runs; lifts equipment throughput to 85%.",
            "color": PRIMARY_BLUE,
            "bg": RGBColor(239, 246, 255)
        },
        {
            "icon": "🏭",
            "name": "Bio-CNG & Industrial Plants",
            "role": "Industrial Offtakers (CBG / 2G Ethanol)",
            "pain": "Unpredictable daily biomass feedstocks; costly boiler shutdowns if straw deliveries halt.",
            "gain": "Web portal sets daily intake quotas (200+ t/day); guaranteed contracted straw via pre-funded escrow.",
            "color": AMBER_ACCENT,
            "bg": RGBColor(254, 243, 199)
        },
        {
            "icon": "🏛️",
            "name": "Government & Regulators",
            "role": "CAQM, KVK & District Agriculture DAOs",
            "pain": "Physically impossible to manually inspect thousands of villages; fraudulent paper subsidy claims.",
            "gain": "Copernicus Sentinel-2 remote burn verification; 1-click transparent ₹1,000/acre DBT subsidy clearance.",
            "color": PURPLE_ACCENT,
            "bg": RGBColor(245, 243, 255)
        }
    ]

    for k, s in enumerate(stakeholders):
        cur_scx = sc_start_x + k * (sc_w + sc_gap)
        sc_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cur_scx, sc_y, sc_w, sc_h)
        sc_card.fill.solid()
        sc_card.fill.fore_color.rgb = s["bg"]
        sc_card.line.color.rgb = s["color"]
        sc_card.line.width = Pt(1.0)

        tb_sc = slide.shapes.add_textbox(cur_scx + Inches(0.10), sc_y + Inches(0.05), sc_w - Inches(0.20), sc_h - Inches(0.10))
        tf_sc = tb_sc.text_frame
        tf_sc.word_wrap = True
        tf_sc.margin_left = tf_sc.margin_top = tf_sc.margin_right = tf_sc.margin_bottom = 0

        p_s1 = tf_sc.paragraphs[0]
        p_s1.text = f"{s['icon']} {s['name']}"
        p_s1.font.bold = True
        p_s1.font.size = Pt(8.8)
        p_s1.font.color.rgb = TEXT_DARK

        p_s2 = tf_sc.add_paragraph()
        p_s2.text = s["role"]
        p_s2.font.bold = True
        p_s2.font.size = Pt(7.0)
        p_s2.font.color.rgb = s["color"]

        p_s3 = tf_sc.add_paragraph()
        r_pn = p_s3.add_run()
        r_pn.text = "• Pain: "
        r_pn.font.bold = True
        r_pn.font.size = Pt(7.0)
        r_pn.font.color.rgb = ROSE_ACCENT
        r_pnt = p_s3.add_run()
        r_pnt.text = s["pain"]
        r_pnt.font.size = Pt(6.8)
        r_pnt.font.color.rgb = TEXT_DARK
        p_s3.space_before = Pt(1.5)

        p_s4 = tf_sc.add_paragraph()
        r_gn = p_s4.add_run()
        r_gn.text = "• Solution: "
        r_gn.font.bold = True
        r_gn.font.size = Pt(7.0)
        r_gn.font.color.rgb = GREEN_ACCENT
        r_gnt = p_s4.add_run()
        r_gnt.text = s["gain"]
        r_gnt.font.size = Pt(6.8)
        r_gnt.font.color.rgb = TEXT_DARK
        p_s4.space_before = Pt(1.0)

    # ------------------ 5. Section 4: Ground Truth Verification Strip ------------------
    verif_box = slide.shapes.add_textbox(Inches(0.55), Inches(6.94), Inches(12.25), Inches(0.24))
    tf_v = verif_box.text_frame
    tf_v.margin_left = tf_v.margin_top = tf_v.margin_right = tf_v.margin_bottom = 0
    p_v = tf_v.paragraphs[0]
    p_v.alignment = PP_ALIGN.CENTER

    r_vt = p_v.add_run()
    r_vt.text = "🔍 Official Sources & Ground Truth Verification:  "
    r_vt.font.bold = True
    r_vt.font.size = Pt(7.2)
    r_vt.font.color.rgb = NAVY_TITLE

    sources_list = [
        ("World Bank / IFPRI Health Study (doi:10.1093/ije/dyz022)", "https://www.ifpri.org"),
        ("MoPNG SATAT Scheme (mopng.gov.in)", "https://mopng.gov.in"),
        ("CAQM NCR Directives (caqm.nic.in)", "https://caqm.nic.in"),
        ("PAU Stubble Soil Agronomy (pau.edu)", "https://www.pau.edu")
    ]

    for s_idx, (s_name, s_url) in enumerate(sources_list):
        if s_idx > 0:
            r_sep = p_v.add_run()
            r_sep.text = "  •  "
            r_sep.font.size = Pt(7.0)
            r_sep.font.color.rgb = TEXT_MUTED

        r_s = p_v.add_run()
        r_s.text = s_name
        r_s.font.size = Pt(7.0)
        r_s.font.bold = True
        r_s.font.color.rgb = PRIMARY_BLUE
        r_s.hyperlink.address = s_url

    # ------------------ 6. Footer ------------------
    footer_box = slide.shapes.add_textbox(Inches(0.55), Inches(7.20), Inches(12.25), Inches(0.22))
    tf_f = footer_box.text_frame
    tf_f.margin_left = tf_f.margin_top = tf_f.margin_right = tf_f.margin_bottom = 0
    p_f = tf_f.paragraphs[0]
    p_f.text = "@HSC submission- Template  |  ParaliSetu: Multi-Stakeholder Impact Potential & Socio-Economic Value"
    p_f.font.size = Pt(8.5)
    p_f.font.color.rgb = TEXT_MUTED
    p_f.alignment = PP_ALIGN.CENTER

    # Save Presentation
    output_path = r"c:\Users\Rishabh Bansal\Downloads\Parali setu\Impact_Potential_Slide.pptx"
    prs.save(output_path)
    print(f"Impact slide saved successfully to {output_path}")

if __name__ == "__main__":
    build_impact_slide()
