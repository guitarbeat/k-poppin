# TODO

## High priority
- [ ] Replace social share images with a real card and update meta tags in `index.html`
  - Add `social-card.png` (1200×630) to repo
  - Update `og:image`, `twitter:image`, and optionally `og:image:width/height`
- [x] Serve favicon locally (done)
- [ ] Add PWA basics
  - [ ] `site.webmanifest` with name, icons (192/512), start_url `/`, display `standalone`
  - [ ] `<meta name="theme-color">` in `index.html`
- [ ] Performance/network hints
  - [ ] `<link rel="preconnect" href="https://w.soundcloud.com" crossorigin>`
  - [ ] `<link rel="preconnect" href="https://api.soundcloud.com" crossorigin>`
- [ ] Basic SEO
  - [ ] `<link rel="canonical" href="https://kpop.alw.lol/">`
  - [ ] `robots.txt` and `sitemap.xml`
- [ ] Privacy/Analytics
  - [ ] Add GA4 consent mode defaults or remove GA if not needed
  - [ ] Respect DNT (do-not-track)
- [ ] `<noscript>` fallback message (JS-required)

## UX & accessibility
- [ ] Ensure play/pause/skip are keyboard accessible with visible focus
- [ ] Add ARIA live region to announce guess results and game end
- [ ] Check color contrast in `style/bundle.css`; adjust variables if needed
- [ ] Honor reduced motion preferences for any animations

## Game logic
- [ ] Use UTC midnight for the daily seed to avoid timezone surprises
- [ ] Show a countdown to next round
- [ ] Persist and check last played day in `localStorage` to avoid unexpected reloads

## Sharing
- [ ] Add Web Share API on mobile; copy-to-clipboard on desktop with success toast
- [ ] Verify copied link points to your domain

## Performance
- [ ] Lazy-load the SoundCloud widget after first interaction to improve TTI
- [ ] Consider preconnecting/preloading only when the player becomes visible

## Data & tools
- [ ] Improve validator `scripts/validate_songs.py`
  - [ ] Detect unreachable/private SoundCloud URLs (HEAD request optional)
  - [ ] Enforce `Artist - Title` pattern and leading space rule for numeric starts
- [ ] Optional: script to move a completed day’s song from `data/songs.js` to `data/songs.archive.js`

## CI
- [ ] Add a scheduled workflow (e.g., weekly) to run validation
- [ ] Require "Validate songs list" check on PRs to `main`

## Docs
- [ ] Add a short screenshot/gif of gameplay and sharing results
- [ ] Expand "How to add a song" with a tiny example PR in `README.md`

## Pointers
- Songs list: `data/songs.js`
- Validator: `scripts/validate_songs.py`
- Entry point: `index.html`