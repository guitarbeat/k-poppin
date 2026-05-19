## 2026-05-19 - [Performance Optimization: Preload Critical JSON Data]

**Learning:** The application fetches `data/songs.json` inside `main.js`, which is deferred. This causes a waterfall: HTML loads -> main.js loads -> main.js executes -> songs.json is requested.
**Action:** Adding `<link rel="preload" href="data/songs.json" as="fetch" crossorigin="anonymous" />` to `index.html` and `bg/index.html` initiates the download of this critical data alongside the initial HTML parsing, reducing the time to first interactive state.
