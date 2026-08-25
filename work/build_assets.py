#!/usr/bin/env python3
"""One-off asset build: convert delivered stills/frames to site webp posters.
Re-run any time new poster_*.png source frames are added/replaced."""
import os
from PIL import Image

WORK = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.normpath(os.path.join(WORK, "..", "assets"))

# (source frame in work/, output filename in assets/, max width)
POSTERS = [
    ("poster_shirt.png",    "shirt.webp",    1920),
    ("poster_shirt-m.png",  "shirt-m.webp",  1080),
    ("poster_cotton.png",   "cotton.webp",   1920),
    ("poster_cotton-m.png", "cotton-m.webp", 1080),
    ("poster_weave.png",    "weave.webp",    1920),
    ("poster_weave-m.png",  "weave-m.webp",  1080),
    ("poster_stitch.png",   "stitch.webp",   1920),
    ("poster_stitch-m.png", "stitch-m.webp", 1080),
    ("poster_lookbook.png",   "lookbook.webp",   1920),
    ("poster_lookbook-m.png", "lookbook-m.webp", 1080),
    ("poster_finale.png",   "finale.webp",   1920),
    ("poster_finale-m.png", "finale-m.webp", 1080),
]


def resize_max_width(im, max_w):
    if im.width <= max_w:
        return im
    h = round(im.height * (max_w / im.width))
    return im.resize((max_w, h), Image.LANCZOS)


def save_webp(im, path, quality=86):
    im.convert("RGB").save(path, "WEBP", quality=quality, method=6)
    print("wrote", os.path.relpath(path, os.path.dirname(WORK)))


if __name__ == "__main__":
    os.makedirs(ASSETS, exist_ok=True)
    for src, out, max_w in POSTERS:
        src_path = os.path.join(WORK, src)
        if not os.path.exists(src_path):
            print("skip (missing):", src)
            continue
        im = Image.open(src_path)
        im = resize_max_width(im, max_w)
        save_webp(im, os.path.join(ASSETS, out))
    print("done")
