#!/usr/bin/env python3
import re
import json

# ============= CONFIGURATION SECTION =============
# Edit these values to customize your Heardle game

# App name (used throughout the app)
APP_NAME = "kpop-girl-heardle"
APP_DISPLAY_NAME = "K-Pop Girl Heardle 💝 🎤"  # How it appears to users

# Game configuration
GLITCH_NAME = "kpop-girl-heardle"
GAME_URL = f"https://{GLITCH_NAME}.glitch.me/"
ARTIST_NAME = "K-Pop Girl Groups"
GAME_NAME = f"{ARTIST_NAME} Heardle 💖"
START_DATE = "2024-03-20"  # Today's date

# Game comments (7 required)
GAME_COMMENTS = [
    "아이고! (Aigo!) 😭",  # FAILED
    "완벽해! (Perfect!) 💫",  # First try
    "대단해! (Amazing!) ⭐",
    "멋있어! (Cool!) 💝",
    "잘했어! (Well done!) 💕",
    "좋아요! (Good!) 💗",
    "괜찮아요! (Not bad!) 💓"  # Sixth try
]

# Google Analytics ID (leave empty if you don't want to use GA)
GOOGLE_ANALYTICS_ID = ""

# Your favicon/icon URL
NEW_FAVICON_URL = "https://cdn.glitch.global/70e7d90a-86fa-4c52-8f03-1310353a5651/favicon.png?v=1657371906066"

# Color scheme (HEX colors)
COLORS = {
    "primary": "#FF1493",       # Hot pink - main accent color
    "secondary": "#FF69B4",     # Light pink - secondary accent
    "background": "#000000",    # Black background
    "text": "#FFFFFF",          # White text
    "positive": "#FF69B4",      # Submit button - light pink
    "negative": "#FF1493",      # Incorrect answer - hot pink
    "foreground": "#FFFFFF",    # Font color and accents
    "midground": "#333333",     # Skip button, progress bar
    "line": "#FF69B4",          # Line color for current guess box
    "playback-bar": "#272b46"   # Playback bar color
}

# ===============================================

def update_app_name():
    """Update app name in index.html and main.js"""
    # Update index.html
    with open('index.html', 'r') as file:
        content = file.read()
    
    content = re.sub(r'<title>.*?</title>', f'<title>{GAME_NAME}</title>', content)
    content = re.sub(r'content="Guess the Harry Styles song', f'content="Guess the {ARTIST_NAME} song', content)
    
    with open('index.html', 'w') as file:
        file.write(content)
    
    # Update main.js
    with open('main.js', 'r') as file:
        content = file.read()
    
    # Update all configuration values
    content = re.sub(r'HEARDLE_GLITCH_NAME\s*=\s*".*?"', f'HEARDLE_GLITCH_NAME = "{GLITCH_NAME}"', content)
    content = re.sub(r'HEARDLE_URL\s*=\s*".*?"', f'HEARDLE_URL = "{GAME_URL}"', content)
    content = re.sub(r'HEARDLE_ARTIST\s*=\s*".*?"', f'HEARDLE_ARTIST = "{ARTIST_NAME}"', content)
    content = re.sub(r'HEARDLE_NAME\s*=\s*".*?"', f'HEARDLE_NAME = "{GAME_NAME}"', content)
    content = re.sub(r'HEARDLE_START_DATE\s*=\s*".*?"', f'HEARDLE_START_DATE = "{START_DATE}"', content)
    
    # Update game comments
    comments_str = ',\n      '.join([f'"{comment}"' for comment in GAME_COMMENTS])
    content = re.sub(r'const HEARDLE_GAME_COMMENTS = \[.*?\];', 
                    f'const HEARDLE_GAME_COMMENTS = [\n      {comments_str}\n    ];', 
                    content, 
                    flags=re.DOTALL)
    
    with open('main.js', 'w') as file:
        file.write(content)

def update_google_analytics():
    """Update or remove Google Analytics based on configuration"""
    with open('index.html', 'r') as file:
        content = file.read()
    
    if GOOGLE_ANALYTICS_ID:
        # Add Google Analytics if ID is provided
        ga_script = f'''
        <!-- Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id={GOOGLE_ANALYTICS_ID}"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){{dataLayer.push(arguments);}}
            gtag('js', new Date());
            gtag('config', '{GOOGLE_ANALYTICS_ID}');
        </script>
        '''
        # Insert GA script before </head>
        content = content.replace('</head>', f'{ga_script}\n</head>')
    else:
        # Remove existing GA script if any
        content = re.sub(r'<!-- Google Analytics -->.*?</script>\n', '', content, flags=re.DOTALL)
    
    with open('index.html', 'w') as file:
        file.write(content)

