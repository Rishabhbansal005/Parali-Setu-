import os
from PIL import Image, ImageDraw, ImageOps

def create_thumbnails():
    os.makedirs("docs/diagrams", exist_ok=True)

    # 1. Mobile App Voice Intake Thumbnail
    mob_path = "docs/screenshots/03_voice_vernacular_chips.png"
    if os.path.exists(mob_path):
        img_mob = Image.open(mob_path)
        # Crop: remove status bar (top 120px) and bottom nav bar (bottom 150px)
        w, h = img_mob.size
        cropped_mob = img_mob.crop((40, 140, w - 40, h - 160))
        # Resize to thumbnail (width 400, keep aspect ratio)
        cropped_mob.thumbnail((420, 520), Image.Resampling.LANCZOS)
        
        # Add subtle rounded corners and clean border
        border_img = ImageOps.expand(cropped_mob, border=2, fill='#94A3B8')
        border_img.save("docs/diagrams/thumb_mobile.png", "PNG")
        print("Created docs/diagrams/thumb_mobile.png", border_img.size)

    # 2. Dharamkanta Weighbridge Terminal Thumbnail
    web_path = "docs/screenshots/07_dharamkanta_weighbridge.png"
    if os.path.exists(web_path):
        img_web = Image.open(web_path)
        w, h = img_web.size
        # Crop the Shipment Queue & Weight Entry section (x: 320 to 1860, y: 380 to 900)
        cropped_web = img_web.crop((340, 380, 1860, 900))
        cropped_web.thumbnail((620, 320), Image.Resampling.LANCZOS)
        border_web = ImageOps.expand(cropped_web, border=2, fill='#94A3B8')
        border_web.save("docs/diagrams/thumb_scale.png", "PNG")
        print("Created docs/diagrams/thumb_scale.png", border_web.size)

if __name__ == "__main__":
    create_thumbnails()
