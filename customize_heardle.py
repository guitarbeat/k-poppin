#!/usr/bin/env python3
import re
import json

# ============= CONFIGURATION SECTION =============
# Edit these values to customize your Heardle game

# App name (used throughout the app)
APP_NAME = "kpop-heardle"
APP_DISPLAY_NAME = "K-Pop Girl Groups"  # How it appears to users

# Game configuration
GLITCH_NAME = "kpop-girlgroups-heardle"
GAME_URL = f"https://{GLITCH_NAME}.glitch.me/"
ARTIST_NAME = "K-Pop Girl Groups"
GAME_NAME = f"{ARTIST_NAME} Heardle"
START_DATE = "2024-03-20"  # Today's date

# Game comments (7 required)
GAME_COMMENTS = [
    "아이고! (Aigo!)",  # FAILED
    "완벽해! (Perfect!)",  # First try
    "대단해! (Amazing!)",
    "멋있어! (Cool!)",
    "잘했어! (Well done!)",
    "좋아요! (Good!)",
    "괜찮아요! (Not bad!)"  # Sixth try
]

# Google Analytics ID (leave empty if you don't want to use GA)
GOOGLE_ANALYTICS_ID = ""

# Your favicon/icon URL
NEW_FAVICON_URL = "https://cdn-icons-png.flaticon.com/512/2111/2111463.png"  # K-pop music icon

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
    "line": "#FF69B4"          # Line color for current guess box
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
    
    # Also update any direct color references
    content = re.sub(r'color: #333333;', f'color: {COLORS["text"]};', content)
    content = re.sub(r'background-color: #f4f4f4;', f'background-color: {COLORS["midground"]};', content)
    
    with open('stylesheet.css', 'w') as file:
        file.write(content)

def update_html_content():
    """Update HTML content with K-pop theme and Dilara's name"""
    with open('index.html', 'r') as file:
        content = file.read()
    
    # Update meta tags and content
    content = re.sub(r'<meta itemprop="name" content=".*?"', f'<meta itemprop="name" content="{GAME_NAME}"', content)
    content = re.sub(r'<meta itemprop="description" content=".*?"', f'<meta itemprop="description" content="Guess the {ARTIST_NAME} song from the intro in as few tries as possible. Made for Dilara with love! 💖"', content)
    content = re.sub(r'<meta property="og:title" content=".*?"', f'<meta property="og:title" content="{GAME_NAME}"', content)
    content = re.sub(r'<meta property="og:description" content=".*?"', f'<meta property="og:description" content="Guess the {ARTIST_NAME} song from the intro in as few tries as possible. Made for Dilara with love! 💖"', content)
    content = re.sub(r'<meta name="twitter:title" content=".*?"', f'<meta name="twitter:title" content="{GAME_NAME}"', content)
    content = re.sub(r'<meta name="twitter:description" content=".*?"', f'<meta name="twitter:description" content="Guess the {ARTIST_NAME} song from the intro in as few tries as possible. Made for Dilara with love! 💖"', content)
    
    # Update the page title
    content = re.sub(r'<title>.*?</title>', f'<title>{GAME_NAME}</title>', content)
    
    # Update favicon links
    if NEW_FAVICON_URL:
        content = re.sub(r'<link rel="icon".*?href=".*?"', f'<link rel="icon" type="image/png" href="{NEW_FAVICON_URL}"', content)
        content = re.sub(r'<link rel="icon".*?sizes="32x32".*?href=".*?"', f'<link rel="icon" type="image/png" sizes="32x32" href="{NEW_FAVICON_URL}"', content)
        content = re.sub(r'<link rel="icon".*?sizes="16x16".*?href=".*?"', f'<link rel="icon" type="image/png" sizes="16x16" href="{NEW_FAVICON_URL}"', content)
        content = re.sub(r'<link rel="apple-touch-icon".*?href=".*?"', f'<link rel="apple-touch-icon" sizes="180x180" href="{NEW_FAVICON_URL}"', content)
        content = re.sub(r'<link rel="shortcut icon".*?href=".*?"', f'<link rel="shortcut icon" href="{NEW_FAVICON_URL}"', content)
    
    # Ensure Dilara is mentioned in the footer
    if '<div class="footer">' in content:
        content = re.sub(r'<div class="footer">.*?</div>', 
                       '<div class="footer">\n    <p>Made for Dilara with love! 💖</p>\n    <p>New song every day!</p>\n  </div>', 
                       content, flags=re.DOTALL)
    
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
        print(f"Your K-pop Girl Groups Heardle game for Dilara is ready to play!")
        print(f"Visit http://localhost:3000 to preview the game locally")
        print(f"Or deploy it to Glitch at: {GAME_URL}")
        
    except Exception as e:
        print(f"\nError during customization: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    main() 