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

## 2025-05-21 - [Interactive Elements must be Buttons]
**Learning:** Found a clickable `div` used for "Clear search" action. This breaks keyboard accessibility (no tab focus, no Enter/Space activation).
**Action:** Converted `div` to `button`, added `type="button"`, `aria-label`, and reset styles (`bg-transparent`, `border-none`) to match the original design while enabling standard button behavior.
