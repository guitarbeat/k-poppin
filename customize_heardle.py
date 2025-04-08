#!/usr/bin/env python3
import re
import json
import os
import datetime
from pathlib import Path

def extract_config_from_readme():
    """Extract configuration settings from README.md"""
    config = {
        "app_name": "",
        "app_display_name": "",
        "glitch_name": "",
        "artist_name": "Harry Styles",  # Default value
        "start_date": datetime.datetime.now().strftime("%Y-%m-%d"),  # Default to today
        "game_comments": [
            "Failed 😭",               # FAILED
            "Perfect! 🎯",             # First try
            "Amazing! ⭐",
            "Great! 👍",
            "Well done! 👏",
            "Good! 👌",
            "Not bad! 🙂"              # Sixth try
        ],
        "google_analytics_id": "",
        "favicon_url": "",
        "colors": {
            "primary": "#2a2139",       # Default value
            "secondary": "#4a4352",     # Default value
            "background": "#121212",    # Default value
            "text": "#ffffff",          # Default value
            "positive": "#4caf50",      # Default value
            "negative": "#f44336",      # Default value
            "foreground": "#ffffff",    # Default value
            "midground": "#2a2139",     # Default value
            "line": "#4a4352",          # Default value
            "playback-bar": "#272b46"   # Default value
        }
    }
    
    # Check if README.md exists
    if not os.path.exists("README.md"):
        print("README.md not found. Using default values.")
        return config
    
    # Read README.md content
    with open("README.md", "r") as f:
        readme_content = f.read()
    
    # Extract configuration from README.md
    
    # Get artist name from the title
    title_match = re.search(r'^# (.*?)\s*Heardle', readme_content, re.MULTILINE)
    if title_match:
        config["artist_name"] = title_match.group(1).strip()
    
    # Look for configuration section
    config_section_match = re.search(r'## Configuration\s*\n(.*?)(?:\n##|\Z)', 
                                     readme_content, re.DOTALL | re.MULTILINE)
    
    if not config_section_match:
        print("No configuration section found in README.md.")
        print("Using default values and creating a configuration section.")
        return config
    
    config_section = config_section_match.group(1)
    
    # Extract individual configuration items
    app_name_match = re.search(r'- App Name:\s*`(.*?)`', config_section)
    if app_name_match:
        config["app_name"] = app_name_match.group(1)
    
    app_display_match = re.search(r'- App Display Name:\s*`(.*?)`', config_section)
    if app_display_match:
        config["app_display_name"] = app_display_match.group(1)
    
    glitch_name_match = re.search(r'- Glitch Project Name:\s*`(.*?)`', config_section)
    if glitch_name_match:
        config["glitch_name"] = glitch_name_match.group(1)
    
    artist_name_match = re.search(r'- Artist Name:\s*`(.*?)`', config_section)
    if artist_name_match:
        config["artist_name"] = artist_name_match.group(1)
    
    start_date_match = re.search(r'- Start Date:\s*`(.*?)`', config_section)
    if start_date_match:
        config["start_date"] = start_date_match.group(1)
    
    ga_id_match = re.search(r'- Google Analytics ID:\s*`(.*?)`', config_section)
    if ga_id_match:
        config["google_analytics_id"] = ga_id_match.group(1)
    
    favicon_url_match = re.search(r'- Favicon URL:\s*`(.*?)`', config_section)
    if favicon_url_match:
        config["favicon_url"] = favicon_url_match.group(1)
    
    # Extract game comments
    comments_match = re.search(r'### Game Comments\s*\n```\s*\n(.*?)\n```', config_section, re.DOTALL)
    if comments_match:
        comments_text = comments_match.group(1).strip()
        comments = []
        for line in comments_text.split('\n'):
            line = line.strip()
            if line:
                comments.append(line)
        if len(comments) == 7:  # Make sure we have exactly 7 comments
            config["game_comments"] = comments
    
    # Extract colors
    colors_match = re.search(r'### Colors\s*\n```\s*\n(.*?)\n```', config_section, re.DOTALL)
    if colors_match:
        colors_text = colors_match.group(1).strip()
        for line in colors_text.split('\n'):
            line = line.strip()
            if not line or ':' not in line:
                continue
            key, value = line.split(':', 1)
            key = key.strip().lower()
            value = value.strip()
            if key in config["colors"] and re.match(r'^#[0-9a-fA-F]{6}$', value):
                config["colors"][key] = value
    
    # Make sure app_name is set
    if not config["app_name"] and config["glitch_name"]:
        config["app_name"] = config["glitch_name"]
    elif not config["app_name"] and config["artist_name"]:
        config["app_name"] = f"{config['artist_name'].lower().replace(' ', '-')}-heardle"
    
    # Make sure app_display_name is set
    if not config["app_display_name"] and config["artist_name"]:
        config["app_display_name"] = f"{config['artist_name']} Heardle"
    
    # Make sure glitch_name is set
    if not config["glitch_name"] and config["app_name"]:
        config["glitch_name"] = config["app_name"]
    
    # Derive other settings
    if config["glitch_name"]:
        config["game_url"] = f"https://{config['glitch_name']}.glitch.me/"
    else:
        config["game_url"] = "https://your-heardle.glitch.me/"
    
    if config["artist_name"]:
        config["game_name"] = f"{config['artist_name']} Heardle"
    else:
        config["game_name"] = "Custom Heardle"
    
    return config

