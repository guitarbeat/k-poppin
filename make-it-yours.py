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
    
    return backup_path

def check_js_syntax(js_content):
    """
    Basic check to see if JavaScript syntax is balanced
    Returns True if the syntax seems valid, False otherwise
    """
    # Check for balanced brackets and quotes
    brackets = {'(': ')', '[': ']', '{': '}'}
    stack = []
    in_string = None  # None, ', or "
    escaped = False
    
    for i, char in enumerate(js_content):
        # Handle string literals
        if in_string:
            if escaped:
                escaped = False
                continue
            if char == '\\':
                escaped = True
                continue
            if char == in_string:
                in_string = None
            continue
        
        if char in ["'", '"']:
            in_string = char
            continue
        
        # Handle brackets
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack:
                logger.warning(f"Syntax error: unexpected closing bracket '{char}' at position {i}")
                return False
            
            last_open = stack.pop()
            if char != brackets.get(last_open):
                logger.warning(f"Syntax error: mismatched brackets '{last_open}' and '{char}' at position {i}")
                return False
    
    # Check if all brackets are closed
    if stack:
        logger.warning(f"Syntax error: unclosed brackets: {''.join(stack)}")
        return False
    
    # Check if all strings are closed
    if in_string:
        logger.warning(f"Syntax error: unclosed string")
        return False
    
    return True

