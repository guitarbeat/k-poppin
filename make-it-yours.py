#!/usr/bin/env python3
import re
import json
import argparse
import os
import sys
import shutil
import datetime
import logging
from urllib.request import urlretrieve

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger('customize_heardle')

def create_backup(file_path):
    """Create a backup of a file before modifying it"""
    if not os.path.exists(file_path):
        logger.warning(f"Can't backup non-existent file: {file_path}")
        return
        
    backup_dir = 'backups'
    os.makedirs(backup_dir, exist_ok=True)
    
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = os.path.basename(file_path)
    backup_path = os.path.join(backup_dir, f"{filename}.{timestamp}")
    
    shutil.copy2(file_path, backup_path)
    logger.info(f"Created backup: {backup_path}")

def validate_config(config):
    """Validate the configuration file"""
    required_sections = ['project', 'game_comments', 'appearance', 'analytics']
    for section in required_sections:
        if section not in config:
            raise ValueError(f"Missing required section '{section}' in config file")
    
    project_keys = ['app_name', 'app_display_name', 'glitch_name', 'game_url', 
                    'artist_name', 'game_name', 'start_date']
    for key in project_keys:
        if key not in config['project']:
            raise ValueError(f"Missing required key '{key}' in project section")
    
    if len(config['game_comments']) < 7:
        raise ValueError(f"Need at least 7 game comments, found {len(config['game_comments'])}")
    
    if 'favicon_url' not in config['appearance']:
        raise ValueError("Missing 'favicon_url' in appearance section")
    
    if 'colors' not in config['appearance']:
        raise ValueError("Missing 'colors' in appearance section")
    
    color_keys = ['primary', 'secondary', 'background', 'text', 'positive', 
                  'negative', 'foreground', 'midground', 'line', 'playback-bar']
    for key in color_keys:
        if key not in config['appearance']['colors']:
            raise ValueError(f"Missing color '{key}' in colors section")
    
    logger.info("Configuration validated successfully")
    return True

def load_config(config_file='your-data.json'):
    """Load configuration from a JSON file"""
    # Check if config file exists
    if not os.path.exists(config_file):
        raise FileNotFoundError(f"Config file not found: {config_file}")
    
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
            logger.info(f"Configuration loaded from {config_file}")
    except json.JSONDecodeError as e:
        raise Exception(f"Error parsing config file: {e}")
    except Exception as e:
        raise Exception(f"Error loading config file: {e}")
    
    # Validate the configuration
    validate_config(config)
    
    # Map to variables for backward compatibility
    global APP_NAME, APP_DISPLAY_NAME, GLITCH_NAME, GAME_URL, ARTIST_NAME
    global GAME_NAME, START_DATE, GAME_COMMENTS, GOOGLE_ANALYTICS_ID
    global NEW_FAVICON_URL, COLORS
    
    APP_NAME = config['project']['app_name']
    APP_DISPLAY_NAME = config['project']['app_display_name']
    GLITCH_NAME = config['project']['glitch_name']
    GAME_URL = config['project']['game_url']
    ARTIST_NAME = config['project']['artist_name'] 
    GAME_NAME = config['project']['game_name']
    START_DATE = config['project']['start_date']
    GAME_COMMENTS = config['game_comments']
    GOOGLE_ANALYTICS_ID = config['analytics']['google_analytics_id']
    NEW_FAVICON_URL = config['appearance']['favicon_url']
    COLORS = config['appearance']['colors']
    
    return config

# Default variable declarations
APP_NAME = ""
APP_DISPLAY_NAME = ""
GLITCH_NAME = ""
GAME_URL = ""
ARTIST_NAME = ""
GAME_NAME = ""
START_DATE = ""
GAME_COMMENTS = []
GOOGLE_ANALYTICS_ID = ""
NEW_FAVICON_URL = ""
COLORS = {}

