import os
import subprocess
import shutil
import zipfile

# 1. Update HTML
html_path = 'c:/Users/Rishabh Bansal/Downloads/Parali setu/docs/business/business_model_canvas_print.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace(
    '<div class="meta-chip"><strong>Hackathon:</strong> Hack for Social</div>',
    '<div class="meta-chip"><strong>Challenge:</strong> SEVA First Innovation Challenge 2026</div>'
)
html = html.replace('Hack for Social 2026', 'SEVA First 2026 · DTU & Delhi Govt')
html = html.replace('Hack for Social', 'SEVA First 2026')

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("HTML updated successfully!")

# 2. Update Markdown
md_path = 'c:/Users/Rishabh Bansal/Downloads/Parali setu/docs/business/business_model_canvas.md'
with open(md_path, 'r', encoding='utf-8') as f:
    md = f.read()

md = md.replace('Hack for Social Hackathon', 'SEVA First Innovation Challenge 2026 (DTU & Govt. of NCT of Delhi)')
md = md.replace('Hack for Social 2026', 'SEVA First Innovation Challenge 2026')
md = md.replace('Hack for Social', 'SEVA First Innovation Challenge 2026')

with open(md_path, 'w', encoding='utf-8') as f:
    f.write(md)
print("Markdown updated successfully!")

# 3. Update generate_bmc_pdf.py
py_script = 'c:/Users/Rishabh Bansal/Downloads/Parali setu/backend/scripts/generate_bmc_pdf.py'
with open(py_script, 'r', encoding='utf-8') as f:
    py_code = f.read()

py_code = py_code.replace('Hack for Social', 'SEVA First Innovation Challenge 2026 (DTU & Delhi Govt)')
with open(py_script, 'w', encoding='utf-8') as f:
    f.write(py_code)
print("Python script updated successfully!")

# 4. Render HTML to PDF using Chrome Headless
pdf_target = 'c:/Users/Rishabh Bansal/Downloads/Parali setu/docs/business/ParaliSetu_Business_Model_Canvas.pdf'
chrome_exe = 'C:/Program Files/Google/Chrome/Application/chrome.exe'
html_file_url = 'file:///' + os.path.abspath(html_path).replace('\\', '/')

cmd = [
    chrome_exe,
    '--headless=new',
    '--disable-gpu',
    '--run-all-compositor-stages-before-draw',
    '--no-pdf-header-footer',
    f'--print-to-pdf={os.path.abspath(pdf_target)}',
    html_file_url
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Chrome print-to-pdf exited with code:", res.returncode)
if os.path.exists(pdf_target):
    print("Generated PDF size:", os.path.getsize(pdf_target), "bytes")

# 5. Copy to Desktop and Downloads
destinations = [
    'C:/Users/Rishabh Bansal/Desktop/ParaliSetu_Business_Model_Canvas.pdf',
    'C:/Users/Rishabh Bansal/OneDrive/Desktop/ParaliSetu_Business_Model_Canvas.pdf',
    'C:/Users/Rishabh Bansal/Downloads/ParaliSetu_Business_Model_Canvas.pdf'
]

for dest in destinations:
    try:
        shutil.copy(pdf_target, dest)
        print(f"Copied to {dest}")
    except Exception as e:
        print(f"Error copying to {dest}: {e}")

# 6. Update the ZIP archive so it has the refreshed PDF
zip_path = 'C:/Users/Rishabh Bansal/Downloads/ParaliSetu_Supporting_Evidence_Archive.zip'
if os.path.exists(zip_path):
    # Add/update the file in zip
    with zipfile.ZipFile(zip_path, 'a') as zf:
        zf.write(pdf_target, arcname='ParaliSetu_Business_Model_Canvas.pdf')
    print("ZIP archive updated with new BMC PDF!")

print("ALL COMPLETED!")
