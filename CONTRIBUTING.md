# Contributing

Thanks for helping grow K‑Pop Girl Group Heardle! This guide is designed for non‑developers and friends collaborating on the song list.

## The one thing that powers the game
- The game reads its daily songs from `music-stuff/songs.js`.
- Each entry looks like this:
  ```js
  {
    url: "https://soundcloud.com/artist/track",
    answer: "ARTIST - Track Title"
  }
  ```
- Tip: If the answer starts with a number, add a leading space to work around an autocomplete quirk, e.g. `" 2NE1 - I Am the Best"`.

## Easiest way to add songs
1. Open `music-stuff/songs.js`.
2. Scroll to the bottom and add a new object with both `url` and `answer`.
3. Keep the exact casing/spacing of the artist/title as you want it shown in results.
4. Save.
5. Run the validator locally (optional) or open a PR.

## Optional: Run checks locally
If you have Python 3 installed:
```bash
python music-stuff/tools/validate_songs.py
```
This checks for:
- Duplicate URLs or answers
- Missing fields
- Leading‑number answers missing a leading space

## Pull requests
- Use the PR template checklist that will appear when you open a PR.
- The CI will automatically run validation on your changes.
- A maintainer will merge once the checks pass.

## Song requests
- If you don’t want to edit files yourself, open a “Song request” issue (template provided). Include the SoundCloud link and the display text.

## Style notes
- Keep lines wrapped reasonably in Markdown files.
- Do not reformat `main.js` or other compiled assets.

## What NOT to change
- Do not rename or move `index.html`, `main.js`, or `music-stuff/songs.js` (the site depends on these paths).
- Do not remove Google Analytics without discussing (you can disable locally).

Thank you! 💜