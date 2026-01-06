## 2024-01-01 - [Modal Close Accessibility]
**Learning:** The application uses minified Svelte components where modal close buttons lack accessible labels.
**Action:** Manually patch `main.js` to inject `aria-label` attributes using the internal `M` helper function.