def update_readme_with_config(config):
    """Update README.md with the configuration section"""
    if not os.path.exists("README.md"):
        print("README.md not found. Creating a new one.")
        with open("README.md", "w") as f:
            f.write(f"# {config['artist_name']} Heardle\n\n")
    
    # Read README.md content
    with open("README.md", "r") as f:
        readme_content = f.read()
    
    # First, remove any orphaned Game Comments or Colors sections that might exist
    readme_content = re.sub(r'### Game Comments\s*\n```[\s\S]*?```\s*\n', '', readme_content)
    readme_content = re.sub(r'### Colors\s*\n```[\s\S]*?```\s*\n', '', readme_content)
    
    # Clean up any double newlines created by the removal
    readme_content = re.sub(r'\n\n\n+', '\n\n', readme_content)
    
    # Now remove any existing Configuration sections
    if "## Configuration" in readme_content:
        readme_content = re.sub(r'## Configuration\s*\n(.*?)(?=\n##|\Z)', 
                             '', 
                             readme_content, 
                             flags=re.DOTALL)
        # Clean up any double newlines again
        readme_content = re.sub(r'\n\n\n+', '\n\n', readme_content)
    
    # Prepare configuration section
    config_section = f"""
## Configuration

Edit these values to customize your Heardle game:

- App Name: `{config['app_name']}`
- App Display Name: `{config['app_display_name']}`
- Glitch Project Name: `{config['glitch_name']}`
- Artist Name: `{config['artist_name']}`
- Start Date: `{config['start_date']}`
- Google Analytics ID: `{config['google_analytics_id']}`
- Favicon URL: `{config['favicon_url']}`

### Game Comments
```
{chr(10).join(config['game_comments'])}
```

### Colors
```
primary: {config['colors']['primary']}
secondary: {config['colors']['secondary']}
background: {config['colors']['background']}
text: {config['colors']['text']}
positive: {config['colors']['positive']}
negative: {config['colors']['negative']}
foreground: {config['colors']['foreground']}
midground: {config['colors']['midground']}
line: {config['colors']['line']}
playback-bar: {config['colors']['playback-bar']}
```

"""
    
    # Find the position after the title section to insert the configuration
    first_h2_match = re.search(r'\n## ', readme_content)
    if first_h2_match:
        insert_position = first_h2_match.start()
        updated_readme = (
            readme_content[:insert_position] + 
            config_section + 
            readme_content[insert_position:]
        )
    else:
        updated_readme = readme_content + config_section
    
    with open("README.md", "w") as f:
        f.write(updated_readme)
    
    print("Updated README.md with configuration section.")

