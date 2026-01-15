## 2024-01-01 - [Modal Close Accessibility]
**Learning:** The application uses minified Svelte components where modal close buttons lack accessible labels.
**Action:** Manually patch `main.js` to inject `aria-label` attributes using the internal `M` helper function.

## 2024-05-21 - [Patching Minified Svelte for A11y]
**Learning:** Even without source code, minified Svelte components (using `ie`/`oe` patterns) can be patched to accept new props like `aria-label` by modifying the internal state management and attribute setting logic.
**Action:** When working with legacy/bundled Svelte apps, look for the `$$set` logic in the component factory function to inject new accessibility properties.

## 2025-05-21 - [Search Input Accessibility]
**Learning:** The autocomplete search input (autoComplete.js) relies on a placeholder and lacks an associated `<label>` or `aria-label`, making it inaccessible to screen readers.
**Action:** Patched the `Dt` function in `main.js` and `bg/main.js` to explicitly add `aria-label="Search for the song title"` to the input element (variable `c`).

## 2025-05-22 - [Empty ARIA Labels Silencing Buttons]
**Learning:** The generic button component (`ae`) defaults `aria-label` to an empty string if not provided. When used for buttons with text content (like "Play" or "Share"), this empty attribute can silence the accessible name of the button for screen readers.
**Action:** Always explicitly provide a `label` prop to `ae` components, even if the button has visible text content, to ensuring the `aria-label` matches the visible text or describes the action.
