#!/usr/bin/env python3
"""One-off asset build: convert delivered stills/frames to site webp posters
and render branded 'footage in production' placeholders for scenes with no
delivered asset yet. Re-run any time new stills land."""
import os
from PIL import Image, ImageDraw, ImageFont

WORK = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.normpath(os.path.join(WORK, "..", "assets"))
FONT_SERIF = "/System/Library/Fonts/Supplemental/Georgia.ttf"
FONT_SERIF_IT = "/System/Library/Fonts/Supplemental/Georgia Italic.ttf"

BG = (10, 10, 11)          # ~ hsl(210,10%,4%), the cinematic --sw-bg
INK = (250, 250, 250)
INK_SOFT = (168, 168, 172)
ACCENT = (224, 18, 42)     # ~ hsl(356,84%,48%), --primary


def save_webp(im, path, quality=86):
    im.convert("RGB").save(path, "WEBP", quality=quality, method=6)
    print("wrote", os.path.relpath(path, os.path.dirname(WORK)))


def resize_max_width(im, max_w):
    if im.width <= max_w:
        return im
    h = round(im.height * (max_w / im.width))
    return im.resize((max_w, h), Image.LANCZOS)


def convert_still(src_name, out_name, max_w):
    im = Image.open(os.path.join(WORK, src_name))
    im = resize_max_width(im, max_w)
    save_webp(im, os.path.join(ASSETS, out_name))


def placeholder(label, eyebrow, out_name, size=(1920, 1080)):
    im = Image.new("RGB", size, BG)
    d = ImageDraw.Draw(im)
    w, h = size
    cx, cy = w // 2, h // 2

    # soft vignette
    for r in range(min(w, h) // 2, 0, -2):
        t = r / (min(w, h) / 2)
        shade = int(10 + 6 * (1 - t))
        d.ellipse([cx - r, cy - r * 0.7, cx + r, cy + r * 0.7], outline=(shade, shade, shade + 1))

    # thin red orbit ring (echoes the look-book swatch motif)
    rw, rh = w * 0.16, h * 0.30
    d.ellipse([cx - rw, cy - rh - h * 0.02, cx + rw, cy + rh - h * 0.02], outline=ACCENT, width=2)

    eyebrow_font = ImageFont.truetype(FONT_SERIF, int(h * 0.022))
    label_font = ImageFont.truetype(FONT_SERIF, int(h * 0.052))
    note_font = ImageFont.truetype(FONT_SERIF_IT, int(h * 0.02))

    def centered(text, font, y, fill, spacing=0):
        if spacing:
            text = (" " * 0).join(list(text))
            bbox = d.textbbox((0, 0), text, font=font)
            tw = bbox[2] - bbox[0]
        else:
            bbox = d.textbbox((0, 0), text, font=font)
            tw = bbox[2] - bbox[0]
        d.text((cx - tw / 2, y), text, font=font, fill=fill)

    centered(eyebrow.upper(), eyebrow_font, cy - h * 0.11, ACCENT)
    centered(label, label_font, cy - h * 0.045, INK)
    centered("Footage in production", note_font, cy + h * 0.20, INK_SOFT)

    save_webp(im, os.path.join(ASSETS, out_name))


def poster_from_frame(png_name, out_name, max_w):
    im = Image.open(os.path.join(WORK, png_name))
    im = resize_max_width(im, max_w)
    save_webp(im, os.path.join(ASSETS, out_name))


if __name__ == "__main__":
    os.makedirs(ASSETS, exist_ok=True)

    # --- real delivered assets -------------------------------------------------
    convert_still("still-shirt.png", "shirt.webp", 1920)
    convert_still("still-shirt-m.png", "shirt-m.webp", 1080)
    poster_from_frame("_qa_weave_first.png", "weave.webp", 1920)
    poster_from_frame("_qa_stitch_first.png", "stitch.webp", 1920)
    poster_from_frame("_qa_stitch_m_first.png", "stitch-m.webp", 1080)

    # --- placeholders for scenes with no delivered footage yet -----------------
    placeholder("Suvin Cotton", "1 in 38 Tons", "cotton.webp")
    placeholder("The Look Book", "Your Setting", "lookbook.webp")
    placeholder("Commission", "QuiteYou", "finale.webp")

    print("done")
