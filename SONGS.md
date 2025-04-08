## A simple way to get songs from Soundcloud (Tracks, Playlists, or Albums)

1. Go to the playlist/album page on soundcloud

2. Keep scrolling to make sure all the tracks are loaded

3. Run this in your browser's developer tools console  
(press F12 or similar and go to the `console` tab)

```javascript
let songs = [];
// Wait for page load and try multiple selectors
setTimeout(() => {
    // Try different selectors for both playlists and albums
    const items = document.querySelectorAll(`
        .trackList__item,
        .playableTile__mainHeading,
        [role="listitem"],
        .trackItem,
        .soundList__item,
        .trackList__track,
        .trackList__item--track
    `);
    
    items.forEach(item => {
        try {
            // Try multiple selectors for different layouts
            const titleEl = item.querySelector(`
                .trackItem__trackTitle,
                .playableTile__heading span,
                .trackItem__title,
                .soundTitle__title,
                .trackItem__trackTitle span
            `);
            
            const artistEl = item.querySelector(`
                .trackItem__username,
                .playableTile__usernameText,
                .trackItem__username span,
                .soundTitle__username,
                .trackItem__username
            `);
            
            const linkEl = item.querySelector(`
                .trackItem__trackTitle,
                .playableTile__heading,
                .trackItem__title,
                .soundTitle__title,
                a[href*="/sets/"],
                a[href*="/tracks/"]
            `);

            // Skip if we can't find all elements
            if (!titleEl || !artistEl || !linkEl) return;

            const title = titleEl.innerText.trim();
            const artist = artistEl.innerText.trim();
            
            // Get the full URL
            let url = linkEl.href || linkEl.getAttribute('href');
            if (!url.startsWith('https://soundcloud.com')) {
                url = 'https://soundcloud.com' + url;
            }
            
            // Only add if we have all the information
            if (title && artist && url) {
                songs.push({
                    url: url,
                    answer: `${artist} - ${title}`
                });
            }
        } catch (e) {
            console.log('Error processing track:', e);
        }
    });
    
    // Format the output ready for songs.js
    const output = 'const SONGS = ' + JSON.stringify(songs, null, 2) + ';';
    console.log('Copy everything between the lines below:');
    console.log('------------------------');
    console.log(output);
    console.log('------------------------');
    console.log(`Found ${songs.length} songs`);
}, 2000);  // 2 second delay to ensure page loads
```

4. Copy EVERYTHING between the lines (including the `const SONGS = ` part)

5. Create/open `songs.js` and replace its entire contents with what you copied

If you're still not getting all songs:
- Make sure to scroll all the way down in the playlist/album to load all tracks
- Try increasing the timeout (change 2000 to 5000 for 5 seconds)
- Check if any tracks are in a "Show more" section and click to expand it
- Refresh the page and wait for it to fully load before running the script
- If some tracks are still missing, try running the script multiple times as you scroll down 