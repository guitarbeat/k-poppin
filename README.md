# K-Pop Girl Group Heardle with Spotify Integration

An Artist Heardle game customized for K-Pop Girl Group songs, with tools to automatically import songs from Spotify playlists via the SoundCloud API.

## Project Structure

The project has been simplified into the following streamlined structure:

```
artist-heardle/
├── src/                        # Source files for the Heardle game
│   ├── bundle.css              # Bundled CSS
│   ├── global.css              # Global CSS
│   ├── index.html              # Main HTML file
│   ├── main.js                 # Main JavaScript
│   └── songs.js                # Songs database
│
├── scripts/                    # Python scripts for integration
│   ├── spotify_to_heardle.py   # All-in-one script
│   └── requirements.txt        # Python dependencies
│
├── docs.md                     # Comprehensive project documentation
├── .glitch-assets              # Glitch configuration
├── [Symlinks to key files]     # For backward compatibility
└── README.md                   # This file
```

## Getting Started

### Quick Start

To import songs from a Spotify playlist to your Heardle game:

1. Install required packages:
   ```
   pip install -r requirements.txt
   ```

2. Run the main script:
   ```
   python spotify_to_heardle.py
   ```

3. Follow the interactive prompts to:
   - Extract songs from Spotify
   - Search for them on SoundCloud
   - Update your Heardle game

### Prerequisites

- Python 3.6 or higher
- Spotify API credentials (Client ID and Secret)
- SoundCloud API Client ID

## Documentation

For detailed information about the project, refer to the `docs.md` file.

## Customizing the Game

After updating the songs, you can customize:
- Game appearance in `src/bundle.css`
- Game title and description in `src/index.html`
- Game messages in `src/main.js`

## Original Project

This is a fork/remix of the original K-Pop Girl Group Heardle. The code was remixed from ZAYN Heardle and Taylor Swift Heardle projects. 