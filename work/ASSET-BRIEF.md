# ASD — scroll-cinematic asset brief (manual render path)

**Status update:** the site now ships with whatever footage has actually been
delivered, and a branded "footage in production" placeholder poster everywhere else —
per your instruction to stop waiting on the full sequential chain and just use what's
available. The strict leg-by-leg frame-handoff process below is still the right way to
get a *seamless* forward glide across scenes that are adjacent to each other, so keep
using it for anything you want chained — but nothing is blocking on it anymore.

## Live on the site right now

| Scene | Still / poster | Desktop clip | Mobile clip | Notes |
|---|---|---|---|---|
| 1. The Shirt | ✅ `assets/shirt.webp` | — | — | Poster only; no dive video delivered yet. |
| 2. Suvin Cotton | placeholder | — | — | Nothing delivered. |
| 3. The Weave | ✅ `assets/weave.webp` (extracted frame 0) | ✅ `assets/vid/weave.mp4` | ⚠️ `assets/vid/weave-m.mp4` | See mobile note below. |
| 4. The Stitch | ✅ `assets/stitch.webp` / `assets/stitch-m.webp` | ✅ `assets/vid/stitch.mp4` | ✅ `assets/vid/stitch-m.mp4` (true native 9:16) | Fully live, desktop + mobile. |
| 5. The Look Book | placeholder | — | — | Nothing delivered. |
| 6. Commission | placeholder | — | — | Nothing delivered. |

**Mobile note on The Weave:** the delivered `dive-weave-m.mp4` was rendered landscape
(1280×720 — same as the desktop file), not portrait 9:16. Rather than ship it as a fake
"mobile" file, I encoded it as a lighter, tighter-GOP version of the *same* landscape
clip (`assets/vid/weave-m.mp4`) purely for smoother phone scrubbing — phones will see
the same framing as desktop, centre-cropped by the engine, not a native portrait shot.
If you want a true portrait Weave clip later, re-render `dive_weave-m.txt` through a
tool that actually honors the "vertical portrait composition (9:16)" clause at the top
of that prompt.

**Seam note on Weave → Stitch:** these two weren't rendered as a frame-locked pair
(Weave's last frame and Stitch's first frame land on different compositions — a loom
room vs. a tailor's bench close-up), so the engine's crossfade will read as a soft
*cut* between them rather than a continuous glide. That's expected given they were
generated independently, not chained — fine for now, but not the seamless-chain
standard the rest of this doc describes.

## Prompt files, still available for anything you want to render next

Same style preamble, same architecture-A rule (never pass an end-image; start-image =
either a fresh still, or — for a true seamless join — the *actual* last frame of the
scene immediately before it):

| Scene | Desktop prompt | Mobile (9:16) prompt |
|---|---|---|
| 1. The Shirt | `dive_shirt.txt` (start = `still-shirt.png`, delivered) | `dive_shirt-m.txt` (start = `still-shirt-m.png`, delivered) |
| 2. Suvin Cotton | `dive_cotton.txt` | `dive_cotton-m.txt` |
| 5. The Look Book | `dive_lookbook.txt` | `dive_lookbook-m.txt` |
| 6. Commission | `dive_finale.txt` | `dive_finale-m.txt` |

If you want **Scene 1 → Scene 2 → Scene 3** to eventually flow as one continuous glide
(rather than the current hard cuts in/out of placeholders), render them in order and
send each one back so I can extract its last frame as the next one's start-image — same
process as before, just optional now rather than blocking. Anything you send me for a
scene that currently shows a placeholder immediately replaces it; anything for Weave or
Stitch that's meant to *chain* off the existing clips should start from that clip's last
frame (ask and I'll pull it for you).

## When you send new files

Drop stills as `.png`/`.jpg` and clips as `.mp4` into `work/` (or tell me where they
are) named however's convenient — I'll validate (aspect/resolution/duration, frame 0
matches the intended start image), convert stills to the site's `.webp` posters, encode
clips to the site's scrub-ready format (native res, crf 20, GOP 8, no audio, faststart;
mobile 720-wide, GOP 4, crf 23), extract poster frames where needed, and wire the new
paths into `js/site.js` myself. You don't need to touch the code.