def update_favicon():
    """Update favicon URL in index.html"""
    if not NEW_FAVICON_URL:
        print("No new favicon URL provided, skipping favicon update")
        return

    with open('index.html', 'r') as file:
        content = file.read()
    
    # Replace all instances of the old favicon URL
    old_favicon_pattern = r'https://cdn\.glitch\.global/[^"]+/favicon\.png\?[^"]*'
    content = re.sub(old_favicon_pattern, NEW_FAVICON_URL, content)
    
    with open('index.html', 'w') as file:
        file.write(content)

def update_colors():
    """Update color scheme in stylesheet.css"""
    with open('stylesheet.css', 'r') as file:
        content = file.read()
    
    # Update all color variables
    content = re.sub(r'--color-primary:\s*#[0-9a-fA-F]{6}', f'--color-primary: {COLORS["primary"]}', content)
    content = re.sub(r'--color-secondary:\s*#[0-9a-fA-F]{6}', f'--color-secondary: {COLORS["secondary"]}', content)
    content = re.sub(r'--color-background:\s*#[0-9a-fA-F]{6}', f'--color-background: {COLORS["background"]}', content)
    content = re.sub(r'--color-text:\s*#[0-9a-fA-F]{6}', f'--color-text: {COLORS["text"]}', content)
    content = re.sub(r'--color-positive:\s*#[0-9a-fA-F]{6}', f'--color-positive: {COLORS["positive"]}', content)
    content = re.sub(r'--color-negative:\s*#[0-9a-fA-F]{6}', f'--color-negative: {COLORS["negative"]}', content)
    content = re.sub(r'--color-fg:\s*#[0-9a-fA-F]{6}', f'--color-fg: {COLORS["foreground"]}', content)
    content = re.sub(r'--color-mg:\s*#[0-9a-fA-F]{6}', f'--color-mg: {COLORS["midground"]}', content)
    content = re.sub(r'--color-bg:\s*#[0-9a-fA-F]{6}', f'--color-bg: {COLORS["background"]}', content)
    content = re.sub(r'--color-line:\s*#[0-9a-fA-F]{6}', f'--color-line: {COLORS["line"]}', content)
    content = re.sub(r'--color-playback-bar:\s*#[0-9a-fA-F]{6}', f'--color-playback-bar: {COLORS["playback-bar"]}', content)
    
    with open('stylesheet.css', 'w') as file:
        file.write(content)

