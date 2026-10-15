import os
import subprocess
from PIL import Image

assets_dir = r"C:\Users\0231304\.gemini\antigravity-ide\scratch\welspun_dashboard\assets"
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

# HTML templates for rendering
html_content_blue = f'''<!DOCTYPE html>
<html>
<head>
<style>
body {{
  margin: 0;
  padding: 20px;
  background: transparent;
  display: flex;
  align-items: center;
  justify-content: center;
}}
svg {{
  width: 800px;
  height: auto;
}}
</style>
</head>
<body>
{open(os.path.join(assets_dir, "welspun_full_logo.svg"), "r", encoding="utf-8").read()}
</body>
</html>'''

html_path = os.path.join(assets_dir, "temp_logo.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content_blue)

png_tmp = os.path.join(assets_dir, "temp_logo.png")

cmd = [
    edge_path,
    "--headless",
    "--disable-gpu",
    "--default-background-color=00000000",
    f"--screenshot={png_tmp}",
    "--window-size=900,300",
    f"file:///{html_path.replace(os.sep, '/')}"
]

res = subprocess.run(cmd, capture_output=True, text=True)
print("Edge return:", res.returncode)

if os.path.exists(png_tmp):
    # Crop and save as welspun_full_logo.png
    im = Image.open(png_tmp)
    # Find bounding box of non-transparent pixels
    bbox = im.getbbox()
    if bbox:
        # Add a tiny padding
        pad = 10
        w, h = im.size
        box = (max(0, bbox[0]-pad), max(0, bbox[1]-pad), min(w, bbox[2]+pad), min(h, bbox[3]+pad))
        cropped = im.crop(box)
        cropped.save(os.path.join(assets_dir, "welspun_full_logo.png"))
        print("welspun_full_logo.png saved!", cropped.size)

# Now do the same for dark mode logo
html_content_white = f'''<!DOCTYPE html>
<html>
<head>
<style>
body {{
  margin: 0;
  padding: 20px;
  background: transparent;
  display: flex;
  align-items: center;
  justify-content: center;
}}
svg {{
  width: 800px;
  height: auto;
}}
</style>
</head>
<body>
{open(os.path.join(assets_dir, "welspun_full_logo_dark.svg"), "r", encoding="utf-8").read()}
</body>
</html>'''

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content_white)

cmd[4] = f"--screenshot={png_tmp}"
subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(png_tmp):
    im = Image.open(png_tmp)
    bbox = im.getbbox()
    if bbox:
        pad = 10
        w, h = im.size
        box = (max(0, bbox[0]-pad), max(0, bbox[1]-pad), min(w, bbox[2]+pad), min(h, bbox[3]+pad))
        cropped = im.crop(box)
        cropped.save(os.path.join(assets_dir, "welspun_full_logo_dark.png"))
        print("welspun_full_logo_dark.png saved!", cropped.size)

# Clean up
if os.path.exists(html_path):
    os.remove(html_path)
if os.path.exists(png_tmp):
    os.remove(png_tmp)
