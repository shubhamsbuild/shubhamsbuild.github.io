"""Render the site favicon: a white "S" and the lime full stop from the
"Shubham Sharma." wordmark, on the dark surface colour.

Rendered as PNG/ICO rather than SVG text on purpose: an SVG favicon draws its
text with whatever font the visitor has, so it looks different on every
machine. One raster, drawn once at 512px and scaled down, looks the same
everywhere.

    python make_favicon.py      # writes assets/favicon.ico + apple-touch-icon.png
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / "assets"

BG = "#14181F"      # --surface (dark)
INK = "#F2F4F6"     # --ink (dark)
HL = "#DFFF00"      # --hl, the lime in the wordmark's full stop
FONT = Path("C:/Windows/Fonts/seguibl.ttf")   # Segoe UI Black

S = 512


def draw(rounded=True):
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # iOS masks the home-screen icon itself, so that one is drawn square
    if rounded:
        d.rounded_rectangle((0, 0, S - 1, S - 1), radius=112, fill=BG)
    else:
        d.rectangle((0, 0, S, S), fill=BG)

    font = ImageFont.truetype(str(FONT), 380)
    l, t, r, b = d.textbbox((0, 0), "S", font=font)
    w, h = r - l, b - t
    dot = 46                          # radius of the full stop
    gap = 14
    total = w + gap + dot * 2
    x = (S - total) / 2 - l
    y = (S - h) / 2 - t
    d.text((x, y), "S", font=font, fill=INK)
    cx = x + l + w + gap + dot
    cy = y + t + h - dot              # sits on the baseline, like a full stop
    d.ellipse((cx - dot, cy - dot, cx + dot, cy + dot), fill=HL)
    return img


def main():
    ASSETS.mkdir(exist_ok=True)
    draw().save(ASSETS / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    draw(rounded=False).resize((180, 180), Image.LANCZOS).save(
        ASSETS / "apple-touch-icon.png", optimize=True)
    draw().resize((32, 32), Image.LANCZOS).save(ASSETS / "favicon-32.png", optimize=True)
    print("wrote favicon.ico, favicon-32.png, apple-touch-icon.png")


if __name__ == "__main__":
    main()