def safe_update_file(file_path, new_content):
    """Update a file only if content has changed, creating a backup if needed"""
    if not os.path.exists(file_path):
        logger.warning(f"File does not exist: {file_path}")
        return False
        
    # Read original content
    with open(file_path, 'r') as file:
        original_content = file.read()
    
    # Check if content would change
    if original_content == new_content:
        logger.info(f"No changes needed for {file_path}")
        return False
    
    # For JavaScript files, validate syntax before saving
    if file_path.endswith('.js'):
        if not check_js_syntax(new_content):
            logger.error(f"Cannot update {file_path}: The generated JavaScript has syntax errors")
            return False
    
    # Create backup since we're making changes
    create_backup(file_path)
    
    # Write new content
    with open(file_path, 'w') as file:
        file.write(new_content)
    
    logger.info(f"Updated {file_path}")
    return True

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
        # Update main.js
        with open('main.js', 'r') as file:
            content = file.read()
        
        # Replace the Heardle variables
        new_content = content
        new_content = re.sub(r'const HEARDLE_GLITCH_NAME = ".*?";', f'const HEARDLE_GLITCH_NAME = "{GLITCH_NAME}";', new_content)
        new_content = re.sub(r'const HEARDLE_URL = ".*?";', f'const HEARDLE_URL = "{GAME_URL}";', new_content)
        new_content = re.sub(r'const HEARDLE_ARTIST = ".*?";', f'const HEARDLE_ARTIST = "{ARTIST_NAME}";', new_content)
        new_content = re.sub(r'const HEARDLE_NAME = .*?;', f'const HEARDLE_NAME = "{GAME_NAME}";', new_content)
        new_content = re.sub(r'const HEARDLE_START_DATE = ".*?";', f'const HEARDLE_START_DATE = "{START_DATE}";', new_content)
        
        # Replace game comments (standard pattern)
        if len(GAME_COMMENTS) >= 7:
            comments_pattern = r'const HEARDLE_GAME_COMMENTS = \[\s*".*?",\s*".*?",\s*".*?",\s*".*?",\s*".*?",\s*".*?",\s*".*?"\s*\];'
            comments_replacement = f'const HEARDLE_GAME_COMMENTS = [\n    "{GAME_COMMENTS[0]}",\n    "{GAME_COMMENTS[1]}",\n    "{GAME_COMMENTS[2]}",\n    "{GAME_COMMENTS[3]}",\n    "{GAME_COMMENTS[4]}",\n    "{GAME_COMMENTS[5]}",\n    "{GAME_COMMENTS[6]}"\n];'
            new_content = re.sub(comments_pattern, comments_replacement, new_content, flags=re.DOTALL)
            
            # Replace Jt array which is also used for game comments
            jt_comments_pattern = r'Jt\s*=\s*\[\s*"[^"]*",\s*"[^"]*",\s*"[^"]*",\s*"[^"]*",\s*"[^"]*",\s*"[^"]*",\s*"[^"]*"\s*\];'
            jt_comments_replacement = f'Jt = [\n      "{GAME_COMMENTS[0]}",\n      "{GAME_COMMENTS[1]}",\n      "{GAME_COMMENTS[2]}",\n      "{GAME_COMMENTS[3]}",\n      "{GAME_COMMENTS[4]}",\n      "{GAME_COMMENTS[5]}",\n      "{GAME_COMMENTS[6]}"\n    ];'
            new_content = re.sub(jt_comments_pattern, jt_comments_replacement, new_content, flags=re.DOTALL)
        
        # Update the Vt object with startDate
        new_content = re.sub(r'startDate: ".*?"', f'startDate: "{START_DATE}"', new_content)
        
        # Update any references to the old project name in the clipboard text
        new_content = re.sub(r'kpopgg-heardle-round2\.glitch\.me', GLITCH_NAME + '.glitch.me', new_content)
        
        # Update main.js file
        safe_update_file('main.js', new_content)
            
        # Update index.html
        with open('index.html', 'r') as file:
            content = file.read()
            
        # Update title and description
        new_content = content
        new_content = re.sub(r'<title>.*?</title>', f'<title>{GAME_NAME}</title>', new_content)
        new_content = re.sub(r'<meta name="description" content=".*?"', f'<meta name="description" content="Guess the {ARTIST_NAME} song from the intro in as few tries as possible."', new_content)
        new_content = re.sub(r'<meta itemprop="name" content=".*?"', f'<meta itemprop="name" content="{GAME_NAME}"', new_content)
        new_content = re.sub(r'<meta itemprop="description" content=".*?"', f'<meta itemprop="description" content="Guess the {ARTIST_NAME} song from the intro in as few tries as possible."', new_content)
        new_content = re.sub(r'<meta property="og:title" content=".*?"', f'<meta property="og:title" content="{GAME_NAME}"', new_content)
        new_content = re.sub(r'<meta property="og:description" content=".*?"', f'<meta property="og:description" content="Guess the {ARTIST_NAME} song from the intro in as few tries as possible."', new_content)
        new_content = re.sub(r'<meta name="twitter:title" content=".*?"', f'<meta name="twitter:title" content="{GAME_NAME}"', new_content)
        new_content = re.sub(r'<meta name="twitter:description" content=".*?"', f'<meta name="twitter:description" content="Guess the {ARTIST_NAME} song from the intro in as few tries as possible."', new_content)
        
        # Update index.html file
        safe_update_file('index.html', new_content)
            
        logger.info("Updated app name in main.js and index.html")
        return True
    except Exception as e:
        logger.error(f"Error updating app name: {e}")
        return False

def update_google_analytics():
    """Update or remove Google Analytics based on configuration"""
    try:
        with open('index.html', 'r') as file:
            content = file.read()
        
        new_content = content
        
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
                new_content = content.replace('</head>', f'{ga_script}\n    </head>')
            else:
                # Replace existing GA script
                new_content = re.sub(r'<!-- Google Analytics -->.*?</script>\s*?</head>', f'{ga_script}\n    </head>', content, flags=re.DOTALL)
        else:
            # Remove existing GA script if any
            new_content = re.sub(r'<!-- Google Analytics -->.*?</script>\s*', '', content, flags=re.DOTALL)
        
        # Update index.html file
        safe_update_file('index.html', new_content)
            
        logger.info("Updated Google Analytics configuration")
        return True
    except Exception as e:
        logger.error(f"Error updating Google Analytics: {e}")
        return False

