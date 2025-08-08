# Data

This folder contains the live song list used by the game and an archive.

- `songs.js`: Live list used by the site (loaded by `index.html`)
- `songs.archive.js`: Archive of previously used songs

Add a song by appending an object to `songs.js`:
```js
{
  url: "https://soundcloud.com/artist/track",
  answer: "ARTIST - Track Title"
}
```

Guidelines:
- Ensure the SoundCloud URL is publicly playable
- Use the final display text you want in `answer`
- If the answer starts with a number, add a leading space
- Avoid duplicates (same URL or same answer)

Validate locally:
```bash
python scripts/validate_songs.py
```