def update_app_name(config):
    """Update app name in index.html and main.js"""
    # Update index.html
    try:
        with open('index.html', 'r') as file:
            content = file.read()
        
        content = re.sub(r'<title>.*?</title>', f'<title>{config["game_name"]}</title>', content)
        content = re.sub(r'content="Guess the Harry Styles song', f'content="Guess the {config["artist_name"]} song', content)
        
        with open('index.html', 'w') as file:
            file.write(content)
    except FileNotFoundError:
        print("Warning: index.html not found. Skipping app name update.")
    
    # Update main.js
    try:
        with open('main.js', 'r') as file:
            content = file.read()
        
        # Update all configuration values
        content = re.sub(r'HEARDLE_GLITCH_NAME\s*=\s*".*?"', f'HEARDLE_GLITCH_NAME = "{config["glitch_name"]}"', content)
        content = re.sub(r'HEARDLE_URL\s*=\s*".*?"', f'HEARDLE_URL = "{config["game_url"]}"', content)
        content = re.sub(r'HEARDLE_ARTIST\s*=\s*".*?"', f'HEARDLE_ARTIST = "{config["artist_name"]}"', content)
        content = re.sub(r'HEARDLE_NAME\s*=\s*".*?"', f'HEARDLE_NAME = "{config["game_name"]}"', content)
        content = re.sub(r'HEARDLE_START_DATE\s*=\s*".*?"', f'HEARDLE_START_DATE = "{config["start_date"]}"', content)
        
        # Update game comments
        comments_str = ',\n      '.join([f'"{comment}"' for comment in config["game_comments"]])
        content = re.sub(r'const HEARDLE_GAME_COMMENTS = \[.*?\];', 
                        f'const HEARDLE_GAME_COMMENTS = [\n      {comments_str}\n    ];', 
                        content, 
                        flags=re.DOTALL)
        
        with open('main.js', 'w') as file:
            file.write(content)
    except FileNotFoundError:
        print("Warning: main.js not found. Skipping app name update.")

def update_google_analytics(config):
    """Update or remove Google Analytics based on configuration"""
    try:
        with open('index.html', 'r') as file:
            content = file.read()
        
        if config["google_analytics_id"]:
            # Add Google Analytics if ID is provided
            ga_script = f'''
        <!-- Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id={config["google_analytics_id"]}"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){{dataLayer.push(arguments);}}
            gtag('js', new Date());
            gtag('config', '{config["google_analytics_id"]}');
        </script>
        '''
            # Insert GA script before </head>
            content = content.replace('</head>', f'{ga_script}\n</head>')
        else:
            # Remove existing GA script if any
            content = re.sub(r'<!-- Google Analytics -->.*?</script>\n', '', content, flags=re.DOTALL)
        
        with open('index.html', 'w') as file:
            file.write(content)
    except FileNotFoundError:
        print("Warning: index.html not found. Skipping Google Analytics update.")

def update_favicon(config):
    """Update favicon URL in index.html"""
    if not config["favicon_url"]:
        print("No favicon URL provided, skipping favicon update")
        return

    try:
        with open('index.html', 'r') as file:
            content = file.read()
        
        # Replace all instances of the old favicon URL
        old_favicon_pattern = r'https://cdn\.glitch\.global/[^"]+/favicon\.png\?[^"]*'
        content = re.sub(old_favicon_pattern, config["favicon_url"], content)
        
        with open('index.html', 'w') as file:
            file.write(content)
    except FileNotFoundError:
        print("Warning: index.html not found. Skipping favicon update.")