def update_favicon():
    """Update favicon URLs in index.html"""
    try:
        with open('index.html', 'r') as file:
            content = file.read()
        
        # Find all favicon URLs in the content
        favicon_urls = re.findall(r'https://cdn\.glitch\.global/[^"]+?/favicon\.[^"]+', content)
        
        new_content = content
        if favicon_urls:
            for url in set(favicon_urls):
                new_content = new_content.replace(url, NEW_FAVICON_URL)
        else:
            # Replace default favicon link
            new_content = re.sub(r'<link rel="icon" type="image/png" href="[^"]+"', f'<link rel="icon" type="image/png" href="{NEW_FAVICON_URL}"', new_content)
        
        # Update index.html file
        safe_update_file('index.html', new_content)
            
        logger.info("Updated favicon URL")
        return True
    except Exception as e:
        logger.error(f"Error updating favicon: {e}")
        return False

def update_colors():
    """Update color scheme in bundle.css"""
    try:
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
        
        new_content = re.sub(root_pattern, root_replacement, content, flags=re.DOTALL)
        
        # Update bundle.css file
        safe_update_file('bundle.css', new_content)
            
        logger.info("Updated color scheme")
        return True
    except Exception as e:
        logger.error(f"Error updating colors: {e}")
        return False

def update_html_content():
    """Update various HTML content in index.html"""
    try:
        with open('index.html', 'r') as file:
            content = file.read()
        
        # Update meta tags and URLs
        new_content = re.sub(r'content="https://[^"]+?"', f'content="{GAME_URL}"', content)
        new_content = re.sub(r'property="og:url" content="[^"]+"', f'property="og:url" content="{GAME_URL}"', new_content)
        
        # Update index.html file
        safe_update_file('index.html', new_content)
            
        logger.info("Updated HTML content")
        return True
    except Exception as e:
        logger.error(f"Error updating HTML content: {e}")
        return False

