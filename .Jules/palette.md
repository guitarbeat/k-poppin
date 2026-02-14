## 2024-01-01 - [Modal Close Accessibility]

**Learning:** The application uses minified Svelte components where modal close buttons lack accessible labels.
**Action:** Manually patch `main.js` to inject `aria-label` attributes using the internal `M` helper function.

## 2024-05-21 - [Patching Minified Svelte for A11y]

**Learning:** Even without source code, minified Svelte components (using `ie`/`oe` patterns) can be patched to accept new props like `aria-label` by modifying the internal state management and attribute setting logic.
**Action:** When working with legacy/bundled Svelte apps, look for the `$$set` logic in the component factory function to inject new accessibility properties.

## 2025-05-21 - [Search Input Accessibility]

**Learning:** The autocomplete search input (autoComplete.js) relies on a placeholder and lacks an associated `<label>` or `aria-label`, making it inaccessible to screen readers.
**Action:** Patched the `Dt` function in `main.js` and `bg/main.js` to explicitly add `aria-label="Search for the song title"` to the input element (variable `c`).

## 2025-05-21 - [Reactive Progress Bar Accessibility]

**Learning:** The custom progress bar uses `style.width` for visual updates but lacks semantic ARIA attributes (`role="progressbar"`, `aria-valuenow`).
**Action:** Patched both the `c()` (creation) method to add static ARIA attributes and the `p()` (update) method to reactively update `aria-valuenow` based on the internal state variable `e[10]`.

## 2025-05-21 - [Toast Accessibility]

**Learning:** Dynamic "toast" messages (like "Copied to clipboard!") implemented as simple divs are not announced by screen readers.
**Action:** Patched the `cn` function in `main.js` and `bg/main.js` to explicitly add `role="status"` (which implies `aria-live="polite"`) to the message container.

## 2025-05-21 - [Button Name Calculation]

**Learning:** The reusable button component defaulted to `label=""`, causing it to render `aria-label=""` even when content was present (like "Share" or "Play"), effectively silencing the button name for screen readers.
**Action:** Patched the `oe` component factory in `main.js` and `bg/main.js` to default `label` to `null` instead of `""`, allowing the internal `M` helper to correctly remove the `aria-label` attribute when no label is provided.

## 2025-10-24 - [Updating Dynamic Button Labels in Minified Svelte]

**Learning:** To make the "Skip" button accessible with dynamic content (time penalty), I patched the `ae` component instantiation and its update (`p`) function in the minified `main.js`. Since `main.js` is the only source, direct patching is required.
**Action:** When updating component props in this codebase, ensure both the initial `new Component({ props: ... })` and the reactive `$set` call in the `p` function are updated to handle dynamic values from the context (`e`).
