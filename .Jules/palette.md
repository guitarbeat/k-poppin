## 2025-04-08 - Fixed invisible focus states
**Learning:** Found that `button` elements had `outline: none` and `border: none` in `global.css`, rendering focus states invisible for keyboard users.
**Action:** Replaced `button:focus` with `button:focus-visible` and added a high-contrast outline + box-shadow ring. Always check global resets for accessibility regressions.