def ensure_css_imports():
    """Ensure the CSS has the proper font imports"""
    try:
        with open('global.css', 'r') as file:
            content = file.read()
        
        # Check if font import exists
        new_content = content
        if '@import url("https://fonts.googleapis.com/css2' not in content:
            # Add font import at the top of the file
            font_import = '@import url("https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;700&family=Noto+Serif+Display:wght@600&display=swap");\n\n'
            new_content = font_import + content
        
        # Update global.css file
        safe_update_file('global.css', new_content)
            
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
        # Update the Ko-fi link
        ko_fi_url = config['project'].get('ko_fi_url', '')
        
        if not ko_fi_url:
            logger.warning("No Ko-fi URL provided in config, skipping Ko-fi link update")
            return True
        
        with open('main.js', 'r') as file:
            content = file.read()
        
        # First approach: Find the specific ko-fi link section 
        kofi_markers = [
            'Support me on Ko-Fi',
            'kofi-button',
            'ko-fi.com'
        ]
        
        # Go through each marker and look for href attributes nearby
        for marker in kofi_markers:
            marker_pos = content.find(marker)
            if marker_pos > 0:
                # Search before and after the marker for href
                start_search = max(0, marker_pos - 200)
                end_search = min(len(content), marker_pos + 200)
                search_area = content[start_search:end_search]
                
                # Look for the specific ko-fi URL pattern
                href_match = re.search(r'href=(["\'])(https://ko-fi\.com/[^"\']+)\1', search_area)
                if href_match:
                    old_url = href_match.group(2)
                    logger.info(f"Found ko-fi URL: {old_url}")
                    
                    # Create precise string replacement
                    old_pattern = f'href={href_match.group(1)}{old_url}{href_match.group(1)}'
                    new_pattern = f'href={href_match.group(1)}{ko_fi_url}{href_match.group(1)}'
                    
                    # Replace the URL
                    new_content = content.replace(old_pattern, new_pattern)
                    
                    if new_content != content:
                        logger.info(f"Successfully replaced ko-fi link from {old_url} to {ko_fi_url}")
                        safe_update_file('main.js', new_content)
                        return True
        
        # Second approach: Look for M(r, "href", "ko-fi.com") pattern
        href_matches = re.findall(r'M\([^,]+,\s*"href",\s*(["\'])(https://ko-fi\.com/[^"\']+)\1\)', content)
        if href_matches:
            new_content = content
            updated = False
            
            for quote_char, old_url in href_matches:
                old_pattern = f'M(r, "href", {quote_char}{old_url}{quote_char})'
                new_pattern = f'M(r, "href", {quote_char}{ko_fi_url}{quote_char})'
                
                if old_pattern in new_content:
                    new_content = new_content.replace(old_pattern, new_pattern)
                    updated = True
                    logger.info(f"Replaced ko-fi link in M() call from {old_url} to {ko_fi_url}")
            
            if updated:
                safe_update_file('main.js', new_content)
                return True
        
        # Third approach: Try harder with context-aware patterns
        kofi_functions = []
        
        # Find functions that likely contain ko-fi references
        function_matches = re.finditer(r'function ([A-Za-z0-9_]+)\(t\)\s*\{', content)
        for match in function_matches:
            func_name = match.group(1)
            # Find the end of this function
            func_start = match.start()
            open_braces = 0
            func_end = -1
            
            for i in range(func_start, len(content)):
                if content[i] == '{':
                    open_braces += 1
                elif content[i] == '}':
                    open_braces -= 1
                    if open_braces == 0:
                        func_end = i + 1
                        break
            
            if func_end > 0:
                func_body = content[func_start:func_end]
                # Check if this function contains ko-fi references
                if 'ko-fi.com' in func_body or 'Ko-Fi' in func_body:
                    kofi_functions.append((func_name, func_start, func_end))
        
        # If we found kofi functions, try to update them specifically
        if kofi_functions:
            new_content = content
            updated = False
            
            for func_name, start, end in kofi_functions:
                func_body = content[start:end]
                updated_func = func_body
                
                # Try to replace ko-fi URL in this function
                kofi_urls = re.findall(r'(https://ko-fi\.com/[^"\')\s]+)', func_body)
                for old_url in kofi_urls:
                    updated_func = updated_func.replace(old_url, ko_fi_url)
                
                if updated_func != func_body:
                    new_content = new_content[:start] + updated_func + new_content[end:]
                    updated = True
                    logger.info(f"Updated ko-fi URL in function {func_name}")
            
            if updated:
                # Validate JS before saving
                if check_js_syntax(new_content):
                    safe_update_file('main.js', new_content)
                    return True
                else:
                    logger.warning("Updated content has syntax errors, reverting changes")
                    return False
        
        # Last resort: Try to find and replace any ko-fi.com URLs directly
        direct_kofi_urls = re.findall(r'(https://ko-fi\.com/[^"\')\s]+)', content)
        if direct_kofi_urls:
            new_content = content
            updated = False
            
            for old_url in direct_kofi_urls:
                # Don't replace blindly as it might be part of a larger string
                # Use safer replacement with context
                for context in [f'href="{old_url}"', f"href='{old_url}'", f'"{old_url}"', f"'{old_url}'"]:
                    if context in new_content:
                        new_context = context.replace(old_url, ko_fi_url)
                        new_content = new_content.replace(context, new_context)
                        updated = True
                        logger.info(f"Replaced ko-fi URL {old_url} with {ko_fi_url} in context: {context}")
            
            if updated:
                safe_update_file('main.js', new_content)
                return True
            
        logger.warning("Ko-fi link pattern not found with any method")
        return False
        
    except Exception as e:
        logger.error(f"Error updating Ko-fi link: {e}", exc_info=True)
        return False

