/* ASD — site chrome + lets-scroll mount */
(function () {
  // ---- theme toggle -------------------------------------------------------
  var root = document.documentElement;
  var stored = localStorage.getItem('asd-theme');
  if (stored === 'dark') root.classList.add('dark');
  document.addEventListener('click', function (e) {
    var btn = e.target.closest('[data-theme-toggle]');
    if (!btn) return;
    root.classList.toggle('dark');
    localStorage.setItem('asd-theme', root.classList.contains('dark') ? 'dark' : 'light');
  });

  // ---- header: solid once you scroll off the cinematic hero --------------
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('is-solid', window.scrollY > window.innerHeight * 0.6);
    };
    document.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // ---- mobile nav (simple slide-down) -------------------------------------
  var navToggle = document.querySelector('.nav-toggle');
  var mainNav = document.querySelector('.main-nav');
  if (navToggle && mainNav) {
    navToggle.addEventListener('click', function () {
      mainNav.classList.toggle('is-open');
    });
  }

  // ---- lets-scroll cinematic hero -----------------------------------------
  var world = document.getElementById('world');
  if (world && typeof mountLetsScroll === 'function') {
    mountLetsScroll(world, {
      brand: { name: 'ASD', href: '#top' },
      hint: 'scroll to begin',
      nav: false,
      atmosphere: true,
      diveScroll: 1.5,
      crossfade: 0.08,
      sections: [
        {
          id: 'shirt',
          label: 'The Shirt',
          still: 'assets/shirt.webp',
          stillMobile: 'assets/shirt-m.webp',
          clip: 'assets/vid/shirt.mp4',
          clipMobile: 'assets/vid/shirt-m.mp4',
          accent: '#E0122A',
          scroll: 1.7,
          linger: 0.4,
          eyebrow: 'The Only Standard',
          title: 'The only standard that matters. Yours.',
          body: 'After a certain point, choice becomes clutter. One fibre. One shirt. Made to your standard — QuiteYou.',
          tags: ['Suvin Cotton', 'Made to Measure', 'Single Fibre'],
        },
        {
          id: 'cotton',
          label: 'Suvin Cotton',
          still: 'assets/cotton.webp',
          stillMobile: 'assets/cotton-m.webp',
          clip: 'assets/vid/cotton.mp4',
          clipMobile: 'assets/vid/cotton-m.mp4',
          accent: '#E0122A',
          scroll: 1.5,
          eyebrow: '1 in 38 Tons',
          title: 'For every 38 tons of cotton grown, less than 1kg is Suvin.',
          body: 'Grown exclusively in India, finer than Giza at 2.9 micronaire — the fineness behind its natural lustre and drape.',
          tags: ['2.9 Micronaire', 'Grown in India', 'Rarer than Giza'],
        },
        {
          id: 'weave',
          label: 'The Weave',
          still: 'assets/weave.webp',
          stillMobile: 'assets/weave-m.webp',
          clip: 'assets/vid/weave.mp4',
          clipMobile: 'assets/vid/weave-m.mp4',
          accent: '#E0122A',
          scroll: 1.5,
          linger: 0.35,
          eyebrow: 'Ends & Picks',
          title: 'A proprietary fabric, constructed with engineered precision.',
          body: 'Every end and every pick interlace under exacting tension, woven into a fabric that drapes like nothing else.',
          tags: ['120/2 Yarn', 'Precision Weave', 'Natural Drape'],
        },
        {
          id: 'stitch',
          label: 'The Stitch',
          still: 'assets/stitch.webp',
          stillMobile: 'assets/stitch-m.webp',
          clip: 'assets/vid/stitch.mp4',
          clipMobile: 'assets/vid/stitch-m.mp4',
          accent: '#E0122A',
          scroll: 1.5,
          eyebrow: 'A Finite Harvest',
          title: 'An uncompromising stitch.',
          body: 'Cut to your exact measurements and stitched at 22 stitches per inch, with unfused interlinings and mother-of-pearl buttons.',
          tags: ['22 Stitches / Inch', 'Made to Measure', 'Mother-of-Pearl'],
        },
        {
          id: 'lookbook',
          label: 'The Look Book',
          still: 'assets/lookbook.webp',
          stillMobile: 'assets/lookbook-m.webp',
          clip: 'assets/vid/lookbook.mp4',
          clipMobile: 'assets/vid/lookbook-m.mp4',
          accent: '#E0122A',
          scroll: 1.4,
          eyebrow: 'Your Setting',
          title: 'Pick a curated style — or make it your own.',
          body: 'From the boardroom to the black-tie evening, six curated looks, endlessly configurable.',
          tags: ['Boardroom', 'Black Tie', 'Fully Customizable'],
        },
        {
          id: 'finale',
          label: 'Commission',
          still: 'assets/finale.webp',
          stillMobile: 'assets/finale-m.webp',
          clip: 'assets/vid/finale.mp4',
          clipMobile: 'assets/vid/finale-m.mp4',
          accent: '#E0122A',
          scroll: 1.8,
          linger: 0.5,
          eyebrow: 'QuiteYou',
          title: 'Commission your standard.',
          body: 'No two shirts are identical, because no two bodies are.',
          tags: [],
          cta: {
            primary: { label: 'Commission Your Shirt', href: 'pages/product.html' },
            secondary: { label: 'Read the Suvin Story', href: 'pages/suvin.html' },
          },
        },
      ],
      // Architecture A (continuous forward walkthrough) — the legs ARE the
      // journey; there are no aerial connectors between scenes.
      connectors: [],
      connectorsMobile: [],
    });
  }
})();