def update_colors(config):
    """Update color scheme in stylesheet.css or bundle.css"""
    # Try stylesheet.css first
    css_file = 'stylesheet.css'
    if not os.path.exists(css_file):
        # Fall back to bundle.css
        css_file = 'bundle.css'
        if not os.path.exists(css_file):
            print("Warning: No CSS file found. Skipping color update.")
            return
    
    try:
        with open(css_file, 'r') as file:
            content = file.read()
        
        # Update all color variables
        content = re.sub(r'--color-primary:\s*#[0-9a-fA-F]{6}', f'--color-primary: {config["colors"]["primary"]}', content)
        content = re.sub(r'--color-secondary:\s*#[0-9a-fA-F]{6}', f'--color-secondary: {config["colors"]["secondary"]}', content)
        content = re.sub(r'--color-background:\s*#[0-9a-fA-F]{6}', f'--color-background: {config["colors"]["background"]}', content)
        content = re.sub(r'--color-text:\s*#[0-9a-fA-F]{6}', f'--color-text: {config["colors"]["text"]}', content)
        content = re.sub(r'--color-positive:\s*#[0-9a-fA-F]{6}', f'--color-positive: {config["colors"]["positive"]}', content)
        content = re.sub(r'--color-negative:\s*#[0-9a-fA-F]{6}', f'--color-negative: {config["colors"]["negative"]}', content)
        content = re.sub(r'--color-fg:\s*#[0-9a-fA-F]{6}', f'--color-fg: {config["colors"]["foreground"]}', content)
        content = re.sub(r'--color-mg:\s*#[0-9a-fA-F]{6}', f'--color-mg: {config["colors"]["midground"]}', content)
        content = re.sub(r'--color-bg:\s*#[0-9a-fA-F]{6}', f'--color-bg: {config["colors"]["background"]}', content)
        content = re.sub(r'--color-line:\s*#[0-9a-fA-F]{6}', f'--color-line: {config["colors"]["line"]}', content)
        content = re.sub(r'--color-playback-bar:\s*#[0-9a-fA-F]{6}', f'--color-playback-bar: {config["colors"]["playback-bar"]}', content)
        
        with open(css_file, 'w') as file:
            file.write(content)
    except FileNotFoundError:
        print(f"Warning: {css_file} not found. Skipping color update.")

def update_html_content(config):
    """Update HTML content with custom theme"""
    try:
        with open('index.html', 'r') as file:
            content = file.read()
        
        # Update meta tags and content
        content = re.sub(r'<title>.*?</title>', f'<title>{config["app_display_name"]}</title>', content)
        
        # Update all Harry Styles references
        content = re.sub(r'Harry Styles', config["artist_name"], content, flags=re.IGNORECASE)
        
        # Update meta descriptions
        meta_description = f'Guess the {config["artist_name"]} song from the intro in as few tries as possible.'
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
                        f'<meta itemprop="name" content="{config["game_name"]}"', content)
        content = re.sub(r'<meta property="og:title" content=".*?"', 
                        f'<meta property="og:title" content="{config["game_name"]}"', content)
        content = re.sub(r'<meta name="twitter:title" content=".*?"', 
                        f'<meta name="twitter:title" content="{config["game_name"]}"', content)
        
        # Update images if favicon URL provided
        if config["favicon_url"]:
            content = re.sub(r'<meta itemprop="image" content=".*?"', 
                            f'<meta itemprop="image" content="{config["favicon_url"]}"', content)
            content = re.sub(r'<meta property="og:image" content=".*?"', 
                            f'<meta property="og:image" content="{config["favicon_url"]}"', content)
            content = re.sub(r'<meta name="twitter:image" content=".*?"', 
                            f'<meta name="twitter:image" content="{config["favicon_url"]}"', content)
            
            # Update favicon links
            content = re.sub(r'<link rel="icon".*?href=".*?"', 
                            f'<link rel="icon" type="image/png" href="{config["favicon_url"]}"', content)
            content = re.sub(r'<link rel="icon".*?sizes="32x32".*?href=".*?"', 
                            f'<link rel="icon" type="image/png" sizes="32x32" href="{config["favicon_url"]}"', content)
            content = re.sub(r'<link rel="icon".*?sizes="16x16".*?href=".*?"', 
                            f'<link rel="icon" type="image/png" sizes="16x16" href="{config["favicon_url"]}"', content)
            content = re.sub(r'<link rel="apple-touch-icon".*?href=".*?"', 
                            f'<link rel="apple-touch-icon" sizes="180x180" href="{config["favicon_url"]}"', content)
            content = re.sub(r'<link rel="shortcut icon".*?href=".*?"', 
                            f'<link rel="shortcut icon" href="{config["favicon_url"]}"', content)
        
        with open('index.html', 'w') as file:
            file.write(content)
    except FileNotFoundError:
        print("Warning: index.html not found. Skipping HTML content update.")

