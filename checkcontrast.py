"""Verify every text/ground pair in the palette against WCAG AA.

The site argues for data integrity, so the palette gets checked rather than eyeballed.
Dark is the authored default; light is a supported alternate and gets the same bar.

Run:  python checkcontrast.py
Exit: 0 if every pair passes its target, 1 otherwise.
"""
import sys

# Instrument-panel dark: near-black ground, signal amber accent.
DARK = dict(
    bg="#0A0B0D", surface="#101216", raised="#16191E",
    ink="#E7E9EC", ink2="#9CA4AE", ink3="#79828D",
    rule="#2C3239", rule2="#1C2126",
    accent="#F0A244", accent_bg="#241A0D", on_accent="#0A0B0D",
)

LIGHT = dict(
    bg="#FAFAF8", surface="#FFFFFF", raised="#F1F1ED",
    ink="#14161A", ink2="#474E57", ink3="#68707A",
    rule="#D8D8CF", rule2="#E9E9E2",
    accent="#8A4A06", accent_bg="#FCF2E2", on_accent="#FFFFFF",
)

# (foreground token, background token, minimum ratio, what it is)
PAIRS = [
    ("ink", "bg", 7.0, "body text on the page ground"),
    ("ink", "surface", 7.0, "body text on a panel"),
    ("ink", "raised", 7.0, "text on a raised chip"),
    ("ink2", "bg", 4.5, "secondary text / lede"),
    ("ink2", "surface", 4.5, "secondary text on a panel"),
    ("ink3", "bg", 4.5, "mono metadata rails"),
    ("ink3", "surface", 4.5, "mono metadata on a panel"),
    ("accent", "bg", 4.5, "links and labels on the ground"),
    ("accent", "surface", 4.5, "links and labels on a panel"),
    ("accent", "raised", 4.5, "labels on a chip"),
    ("ink", "accent_bg", 4.5, "text inside a callout"),
    ("accent", "accent_bg", 4.5, "accent text inside a callout"),
    ("on_accent", "accent", 4.5, "label on the filled primary button"),
]

# Non-text boundaries still need to be visible (WCAG 1.4.11 asks 3:1 for controls;
# hairline rules are decorative separators, so the bar here is just "perceptible").
UI_PAIRS = [("rule", "bg", 1.35, "hairline rules on the ground"),
            ("rule", "surface", 1.35, "panel borders"),
            ("accent", "bg", 3.0, "focus ring / filled button ground")]


def srgb(c):
    c = c / 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def lum(hexstr):
    h = hexstr.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * srgb(r) + 0.7152 * srgb(g) + 0.0722 * srgb(b)


def ratio(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def check(name, pal):
    print(f"\n{name}")
    print(f"  {'pair':<24}{'ratio':>9}  {'need':>5}        what")
    ok = True
    for fg, bg, need, what in PAIRS + UI_PAIRS:
        r = ratio(pal[fg], pal[bg])
        good = r >= need
        ok &= good
        print(f"  {fg + ' on ' + bg:<24}{r:>8.2f}:1{need:>6.2f}  "
              f"{'pass' if good else 'FAIL'}  {what}")
    return ok


if __name__ == "__main__":
    a = check("DARK (authored default)", DARK)
    b = check("LIGHT (alternate)", LIGHT)
    print()
    if a and b:
        print("every pair meets its target")
        sys.exit(0)
    print("PALETTE FAILS — fix the tokens above before shipping")
    sys.exit(1)