def escape_js_string(content):
    """
    Properly escape content for inclusion in JavaScript strings
    """
    # Escape backslashes, single quotes and newlines
    escaped = content.replace('\\', '\\\\')
    escaped = escaped.replace("'", "\\'")
    escaped = escaped.replace('\n', '\\n')
    escaped = escaped.replace('\r', '\\r')
    return escaped

def update_about_text(config):
    """Update the about popup text in main.js"""
    try:
        # Update the about text
        about_text = config['project'].get('about_text', '')
        
        if not about_text:
            logger.warning("No about text provided in config, skipping about text update")
            return True
            
        # Prepare the about text - escape for JavaScript
        about_text = escape_js_string(about_text)
            
        with open('main.js', 'r') as file:
            content = file.read()
            
        # First, try to find the exact Nt function by looking for fragments of known about text
        about_fragments = [
            '<p class="mb-3">A clone of <a href="https://www.heardle.app/"',
            'Original version made by',
            'All copyright goes to the respective artists'
        ]
        
        # Find the innerHTML assignment that contains these fragments
        about_section = None
        for fragment in about_fragments:
            start_pattern = f'n.innerHTML ='
            if start_pattern in content:
                # Find the position of the innerHTML assignment
                start_pos = content.find(start_pattern)
                if start_pos > 0:
                    # Find the closing quote/apostrophe
                    quote_char = None
                    for char in ["'", '"']:
                        if content[start_pos + len(start_pattern):].strip().startswith(char):
                            quote_char = char
                            break
                    
                    if quote_char:
                        # Find the end of the HTML string
                        inner_start = content.find(quote_char, start_pos + len(start_pattern))
                        if inner_start > 0:
                            inner_end = content.find(quote_char, inner_start + 1)
                            if inner_end > 0 and fragment in content[inner_start:inner_end]:
                                # Found the HTML content we need to replace
                                about_section = (inner_start+1, inner_end)  # +1 to exclude the quote
                                logger.info(f"Found about section from position {inner_start} to {inner_end}")
                                break
        
        if about_section:
            # Create the new content by preserving everything except the innerHTML
            new_content = content[:about_section[0]] + about_text + content[about_section[1]:]
                
            logger.info(f"Successfully prepared about text replacement")
            safe_update_file('main.js', new_content)
            return True
        else:
            # Second approach - look for the opening section of about text
            for fragment in about_fragments:
                fragment_start = content.find(fragment)
                if fragment_start > 0:
                    # Look backwards to find the opening quote
                    quote_char = None
                    quote_start = -1
                    for i in range(fragment_start - 1, max(0, fragment_start - 200), -1):
                        if content[i] in ['"', "'"]:
                            quote_char = content[i]
                            quote_start = i
                            break
                            
                    if quote_start == -1:
                        continue
                            
                    # Look forward to find the closing quote
                    quote_end = -1
                    for i in range(fragment_start + len(fragment), min(len(content), fragment_start + 2000)):
                        if content[i] == quote_char and content[i-1] != '\\':  # Check if not escaped
                            quote_end = i
                            break
                            
                    if quote_end == -1:
                        continue
                            
                    logger.info(f"Found about text using fragment search from {quote_start} to {quote_end}")
                    new_content = content[:quote_start+1] + about_text + content[quote_end:]
                    
                    # Verify we haven't broken any strings
                    test_section = new_content[max(0, quote_start-100):min(len(new_content), quote_end+100)]
                    if test_section.count(quote_char) % 2 != 0:
                        logger.warning("String replacement would create unbalanced quotes, trying alternative approach")
                        continue
                        
                    safe_update_file('main.js', new_content)
                    return True
            
            # Special fallback for specific known patterns
            special_patterns = [
                # Very specific pattern for the about text function
                (r'n\.innerHTML\s*=\s*([\'"]).*?<p class="mb-3">A clone of.*?\\n.*?<\/a>\.\1', 
                 lambda m: f'n.innerHTML = {m.group(1)}{about_text}{m.group(1)}'),
                 
                # Alternative pattern
                (r'n\.innerHTML\s*=\s*([\'"]).*?Heardle.*?K-pop.*?copyright.*?\1', 
                 lambda m: f'n.innerHTML = {m.group(1)}{about_text}{m.group(1)}')
            ]
            
            for pattern, replacement_func in special_patterns:
                matches = re.search(pattern, content, re.DOTALL)
                if matches:
                    new_content = re.sub(pattern, replacement_func, content, flags=re.DOTALL)
                    if new_content != content:
                        logger.info(f"Successfully updated about text using special pattern")
                        safe_update_file('main.js', new_content)
                        return True
                
            logger.warning("About text fragments not found in the file with any method")
            return False
    except Exception as e:
        logger.error(f"Error updating about text: {e}", exc_info=True)
        return False