def update_app_name():
    """Update the app name in main.js and index.html"""
    try:
        # First, create a backup
        create_backup('main.js')
        create_backup('index.html')
        
        # Update main.js
        with open('main.js', 'r') as file:
            content = file.read()
        
        # Replace the Heardle variables
        content = re.sub(r'const HEARDLE_GLITCH_NAME = ".*?";', f'const HEARDLE_GLITCH_NAME = "{GLITCH_NAME}";', content)
        content = re.sub(r'const HEARDLE_URL = ".*?";', f'const HEARDLE_URL = "{GAME_URL}";', content)
        content = re.sub(r'const HEARDLE_ARTIST = ".*?";', f'const HEARDLE_ARTIST = "{ARTIST_NAME}";', content)
        content = re.sub(r'const HEARDLE_NAME = .*?;', f'const HEARDLE_NAME = "{GAME_NAME}";', content)
        content = re.sub(r'const HEARDLE_START_DATE = ".*?";', f'const HEARDLE_START_DATE = "{START_DATE}";', content)
        
        # Replace game comments
        if len(GAME_COMMENTS) >= 7:
            comments_pattern = r'const HEARDLE_GAME_COMMENTS = \[\s*".*?",\s*".*?",\s*".*?",\s*".*?",\s*".*?",\s*".*?",\s*".*?"\s*\];'
            comments_replacement = f'const HEARDLE_GAME_COMMENTS = [\n    "{GAME_COMMENTS[0]}",\n    "{GAME_COMMENTS[1]}",\n    "{GAME_COMMENTS[2]}",\n    "{GAME_COMMENTS[3]}",\n    "{GAME_COMMENTS[4]}",\n    "{GAME_COMMENTS[5]}",\n    "{GAME_COMMENTS[6]}"\n];'
            content = re.sub(comments_pattern, comments_replacement, content, flags=re.DOTALL)
        
        # Update the Vt object with startDate
        content = re.sub(r'startDate: ".*?"', f'startDate: "{START_DATE}"', content)
        
        # Update any references to the old project name in the clipboard text
        content = re.sub(r'kpopgg-heardle-round2\.glitch\.me', GLITCH_NAME + '.glitch.me', content)
        
        with open('main.js', 'w') as file:
            file.write(content)
            
        # Update index.html
        with open('index.html', 'r') as file:
            content = file.read()
            
        # Update title and description
        content = re.sub(r'<title>.*?</title>', f'<title>{GAME_NAME}</title>', content)
        content = re.sub(r'<meta name="description" content=".*?"', f'<meta name="description" content="Guess the {ARTIST_NAME} song from the intro in as few tries as possible."', content)
        content = re.sub(r'<meta itemprop="name" content=".*?"', f'<meta itemprop="name" content="{GAME_NAME}"', content)
        content = re.sub(r'<meta itemprop="description" content=".*?"', f'<meta itemprop="description" content="Guess the {ARTIST_NAME} song from the intro in as few tries as possible."', content)
        content = re.sub(r'<meta property="og:title" content=".*?"', f'<meta property="og:title" content="{GAME_NAME}"', content)
        content = re.sub(r'<meta property="og:description" content=".*?"', f'<meta property="og:description" content="Guess the {ARTIST_NAME} song from the intro in as few tries as possible."', content)
        content = re.sub(r'<meta name="twitter:title" content=".*?"', f'<meta name="twitter:title" content="{GAME_NAME}"', content)
        content = re.sub(r'<meta name="twitter:description" content=".*?"', f'<meta name="twitter:description" content="Guess the {ARTIST_NAME} song from the intro in as few tries as possible."', content)
        
        with open('index.html', 'w') as file:
            file.write(content)
            
        logger.info("Updated app name in main.js and index.html")
        return True
    except Exception as e:
        logger.error(f"Error updating app name: {e}")
        return False

