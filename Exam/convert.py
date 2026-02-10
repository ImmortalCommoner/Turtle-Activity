import subprocess
import os
from PIL import Image, ImageOps

svg_file = r"Z:\outline.svg"
png_file = r"Z:\outline.png"

# Convert SVG to PNG using Inkscape
subprocess.run([
    "inkscape", svg_file,
    "--export-type=png",
    "--export-filename", png_file
])

# Load PNG with Pillow
base = Image.open(png_file).convert("RGBA")

# Generate rotated + animated GIFs
for i in range(8):
    angle = i * 45
    rotated = base.rotate(angle, expand=True)

    for f in [2, 3]:
        frame = rotated.copy()
        if f == 3:
            frame = ImageOps.mirror(frame)

        filename = os.path.join("Z:\\", f"{i}_{f}.gif")
        frame.save(filename, format="GIF")
        print("Saved:", filename)

print("✅ All sprite GIFs generated successfully!")