def ensure_css_imports(config):
    """Ensure the CSS has the proper font imports"""
    css_file = 'stylesheet.css'
    if not os.path.exists(css_file):
        # Check if bundle.css exists
        if os.path.exists('bundle.css'):
            # Copy bundle.css to stylesheet.css
            with open('bundle.css', 'r') as src:
                with open('stylesheet.css', 'w') as dst:
                    dst.write(src.read())
        else:
            # Create a new stylesheet.css
            with open('stylesheet.css', 'w') as file:
                file.write('''@import url("https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;700&family=Noto+Serif+Display:wght@600&display=swap");

:root {
  --color-primary: #2a2139;
  --color-secondary: #4a4352;
  --color-background: #121212;
  --color-text: #ffffff;
  --color-positive: #4caf50;
  --color-negative: #f44336;
  --color-fg: #ffffff;
  --color-mg: #2a2139;
  --color-bg: #121212;
  --color-line: #4a4352;
  --color-playback-bar: #272b46;
}

body {
  font-family: 'Noto Sans', sans-serif;
  background-color: var(--color-background);
  color: var(--color-text);
  margin: 0;
  padding: 0;
}

h1, h2, h3 {
  font-family: 'Noto Serif Display', serif;
}
''')
    
    try:
        with open('stylesheet.css', 'r') as file:
            content = file.read()
        
        # Check if font import exists
        if '@import url("https://fonts.googleapis.com/css2' not in content:
            # Add font import at the top of the file
            font_import = '@import url("https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;700&family=Noto+Serif+Display:wght@600&display=swap");\n\n'
            content = font_import + content
        
        # Make sure CSS references are updated in index.html
        try:
            with open('index.html', 'r') as file:
                html_content = file.read()
            
            # Update CSS references to use stylesheet.css
            updated = False
            if '<link rel="stylesheet" href="global.css">' in html_content and '<link rel="stylesheet" href="bundle.css">' in html_content:
                html_content = html_content.replace(
                    '<link rel="stylesheet" href="global.css">\n    <link rel="stylesheet" href="bundle.css">', 
                    '<link rel="stylesheet" href="stylesheet.css">'
                )
                updated = True
            
            if not updated and '<link rel="stylesheet" href="bundle.css">' in html_content:
                html_content = html_content.replace(
                    '<link rel="stylesheet" href="bundle.css">', 
                    '<link rel="stylesheet" href="stylesheet.css">'
                )
            
            with open('index.html', 'w') as file:
                file.write(html_content)
        except FileNotFoundError:
            print("Warning: index.html not found. Skipping CSS reference update.")
        
        with open('stylesheet.css', 'w') as file:
            file.write(content)
    except FileNotFoundError:
        print("Warning: stylesheet.css not found. Skipping CSS import update.")

def main():
    """Main function to run all customizations"""
    print("Starting Heardle customization...")
    
    try:
        # Extract configuration from README.md
        print("Extracting configuration from README.md...")
        config = extract_config_from_readme()
        
        # Debug prints
        print(f"DEBUG - Artist name from README: {config['artist_name']}")
        
        # Update README.md with the configuration section
        print("Updating README.md with configuration section...")
        update_readme_with_config(config)
        
        # Debug prints after update
        print(f"DEBUG - Artist name after README update: {config['artist_name']}")
        
        print(f"Updating app name to {config['app_display_name']}...")
        update_app_name(config)
        
        print("Updating Google Analytics configuration...")
        update_google_analytics(config)
        
        print("Updating favicon...")
        update_favicon(config)
        
        print("Ensuring CSS imports...")
        ensure_css_imports(config)
        
        print("Updating color scheme...")
        update_colors(config)
        
        print("Updating HTML content...")
        update_html_content(config)
        
        print("\nCustomization completed successfully!")
        print(f"Your custom Heardle game for {config['artist_name']} is ready!")
        print(f"To deploy your game:")
        print(f"1. Upload these files to Glitch")
        print(f"2. Your game will be available at: {config['game_url']}")
        
    except Exception as e:
        print(f"\nError during customization: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    main()