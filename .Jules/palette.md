## 2024-05-23 - Accessibility in Bundled Svelte

**Learning:** Svelte's bundled `main.js` contains a `$$set` method in component factories (like `oe`) that maps properties to array indices. Adding a new prop (like `label`) requires:
1. Adding it to the props destructuring in `oe`.
2. Adding a mapping in `$$set` (assigning a new index, e.g., 5).
3. Returning it in the props array.
4. Using that index in the render function (`ie`), respecting the dirty bitmask (2^5 = 32) for updates.

**Action:** When reverse-engineering Svelte bundles for accessibility, trace the `$$set` function to understand prop-to-state mapping before adding new ARIA attributes.