def update_google_analytics():
    """Update or remove Google Analytics based on configuration"""
    try:
        create_backup('index.html')
        
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
        </script>'''
            # Insert GA script before </head>
            if '<!-- Google Analytics -->' not in content:
                content = content.replace('</head>', f'{ga_script}\n    </head>')
            else:
                # Replace existing GA script
                content = re.sub(r'<!-- Google Analytics -->.*?</script>\s*?</head>', f'{ga_script}\n    </head>', content, flags=re.DOTALL)
        else:
            # Remove existing GA script if any
            content = re.sub(r'<!-- Google Analytics -->.*?</script>\s*', '', content, flags=re.DOTALL)
        
        with open('index.html', 'w') as file:
            file.write(content)
            
        logger.info("Updated Google Analytics configuration")
        return True
    except Exception as e:
        logger.error(f"Error updating Google Analytics: {e}")
        return False

def update_favicon():
    """Update favicon URLs in index.html"""
    try:
        create_backup('index.html')
        
        with open('index.html', 'r') as file:
            content = file.read()
        
        # Find all favicon URLs in the content
        favicon_urls = re.findall(r'https://cdn\.glitch\.global/[^"]+?/favicon\.[^"]+', content)
        
        if favicon_urls:
            for url in set(favicon_urls):
                content = content.replace(url, NEW_FAVICON_URL)
        else:
            # Replace default favicon link
            content = re.sub(r'<link rel="icon" type="image/png" href="[^"]+"', f'<link rel="icon" type="image/png" href="{NEW_FAVICON_URL}"', content)
        
        with open('index.html', 'w') as file:
            file.write(content)
            
        logger.info("Updated favicon URL")
        return True
    except Exception as e:
        logger.error(f"Error updating favicon: {e}")
        return False

def update_colors():
    """Update color scheme in bundle.css"""
    try:
        create_backup('bundle.css')
        
        with open('bundle.css', 'r') as file:
            content = file.read()
        
        # Find and replace the :root section
        root_pattern = r':root\s*\{\s*--color-positive:.*?;.*?--color-negative:.*?;.*?--color-fg:.*?;.*?--color-mg:.*?;.*?--color-bg:.*?;.*?--color-line:.*?;.*?\}'
        
        root_replacement = f''':root {{
  --color-positive: {COLORS["positive"]}; /* Submit button */
  --color-negative: {COLORS["negative"]}; /* Incorrect answer */
  --color-fg: {COLORS["foreground"]};       /* Font color and accents */
  --color-mg: {COLORS["midground"]};       /* Skip button, progress bar, line colour for inactive guesses */
  --color-bg: {COLORS["background"]};       /* Page background colour */
  --color-line: {COLORS["line"]};     /* Line color for current guess box, top line, and song player lines */
}}'''
        
        content = re.sub(root_pattern, root_replacement, content, flags=re.DOTALL)
        
        with open('bundle.css', 'w') as file:
            file.write(content)
            
        logger.info("Updated color scheme")
        return True
    except Exception as e:
        logger.error(f"Error updating colors: {e}")
        return False

def update_html_content():
    """Update various HTML content in index.html"""
    try:
        create_backup('index.html')
        
        with open('index.html', 'r') as file:
            content = file.read()
        
        # Update meta tags and URLs
        content = re.sub(r'content="https://[^"]+?"', f'content="{GAME_URL}"', content)
        content = re.sub(r'property="og:url" content="[^"]+"', f'property="og:url" content="{GAME_URL}"', content)
        
        with open('index.html', 'w') as file:
            file.write(content)
            
        logger.info("Updated HTML content")
        return True
    except Exception as e:
        logger.error(f"Error updating HTML content: {e}")
        return False

def ensure_css_imports():
    """Ensure the CSS has the proper font imports"""
    try:
        create_backup('global.css')
        
        with open('global.css', 'r') as file:
            content = file.read()
        
        # Check if font import exists
        if '@import url("https://fonts.googleapis.com/css2' not in content:
            # Add font import at the top of the file
            font_import = '@import url("https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;700&family=Noto+Serif+Display:wght@600&display=swap");\n\n'
            content = font_import + content
        
        with open('global.css', 'w') as file:
            file.write(content)
            
        logger.info("Ensured CSS imports")
        return True
    except Exception as e:
        logger.error(f"Error ensuring CSS imports: {e}")
        return False

def check_required_files():
    """Check if all required files exist before proceeding"""
    required_files = ['main.js', 'index.html', 'bundle.css', 'global.css']
    missing_files = []
    
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        error_message = f"Missing required files: {', '.join(missing_files)}"
        logger.error(error_message)
        raise FileNotFoundError(error_message)
    
    logger.info("All required files found")
    return True

def initialize_project():
    """Initialize a new project by downloading template files"""
    logger.info("Initializing new Heardle project...")
    
    # Try to load config file to get repository URL
    try:
        config = load_config()
        base_url = config['project'].get('repository_url', "https://raw.githubusercontent.com/guitarbeat/Wordle-but-with-songs/main/")
    except Exception as e:
        logger.warning(f"Could not load config file: {e}. Using default repository URL.")
        base_url = "https://raw.githubusercontent.com/guitarbeat/Wordle-but-with-songs/main/"
    
    files_to_download = {
        'main.js': base_url + 'main.js',
        'index.html': base_url + 'index.html',
        'bundle.css': base_url + 'bundle.css',
        'global.css': base_url + 'global.css',
        'songs.js': base_url + 'songs.js'
    }
    
    # Download each file
    for file_name, url in files_to_download.items():
        try:
            logger.info(f"Downloading {file_name}...")
            urlretrieve(url, file_name)
            logger.info(f"Downloaded {file_name}")
        except Exception as e:
            logger.error(f"Error downloading {file_name}: {e}")
            raise
    
    logger.info("Project initialization complete. Use --dry-run to preview your changes.")
    return True

def update_ko_fi_link(config):
    """Update the Ko-fi link in main.js"""
    try:
        create_backup('main.js')
        
        with open('main.js', 'r') as file:
            content = file.read()
        
        # Update the Ko-fi link
        ko_fi_url = config['project'].get('ko_fi_url', '')
        if ko_fi_url:
            # Replace the Ko-fi link in the support message
            content = re.sub(r'<a href="https://ko-fi\.com/[^"]+"', f'<a href="{ko_fi_url}"', content)
            
            # Update the Ko-fi text if needed
            content = re.sub(r'Support me on Ko-Fi', 'Support me on Ko-Fi', content)
            
            logger.info(f"Updated Ko-fi link to: {ko_fi_url}")
        else:
            logger.warning("No Ko-fi URL provided in config, skipping Ko-fi link update")
        
        with open('main.js', 'w') as file:
            file.write(content)
            
        return True
    except Exception as e:
        logger.error(f"Error updating Ko-fi link: {e}")
        return False

def update_about_text(config):
    """Update the about popup text in main.js"""
    try:
        create_backup('main.js')
        
        with open('main.js', 'r') as file:
            content = file.read()
        
        # Update the about text
        about_text = config['project'].get('about_text', '')
        if about_text:
            # Replace the about text in the popup
            content = re.sub(r'<p class="mb-3">A clone of <a href="https://www\.heardle\.app/" title="Heardle">Heardle</a>.*?<a href="https://glitch\.com/edit/#!/[^"]+">here</a>\.', 
                            about_text, content, flags=re.DOTALL)
            
            logger.info("Updated about popup text")
        else:
            logger.warning("No about text provided in config, skipping about text update")
        
        with open('main.js', 'w') as file:
            file.write(content)
            
        return True
    except Exception as e:
        logger.error(f"Error updating about text: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Customize your Heardle game')
    parser.add_argument('--config', '-c', type=str, help='Path to config JSON file')
    parser.add_argument('--skip-app-name', action='store_true', help='Skip updating app name')
    parser.add_argument('--skip-ga', action='store_true', help='Skip updating Google Analytics')
    parser.add_argument('--skip-favicon', action='store_true', help='Skip updating favicon')
    parser.add_argument('--skip-colors', action='store_true', help='Skip updating colors')
    parser.add_argument('--skip-html', action='store_true', help='Skip updating HTML content')
    parser.add_argument('--skip-css', action='store_true', help='Skip ensuring CSS imports')
    parser.add_argument('--skip-ko-fi', action='store_true', help='Skip updating Ko-fi link')
    parser.add_argument('--skip-about', action='store_true', help='Skip updating about text')
    parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose logging')
    parser.add_argument('--dry-run', action='store_true', help='Perform a dry run without making changes')
    parser.add_argument('--init', action='store_true', help='Initialize a new Heardle project')
    args = parser.parse_args()
    
    # Set verbose logging if requested
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    
    if args.dry_run:
        logger.info("DRY RUN MODE - No changes will be made")
    
    # Initialize project if requested
    if args.init:
        initialize_project()
        return 0
    
    try:
        # Check current directory
        current_dir = os.getcwd()
        logger.info(f"Running in directory: {current_dir}")
        
        # Load configuration - use default if not specified
        config_file = args.config if args.config is not None else 'your-data.json'
        config = load_config(config_file)
        
        # Check required files exist before proceeding (skip if dry run)
        if not args.dry_run:
            try:
                check_required_files()
            except FileNotFoundError:
                logger.error("Required files missing. Run with --init to create a new project.")
                return 1
        
        logger.info(f"Customizing Heardle for: {APP_DISPLAY_NAME}")
        logger.info(f"Configuration loaded: {GLITCH_NAME}, {ARTIST_NAME}")
        
        if args.dry_run:
            logger.info("DRY RUN - Would customize with these settings:")
            logger.info(f"App name: {APP_NAME}")
            logger.info(f"Display name: {APP_DISPLAY_NAME}")
            logger.info(f"Glitch name: {GLITCH_NAME}")
            logger.info(f"Game URL: {GAME_URL}")
            logger.info(f"Artist name: {ARTIST_NAME}")
            logger.info(f"Game name: {GAME_NAME}")
            logger.info(f"Start date: {START_DATE}")
            logger.info(f"GA ID: {GOOGLE_ANALYTICS_ID}")
            logger.info(f"Favicon URL: {NEW_FAVICON_URL}")
            logger.info(f"Ko-fi URL: {config['project'].get('ko_fi_url', 'Not set')}")
            logger.info(f"About text: {config['project'].get('about_text', 'Not set')[:50]}...")
            return 0
        
        if not args.skip_app_name:
            update_app_name()
        
        if not args.skip_ga:
            update_google_analytics()
        
        if not args.skip_favicon:
            update_favicon()
        
        if not args.skip_colors:
            update_colors()
        
        if not args.skip_html:
            update_html_content()
        
        if not args.skip_css:
            ensure_css_imports()
            
        if not args.skip_ko_fi:
            update_ko_fi_link(config)
            
        if not args.skip_about:
            update_about_text(config)
        
        logger.info("\n✅ All customizations complete!")
        logger.info(f"Your Heardle is now available at: {GAME_URL}")
        
        return 0
    except Exception as e:
        logger.error(f"Error during customization: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 