def update_js_function(file_path, function_name, update_pattern, replacement, flags=re.DOTALL):
    """
    Update a specific JavaScript function in a file
    
    Args:
        file_path: Path to the JavaScript file
        function_name: Name of the function to update (e.g., 'Nt', 'It')
        update_pattern: Regex pattern to find within the function
        replacement: Replacement string or pattern
        flags: Regex flags
    
    Returns:
        True if successful, False otherwise
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Find the target function
        function_pattern = rf'(function {function_name}\(t\) \{{.*?\}}\s*\}};\s*\}})'
        function_match = re.search(function_pattern, content, flags=flags)
        
        if not function_match:
            logger.warning(f"Could not find function {function_name} in {file_path}")
            return False
        
        original_function = function_match.group(0)
        updated_function = re.sub(update_pattern, replacement, original_function, flags=flags)
        
        if original_function == updated_function:
            logger.info(f"No changes needed for function {function_name}")
            return True
        
        # Replace the function in the file content
        new_content = content.replace(original_function, updated_function)
        
        # Update the file
        safe_update_file(file_path, new_content)
        logger.info(f"Successfully updated function {function_name} in {file_path}")
        return True
    except Exception as e:
        logger.error(f"Error updating function {function_name}: {e}")
        return False

def find_function_name_by_usage(file_path, usage_pattern, flags=re.DOTALL):
    """
    Find a function name in minified JavaScript by looking for how it's used
    
    Args:
        file_path: Path to the JavaScript file
        usage_pattern: A regex pattern that identifies how the function is used
        flags: Regex flags
    
    Returns:
        The function name if found, None otherwise
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Look for function declarations and check for the usage pattern
        functions = re.findall(r'function ([A-Za-z0-9_]+)\([^)]*\)\s*\{', content)
        
        for func_name in functions:
            # Find this function's body
            func_pattern = rf'function {func_name}\([^)]*\)\s*\{{.*?\}}\s*\}};\s*\}}'
            func_match = re.search(func_pattern, content, flags=flags)
            
            if func_match and re.search(usage_pattern, func_match.group(0), flags=flags):
                logger.info(f"Found function '{func_name}' matching usage pattern")
                return func_name
                
        logger.warning(f"Could not find any function matching usage pattern")
        return None
    except Exception as e:
        logger.error(f"Error finding function by usage: {e}")
        return None

def locate_about_function(file_path):
    """Find the function that contains the about text"""
    # The about text typically contains this content
    about_usage = r'<p class="mb-3">A clone of <a href="[^"]+" title="Heardle">Heardle</a>'
    return find_function_name_by_usage(file_path, about_usage)

def locate_kofi_function(file_path):
    """Find the function that contains the Ko-fi link"""
    # Ko-fi links typically contain this structure
    kofi_usage = r'ko-fi\.com/[^"]+'
    return find_function_name_by_usage(file_path, kofi_usage)

