# ASD — scroll-cinematic asset brief

## Status: all 6 scenes are live

Every scene now has a real desktop clip, and 5 of 6 have a true native 9:16 portrait
mobile clip (Cotton, Weave, Stitch, Look Book, Commission — all portrait-rendered;
Shirt's mobile clip is also portrait). Posters are extracted frames from each clip
(chosen for best exposure/composition, not always literal frame 0 — see notes below).

| Scene | Desktop clip | Mobile clip | Poster source |
|---|---|---|---|
| 1. The Shirt | ✅ `assets/vid/shirt.mp4` | ✅ `assets/vid/shirt-m.mp4` (native 9:16) | frame 0 of each (clean) |
| 2. Suvin Cotton | ✅ `assets/vid/cotton.mp4` | ✅ `assets/vid/cotton-m.mp4` (native 9:16) | mid-clip frame (see note) |
| 3. The Weave | ✅ `assets/vid/weave.mp4` | ✅ `assets/vid/weave-m.mp4` (native 9:16, re-rendered) | frame 0 of each |
| 4. The Stitch | ✅ `assets/vid/stitch.mp4` | ✅ `assets/vid/stitch-m.mp4` (native 9:16) | frame 0 of each |
| 5. The Look Book | ✅ `assets/vid/lookbook.mp4` | ✅ `assets/vid/lookbook-m.mp4` (native 9:16) | frame 0 of each |
| 6. Commission | ✅ `assets/vid/finale.mp4` | ✅ `assets/vid/finale-m.mp4` (native 9:16) | frame 0 of each — **see quality flag below** |

Regenerate all posters any time a source frame changes: `python3 work/build_assets.py`
(reads `work/poster_<scene>[-m].png`, writes `assets/<scene>[-m].webp`).

## ⚠️ Quality flag: Commission (finale) clip has burned-in text

`dive-finale.mp4` / `dive-finale-m.mp4` carry a persistent "vintage film" overlay for
their **entire duration** (not just the first frame): sprocket-hole corner marks, a
vertical **"SUVUN"** watermark, a **"35"** frame counter, and a woven collar tag reading
**"SUVIN"** — inconsistent spelling between the two, reads like a rendering artifact
rather than intentional branding. This directly contradicts the "no text, no letters, no
logos" instruction in `dive_finale.txt`. It's baked into the pixels, so nothing on the
site side can remove it (cropping would cut into the shirt itself, which sits close to
those edges).

It's shipped as-is because you asked to rebuild with what's available, but this is the
**hero/CTA scene** — worth a re-render before this goes to real traffic. If you regenerate
it, the same prompt file (`dive_finale.txt` / `dive_finale-m.txt`) is still here; just
make sure whatever tool you use isn't applying a "film camera" style preset on top of
the request.

## Seam continuity (informational, not blocking)

These clips were rendered independently, not as a frame-locked architecture-A chain, so
scene-to-scene transitions are soft crossfades/cuts rather than a continuous glide —
expected given how they were produced, not a bug. If you ever want true seamless
handoffs between two adjacent scenes, extract the earlier clip's last frame and use it
as the later clip's start-image, then re-render the later one.

## Reference

- `style-preamble.txt` — the shared visual-style text reused across all prompts.
- `dive_<scene>[.txt / -m.txt]` — the original prompt for each scene's desktop/mobile leg.
- `poster_<scene>[.png / -m.png]` — the exact frame chosen as each scene's site poster.
- `build_assets.py` — regenerates `assets/*.webp` posters from the `poster_*.png` files.
- Encoding used for all clips: desktop = native res, crf 20, GOP 8, no audio, faststart;
  mobile = scale to 720 wide, GOP 4, crf 23, no audio, faststart.
