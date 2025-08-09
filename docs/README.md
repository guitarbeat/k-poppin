# Music Data

This folder contains the song list used by the game and helper tools.

## Files
- `songs.js`: The live list used by the site (loaded in `index.html`).
- `previous_songs.js`: Archive of already‑used songs.
- `tools/validate_songs.py`: Quick checks for duplicates/format issues.

## Add a song
Append to `songs.js` using this shape:
```js
{
  url: "https://soundcloud.com/artist/track",
  answer: "ARTIST - Track Title"
}
```

Guidelines:
- Ensure the SoundCloud URL is publicly playable.
- The `answer` will be shown to players; use the official casing where possible.
- If the title/artist begins with a number, prefix with a single leading space, e.g. `" 2NE1 - I Am the Best"`.
- Avoid duplicates (same `url` or same `answer`).

Run local checks (optional):
```bash
python scripts/validate_songs.py
```

## Moving songs to the archive
Once a song has been used and you want to retire it, move the entry from `songs.js` to `previous_songs.js`.

## Shuffling
The GitHub Action `.github/workflows/shuffle-songs.yml` contains logic to shuffle the order when needed.