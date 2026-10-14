import subprocess
from pathlib import Path

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
html_path = Path(r"c:\Users\Rishabh Bansal\Downloads\Parali setu\docs\diagrams\xyflow_architecture.html").resolve()
output_img = Path(r"c:\Users\Rishabh Bansal\Downloads\Parali setu\docs\diagrams\xyflow_arch_shot.png").resolve()

cmd = [
    edge_path,
    "--headless=new",
    "--disable-gpu",
    f"--screenshot={output_img}",
    "--window-size=1420,480",
    html_path.as_uri()
]

print("Running command:", " ".join(cmd))
res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
print("Return code:", res.returncode)
print("Stderr:", res.stderr)
print("Output exists:", output_img.exists())
if output_img.exists():
    print("File size:", output_img.stat().st_size)