def safe_string_replace(content, old_str, new_str, context_length=50):
    """
    Performs a safer string replacement with context validation
    
    Args:
        content: The string content to modify
        old_str: The string to replace
        new_str: The replacement string
        context_length: Number of characters of context to validate before/after
        
    Returns:
        The updated content if replacement was successful, or original content if unsafe
    """
    # Find all occurrences of the old string
    start_pos = 0
    positions = []
    
    while True:
        pos = content.find(old_str, start_pos)
        if pos == -1:
            break
        positions.append(pos)
        start_pos = pos + len(old_str)
    
    if not positions:
        return content  # No matches found
    
    # Process replacements from end to beginning (to preserve positions)
    positions.reverse()
    new_content = content
    
    for pos in positions:
        # Check the context around this match
        context_start = max(0, pos - context_length)
        context_end = min(len(content), pos + len(old_str) + context_length)
        
        before = content[context_start:pos]
        after = content[pos + len(old_str):context_end]
        
        # Perform the replacement
        test_content = new_content[:pos] + new_str + new_content[pos + len(old_str):]
        
        # Verify the replacement preserves syntax
        if check_js_syntax(test_content):
            new_content = test_content
            logger.info(f"Successfully replaced '{old_str}' at position {pos}")
        else:
            logger.warning(f"Skipped unsafe replacement at position {pos}")
    
    return new_content

def apply_updates(config):
    """Apply all updates to files based on configuration"""
    success = True
    
    if not APP_NAME:
        logger.error("Configuration not loaded correctly. Cannot proceed.")
        return False
    
    try:
        # Group updates in logical order
        if not update_app_name():
            logger.warning("Failed to update app name")
            success = False
        
        if not update_google_analytics():
            logger.warning("Failed to update Google Analytics")
            success = False
            
        if not update_favicon():
            logger.warning("Failed to update favicon")
            success = False
            
        if not update_colors():
            logger.warning("Failed to update colors")
            success = False
            
        if not update_html_content():
            logger.warning("Failed to update HTML content")
            success = False
            
        if not ensure_css_imports():
            logger.warning("Failed to ensure CSS imports")
            success = False
            
        if not update_ko_fi_link(config):
            logger.warning("Failed to update Ko-fi link")
            success = False
            
        if not update_about_text(config):
            logger.warning("Failed to update about text")
            success = False
        
        return success
    except Exception as e:
        logger.error(f"Error applying updates: {e}", exc_info=True)
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
    parser.add_argument('--safe-mode', action='store_true', help='Run in safe mode (more conservative updates)')
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
        
        # Apply updates based on flags
        success = True
        
        if not args.skip_app_name:
            if not update_app_name():
                logger.warning("Failed to update app name")
                success = False
        
        if not args.skip_ga:
            if not update_google_analytics():
                logger.warning("Failed to update Google Analytics")
                success = False
            
        if not args.skip_favicon:
            if not update_favicon():
                logger.warning("Failed to update favicon")
                success = False
            
        if not args.skip_colors:
            if not update_colors():
                logger.warning("Failed to update colors")
                success = False
            
        if not args.skip_html:
            if not update_html_content():
                logger.warning("Failed to update HTML content")
                success = False
            
        if not args.skip_css:
            if not ensure_css_imports():
                logger.warning("Failed to ensure CSS imports")
                success = False
            
        if not args.skip_ko_fi:
            if not update_ko_fi_link(config):
                logger.warning("Failed to update Ko-fi link")
                success = False
            
        if not args.skip_about:
            if not update_about_text(config):
                logger.warning("Failed to update about text")
                success = False
        
        if success:
            logger.info("\n✅ All customizations complete!")
            logger.info(f"Your Heardle is now available at: {GAME_URL}")
        else:
            logger.warning("\n⚠️ Some customizations were not applied. Check the logs for details.")
            logger.info(f"Your Heardle may still be available at: {GAME_URL}")
        
        return 0 if success else 1
    except Exception as e:
        logger.error(f"Error during customization: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 