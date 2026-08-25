# ASD — website

A static, framework-free site for **ASD**, a made-to-measure shirt brand built on a
single material: ultra-rare Indian Suvin cotton, ASD's proprietary 120/2 fabric. Built
with the `lets-scroll` skill's scroll-cinematic engine for the hero, plus standard
content pages for everything else.

## What's live now

- `index.html` — the scroll-cinematic hero (6 scenes, architecture A / continuous
  forward walkthrough, all with real footage — desktop + native 9:16 mobile) + the full
  Look Book grid + closing CTA + footer.
- `pages/suvin.html` — the Suvin cotton article.
- `pages/faq.html` — the FAQ from the brief, as an accordion.
- `pages/product.html` — a configurator **UI scaffold** (collar/cuff/placket/fit
  swatches, sizing method, look pre-select via `?look=`). Not wired to pricing,
  inventory or a real preview yet.
- `pages/checkout.html` — an order-summary/shipping **UI scaffold**. Not wired to
  payments yet.
- `pages/login.html` — a sign-in **UI scaffold**. Not wired to auth yet.
- `css/theme.css` — your design tokens, verbatim.
- `css/site.css` — everything else (typography, header/footer, cards, forms).
- `js/scrub-engine.js` — the unmodified `lets-scroll` engine.
- `js/site.js` — theme toggle, header behaviour, and the `mountLetsScroll(...)`
  config for the 6 scenes.

Open `index.html` directly, or serve the folder (`python3 -m http.server`) — no build
step.

## Hero footage status

All 6 scenes are live with real clips, desktop and native 9:16 portrait mobile. One
thing to know before this goes to real traffic:

- **⚠️ The Commission (finale) clip has burned-in text/artifacts** — a "vintage film"
  overlay (sprocket marks, a "SUVUN" watermark, a "35" frame counter) and a woven tag
  reading "SUVIN" run through the *entire* clip, contradicting the "no text/logos"
  brief and reading as an unintended render artifact rather than branding. It's baked
  into the pixels, so it can't be fixed on the site side — full detail and the original
  prompt file are in `work/ASSET-BRIEF.md`. Worth a re-render since this is the hero/CTA
  scene.
- Scene-to-scene transitions are soft crossfades rather than a fully seamless glide —
  the clips were rendered independently, not as a frame-locked chain. Expected given how
  they were produced; see `work/ASSET-BRIEF.md` if you want true seamless handoffs later.

Posters are generated from the best frame of each clip via `work/build_assets.py` —
re-run it any time a `work/poster_*.png` source changes.

## Intentionally not built yet

- **Product configurator logic, pricing, cart, payments, real auth.** Sections 6 and 7
  of the brief ("Product Selection happens here interactively" / checkout) are UI
  scaffolds only — deliberately, since wiring them needs your sizing tool, catalog and
  payment provider, none of which were specified.
- **An "About Us" page.** The brief itself flagged this as undecided ("Do we really
  need it?"); I left it out rather than guess at content. Easy to add once you decide.
- **Look Book photography.** The 6 look cards on `index.html` use styled placeholder
  swatches (no photos supplied/generated for this build) — swap `.look-swatch` for real
  imagery whenever you have it.

## Brand-name note

The source brief was written for "Ends&Picks" (its wordmark and the "e's & p's" pun
behind "The Weave" section). I carried the *content* over but swapped the brand name to
**ASD** everywhere, including the wordmark, footer, and page titles — the "QuiteYou"
tagline is unrelated wordplay and was kept verbatim since you didn't ask to change it.