def update_html_content():
    """Update HTML content with K-pop theme and Dilara's name"""
    with open('index.html', 'r') as file:
        content = file.read()
    
    # Update CSS references to use stylesheet.css
    content = re.sub(r'<link rel="stylesheet" href="global\.css">\s*<link rel="stylesheet" href="bundle\.css">', 
                    '<link rel="stylesheet" href="stylesheet.css">', 
                    content)
    content = re.sub(r'<link rel="stylesheet" href="bundle\.css">', 
                    '<link rel="stylesheet" href="stylesheet.css">', 
                    content)
    
    # Update meta tags and content
    content = re.sub(r'<title>.*?</title>', f'<title>{APP_DISPLAY_NAME}</title>', content)
    
    # Update all Harry Styles references
    content = re.sub(r'Harry Styles', ARTIST_NAME, content, flags=re.IGNORECASE)
    
    # Update meta descriptions
    meta_description = f'Guess the {ARTIST_NAME} song from the intro in as few tries as possible.'
    content = re.sub(r'<meta name="description" content=".*?"', 
                    f'<meta name="description" content="{meta_description}"', content)
    content = re.sub(r'<meta itemprop="description" content=".*?"', 
                    f'<meta itemprop="description" content="{meta_description}"', content)
    content = re.sub(r'<meta property="og:description" content=".*?"', 
                    f'<meta property="og:description" content="{meta_description}"', content)
    content = re.sub(r'<meta name="twitter:description" content=".*?"', 
                    f'<meta name="twitter:description" content="{meta_description}"', content)
    
    # Update titles
    content = re.sub(r'<meta itemprop="name" content=".*?"', 
                    f'<meta itemprop="name" content="{GAME_NAME}"', content)
    content = re.sub(r'<meta property="og:title" content=".*?"', 
                    f'<meta property="og:title" content="{GAME_NAME}"', content)
    content = re.sub(r'<meta name="twitter:title" content=".*?"', 
                    f'<meta name="twitter:title" content="{GAME_NAME}"', content)
    
    # Update images
    if NEW_FAVICON_URL:
        content = re.sub(r'<meta itemprop="image" content=".*?"', 
                        f'<meta itemprop="image" content="{NEW_FAVICON_URL}"', content)
        content = re.sub(r'<meta property="og:image" content=".*?"', 
                        f'<meta property="og:image" content="{NEW_FAVICON_URL}"', content)
        content = re.sub(r'<meta name="twitter:image" content=".*?"', 
                        f'<meta name="twitter:image" content="{NEW_FAVICON_URL}"', content)
        
        # Update favicon links
        content = re.sub(r'<link rel="icon".*?href=".*?"', 
                        f'<link rel="icon" type="image/png" href="{NEW_FAVICON_URL}"', content)
        content = re.sub(r'<link rel="icon".*?sizes="32x32".*?href=".*?"', 
                        f'<link rel="icon" type="image/png" sizes="32x32" href="{NEW_FAVICON_URL}"', content)
        content = re.sub(r'<link rel="icon".*?sizes="16x16".*?href=".*?"', 
                        f'<link rel="icon" type="image/png" sizes="16x16" href="{NEW_FAVICON_URL}"', content)
        content = re.sub(r'<link rel="apple-touch-icon".*?href=".*?"', 
                        f'<link rel="apple-touch-icon" sizes="180x180" href="{NEW_FAVICON_URL}"', content)
        content = re.sub(r'<link rel="shortcut icon".*?href=".*?"', 
                        f'<link rel="shortcut icon" href="{NEW_FAVICON_URL}"', content)
    
    # Ensure body content is present and correct
    body_content = '''  <body>
    <div id="app">
      <div class="game-container">
        <div class="header">
          <h1>Girl Group Heardle</h1>
          <p>Guess the K-pop girl group song in as few seconds as possible!</p>
        </div>
        
        <div class="game-area">
          <div class="player-container">
            <div class="player">
              <div class="waveform"></div>
              <div class="controls">
                <button class="play-button">▶</button>
                <div class="progress-bar">
                  <div class="progress"></div>
                </div>
              </div>
            </div>
          </div>
          
          <div class="input-container">
            <input type="text" class="song-input" placeholder="Type a song name..." />
            <button class="submit-button">Submit</button>
            <button class="skip-button">Skip</button>
          </div>
          
          <div class="guesses">
            <!-- Guesses will be added here by JavaScript -->
          </div>
        </div>
        
        <div class="footer">
          <p>Made for Dilara with love! 💖</p>
          <p>New song every day!</p>
        </div>
      </div>
    </div>
  </body>'''
    
    # Replace empty body or update existing body content
    if '<body></body>' in content:
        content = content.replace('<body></body>', body_content)
    else:
        content = re.sub(r'<body>.*?</body>', body_content, content, flags=re.DOTALL)
    
    with open('index.html', 'w') as file:
        file.write(content)

def ensure_css_imports():
    """Ensure the CSS has the proper font imports"""
    with open('stylesheet.css', 'r') as file:
        content = file.read()
    
    # Check if font import exists
    if '@import url("https://fonts.googleapis.com/css2' not in content:
        # Add font import at the top of the file
        font_import = '@import url("https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;700&family=Noto+Serif+Display:wght@600&display=swap");\n\n'
        content = font_import + content
    
    with open('stylesheet.css', 'w') as file:
        file.write(content)

def main():
    """Main function to run all customizations"""
    print("Starting Heardle customization...")
    
    try:
        print(f"Updating app name to {APP_DISPLAY_NAME}...")
        update_app_name()
        
        print("Updating Google Analytics configuration...")
        update_google_analytics()
        
        print("Updating favicon...")
        update_favicon()
        
        print("Ensuring CSS imports...")
        ensure_css_imports()
        
        print("Updating color scheme...")
        update_colors()
        
        print("Updating HTML content...")
        update_html_content()
        
        print("\nCustomization completed successfully!")
        print(f"Your K-pop Girl Groups Heardle game for Dilara is ready!")
        print(f"To deploy your game:")
        print(f"1. Upload these files to Glitch")
        print(f"2. Your game will be available at: {GAME_URL}")
        
    except Exception as e:
        print(f"\nError during customization: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    main() 