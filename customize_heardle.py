#!/usr/bin/env python3
import re
import json

# ============= CONFIGURATION SECTION =============
# Edit these values to customize your Heardle game

# App name (used throughout the app)
APP_NAME = "aarons-playlist"
APP_DISPLAY_NAME = "Aaron's Playlist"  # How it appears to users

# Google Analytics ID (leave empty if you don't want to use GA)
GOOGLE_ANALYTICS_ID = ""

# Your favicon/icon URL
NEW_FAVICON_URL = ""

# Color scheme (HEX colors)
COLORS = {
    "primary": "#FF69B4",       # Main accent color
    "secondary": "#FF1493",     # Secondary accent color
    "background": "#000000",    # Background color
    "text": "#FFFFFF"           # Text color
}

# ===============================================

def update_app_name():
    """Update app name in index.html and main.js"""
    # Update index.html
    with open('index.html', 'r') as file:
        content = file.read()
    
    content = re.sub(r'<title>.*?</title>', f'<title>{APP_DISPLAY_NAME} Heardle</title>', content)
    content = re.sub(r'content="Guess the Harry Styles song', f'content="Guess the {APP_DISPLAY_NAME} song', content)
    
    with open('index.html', 'w') as file:
        file.write(content)
    
    # Update main.js
    with open('main.js', 'r') as file:
        content = file.read()
    
    content = re.sub(r'HEARDLE_APP_NAME\s*=\s*".*?"', f'HEARDLE_APP_NAME = "{APP_NAME}"', content)
    
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
    
    # Update primary color
    content = re.sub(r'--color-primary:\s*#[0-9a-fA-F]{6}', f'--color-primary: {COLORS["primary"]}', content)
    
    # Update secondary color
    content = re.sub(r'--color-secondary:\s*#[0-9a-fA-F]{6}', f'--color-secondary: {COLORS["secondary"]}', content)
    
    # Update background color
    content = re.sub(r'--color-background:\s*#[0-9a-fA-F]{6}', f'--color-background: {COLORS["background"]}', content)
    
    # Update text color
    content = re.sub(r'--color-text:\s*#[0-9a-fA-F]{6}', f'--color-text: {COLORS["text"]}', content)
    
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
        
        print("Updating color scheme...")
        update_colors()
        
        print("\nCustomization completed successfully!")
        
    except Exception as e:
        print(f"\nError during customization: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    main() 