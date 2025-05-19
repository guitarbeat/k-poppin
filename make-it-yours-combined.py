#!/usr/bin/env python3
import re, json, argparse, os, sys, shutil, datetime, logging
from urllib.request import urlretrieve
from functools import wraps

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger('customize_heardle')

# Embedded configuration data (from your-data.json)
DEFAULT_CONFIG = {}  # You'd keep your original DEFAULT_CONFIG here

# Global variables
APP_NAME = APP_DISPLAY_NAME = GLITCH_NAME = GAME_URL = ARTIST_NAME = GAME_NAME = ""
START_DATE = ""
GAME_COMMENTS = []
GOOGLE_ANALYTICS_ID = ""
NEW_FAVICON_URL = ""

def error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {e}", exc_info=True)
            return False
    return wrapper

def read_file(file_path):
    try:
        if not os.path.exists(file_path):
            logger.warning(f"File does not exist: {file_path}")
            return None
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        logger.error(f"Error reading file {file_path}: {e}")
        return None

def create_backup(file_path):
    if not os.path.exists(file_path): return
    backup_dir = 'backups'
    os.makedirs(backup_dir, exist_ok=True)
    backup_path = os.path.join(backup_dir, f"{os.path.basename(file_path)}.{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}")
    shutil.copy2(file_path, backup_path)
    logger.info(f"Created backup: {backup_path}")
    return backup_path

def check_js_syntax(js_content):
    brackets = {'(': ')', '[': ']', '{': '}'}
    stack, in_string, escaped = [], None, False
    
    for i, char in enumerate(js_content):
        if in_string:
            if escaped: escaped = False; continue
            if char == '\\': escaped = True; continue
            if char == in_string: in_string = None; continue
        elif char in ["'", '"']: in_string = char; continue
        elif char in brackets: stack.append(char)
        elif char in brackets.values():
            if not stack: return False
            last_open = stack.pop()
            if char != brackets.get(last_open): return False
    
    return not stack and not in_string

def safe_update_file(file_path, new_content):
    if not os.path.exists(file_path):
        logger.warning(f"File does not exist: {file_path}")
        return False
    
    with open(file_path, 'r') as file:
        original_content = file.read()
    
    if original_content == new_content:
        logger.info(f"No changes needed for {file_path}")
        return False
    
    if file_path.endswith('.js') and not check_js_syntax(new_content):
        logger.error(f"Cannot update {file_path}: The generated JavaScript has syntax errors")
        return False
    
    create_backup(file_path)
    with open(file_path, 'w') as file: file.write(new_content)
    logger.info(f"Updated {file_path}")
    return True

def update_file_with_patterns(file_path, patterns):
    content = read_file(file_path)
    if content is None: return False
    
    new_content = content
    for pattern_info in patterns:
        pattern, replacement = pattern_info[:2]
        count = pattern_info[2] if len(pattern_info) > 2 else 0
        new_content = re.sub(pattern, replacement, new_content, count=count)
    
    return safe_update_file(file_path, new_content)

def load_config(config_file=None):
    if config_file is None or config_file == 'default':
        logger.info("Using embedded default configuration")
        config = DEFAULT_CONFIG
    else:
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
        except Exception as e:
            raise Exception(f"Error loading config file: {e}")
    
    # Validate configuration
    required_sections = ['project', 'game_comments', 'appearance', 'analytics']
    for section in required_sections:
        if section not in config:
            raise ValueError(f"Missing required section '{section}' in config file")
    
    project_keys = ['app_name', 'app_display_name', 'glitch_name', 'game_url', 'artist_name', 'game_name', 'start_date']
    for key in project_keys:
        if key not in config['project']:
            raise ValueError(f"Missing required key '{key}' in project section")
    
    if len(config['game_comments']) < 7:
        raise ValueError(f"Need at least 7 game comments, found {len(config['game_comments'])}")
    
    if 'favicon_url' not in config['appearance']:
        raise ValueError("Missing required 'favicon_url' key in appearance section")
    
    # Map to global variables
    global APP_NAME, APP_DISPLAY_NAME, GLITCH_NAME, GAME_URL, ARTIST_NAME, GAME_NAME, START_DATE, GAME_COMMENTS, GOOGLE_ANALYTICS_ID, NEW_FAVICON_URL
    
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
    
    return config

def escape_js_string(content):
    return content.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n').replace('\r', '\\r')

def find_function_name_by_usage(file_path, usage_pattern, flags=re.DOTALL):
    content = read_file(file_path)
    if content is None: return None
    
    functions = re.findall(r'function ([A-Za-z0-9_]+)\([^)]*\)\s*\{', content)
    
    for func_name in functions:
        func_pattern = rf'function {func_name}\([^)]*\)\s*\{{(.*?)\}}\s*\}};\s*\}}'
        func_match = re.search(func_pattern, content, flags=flags)
        
        if func_match and re.search(usage_pattern, func_match.group(1), flags=flags):
            return func_name
    
    return None

# Function locators
locate_about_function = lambda file_path: find_function_name_by_usage(file_path, r'<p class="mb-3">A clone of <a href="[^"]+" title="Heardle">Heardle</a>')
locate_kofi_function = lambda file_path: find_function_name_by_usage(file_path, r'ko-fi\.com/[^"]+')

@error_handler
def update_app_name():
    main_patterns = [
        (r'const HEARDLE_GLITCH_NAME = ".*?";', f'const HEARDLE_GLITCH_NAME = "{GLITCH_NAME}";'),
        (r'const HEARDLE_URL = ".*?";', f'const HEARDLE_URL = "{GAME_URL}";'),
        (r'const HEARDLE_ARTIST = ".*?";', f'const HEARDLE_ARTIST = "{ARTIST_NAME}";'),
        (r'const HEARDLE_NAME = .*?;', f'const HEARDLE_NAME = "{GAME_NAME}";'),
        (r'const HEARDLE_START_DATE = ".*?";', f'const HEARDLE_START_DATE = "{START_DATE}";'),
        (r'startDate: ".*?"', f'startDate: "{START_DATE}"'),
        (r'copy\("https://heardle\.app', f'copy("{GAME_URL}')
    ]
    
    if len(GAME_COMMENTS) >= 7:
        for i, comment in enumerate(GAME_COMMENTS[:7]):
            main_patterns.append((r'gameComments\[\d+\] = ".*?";', f'gameComments[{i}] = "{escape_js_string(comment)}";', 1))
    
    html_patterns = [
        (r'<title>.*?</title>', f'<title>{APP_DISPLAY_NAME}</title>'),
        (r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{APP_DISPLAY_NAME}">'),
        (r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="{GAME_URL}">'),
        (r'<meta name="description" content=".*?">', f'<meta name="description" content="Guess the {ARTIST_NAME} song from the intro in as few tries as possible.">'),
        (r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="Guess the {ARTIST_NAME} song from the intro in as few tries as possible.">')
    ]
    
    return update_file_with_patterns('main.js', main_patterns) and update_file_with_patterns('index.html', html_patterns)

@error_handler
def update_google_analytics():
    content = read_file('index.html')
    if content is None: return False
    
    ga_script_pattern = r'<!-- Global site tag \(gtag\.js\) - Google Analytics -->[\s\S]*?<script async src="https://www\.googletagmanager\.com/gtag/js\?id=.*?">[\s\S]*?</script>[\s\S]*?<script>[\s\S]*?gtag\(\'config\', \'.*?\'\);[\s\S]*?</script>'
    
    if GOOGLE_ANALYTICS_ID:
        new_ga_script = f'''<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GOOGLE_ANALYTICS_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GOOGLE_ANALYTICS_ID}');
</script>'''
        
        new_content = re.sub(ga_script_pattern, new_ga_script, content) if re.search(ga_script_pattern, content) else re.sub(r'<head>', f'<head>\n{new_ga_script}', content)
    else:
        new_content = re.sub(ga_script_pattern, '', content)
    
    return safe_update_file('index.html', new_content)

@error_handler
def update_favicon():
    content = read_file('index.html')
    if content is None: return False
    
    favicon_pattern = r'<link rel="(?:shortcut icon|icon|apple-touch-icon)" (?:sizes=".*?" )?href=".*?">'
    matches = re.findall(favicon_pattern, content)
    if not matches: return False
    
    new_content = content
    for match in matches:
        rel_match = re.search(r'rel="([^"]+)"', match)
        sizes_match = re.search(r'sizes="([^"]+)"', match)
        
        if rel_match:
            rel = rel_match.group(1)
            sizes = sizes_match.group(1) if sizes_match else None
            new_link = f'<link rel="{rel}" {f"sizes=\"{sizes}\" " if sizes else ""}href="{NEW_FAVICON_URL}">'
            new_content = new_content.replace(match, new_link)
    
    return safe_update_file('index.html', new_content)

@error_handler
def update_html_content():
    patterns = [
        (r'<title>.*?</title>', f'<title>{APP_DISPLAY_NAME}</title>'),
        (r'<meta name="description" content=".*?">', f'<meta name="description" content="Guess the {ARTIST_NAME} song from the intro in as few tries as possible.">'),
        (r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{APP_DISPLAY_NAME}">'),
        (r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="Guess the {ARTIST_NAME} song from the intro in as few tries as possible.">'),
        (r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="{GAME_URL}">'),
        (r'<meta name="twitter:title" content=".*?">', f'<meta name="twitter:title" content="{APP_DISPLAY_NAME}">'),
        (r'<meta name="twitter:description" content=".*?">', f'<meta name="twitter:description" content="Guess the {ARTIST_NAME} song from the intro in as few tries as possible.">')
    ]
    return update_file_with_patterns('index.html', patterns)

@error_handler
def update_ko_fi_link(config):
    ko_fi_url = config['project'].get('ko_fi_url')
    if not ko_fi_url: return True
    
    content = read_file('main.js')
    if content is None: return False
    
    kofi_function = locate_kofi_function('main.js')
    if not kofi_function: return False
    
    pattern = r'(href=["\'](https://ko-fi\.com/[^\'"]+)["\'])'
    found = re.search(pattern, content)
    
    if found:
        old_url = found.group(2)
        new_content = content.replace(old_url, ko_fi_url)
        return safe_update_file('main.js', new_content) if content != new_content else True
    
    return False

@error_handler
def update_about_text(config):
    about_text = config['project'].get('about_text', f'<p class="mb-3">A clone of <a href="https://www.heardle.app" title="Heardle">Heardle</a> for {ARTIST_NAME} songs.</p>')
    
    content = read_file('main.js')
    if content is None: return False
    
    about_section = locate_about_function('main.js')
    if not about_section: return False
    
    pattern = r'(<p class="mb-3">.*?Heardle</a>.*?</p>)'
    found = re.search(pattern, content)
    
    if found:
        old_text = found.group(1)
        new_content = content.replace(old_text, about_text)
        return safe_update_file('main.js', new_content)
    
    return False

def check_required_files():
    required_files = ['main.js', 'index.html']
    missing_files = [file for file in required_files if not os.path.exists(file)]
    
    if missing_files:
        logger.error(f"Missing required files: {', '.join(missing_files)}")
        return False
    
    logger.info("All required files found")
    return True

@error_handler
def initialize_project():
    logger.info("Initializing new Heardle project...")
    
    try:
        base_url = DEFAULT_CONFIG['project'].get('repository_url', 'https://raw.githubusercontent.com/guitarbeat/k-poppin/main/')
    found = re.search(pattern, content)
    
    if found:
        old_text = found.group(1)
        new_content = content.replace(old_text, about_text)
        return safe_update_file('main.js', new_content)
    
    return False

def check_required_files():
    required_files = ['main.js', 'index.html', 'style/bundle.css', 'style/global.css']
    missing_files = [file for file in required_files if not os.path.exists(file)]
    
    if missing_files:
        logger.error(f"Missing required files: {', '.join(missing_files)}")
        return False
    
    logger.info("All required files found")
    return True

@error_handler
def initialize_project():
    logger.info("Initializing new Heardle project...")
    
    try:
        base_url = DEFAULT_CONFIG['project'].get('repository_url', 'https://raw.githubusercontent.com/guitarbeat/k-poppin/main/')
        if not base_url.endswith('/'): base_url += '/'
    except Exception:
        base_url = 'https://raw.githubusercontent.com/guitarbeat/k-poppin/main/'
    
    files_to_download = {
        'main.js': base_url + 'main.js',
        'index.html': base_url + 'index.html',
        'style/bundle.css': base_url + 'style/bundle.css',
        'style/global.css': base_url + 'style/global.css',
        'music-stuff/songs.js': base_url + 'music-stuff/songs.js'
    }
    
    for file_name, url in files_to_download.items():
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        try:
            logger.info(f"Downloading {file_name}")
            urlretrieve(url, file_name)
        except Exception as e:
            logger.error(f"Error downloading {file_name}: {e}")
    
    logger.info("Project initialization complete")
    return True

def main():
    parser = argparse.ArgumentParser(description='Customize your Heardle game')
    parser.add_argument('--config', '-c', type=str, help='Path to config JSON file')
    parser.add_argument('--skip-app-name', action='store_true')
    parser.add_argument('--skip-ga', action='store_true')
    parser.add_argument('--skip-favicon', action='store_true')
    parser.add_argument('--skip-colors', action='store_true')
    parser.add_argument('--skip-html', action='store_true')
    parser.add_argument('--skip-css', action='store_true')
    parser.add_argument('--skip-ko-fi', action='store_true')
    parser.add_argument('--skip-about', action='store_true')
    parser.add_argument('--verbose', '-v', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--init', action='store_true')
    args = parser.parse_args()
    
    if args.verbose: logger.setLevel(logging.DEBUG)
    if args.dry_run: logger.info("DRY RUN MODE - No changes will be made")
    if args.init: return 0 if initialize_project() else 1
    
    try:
        config = load_config(args.config if args.config else 'default')
        skip_config = config.get('skip_steps', {})
        
        if not args.dry_run and not check_required_files():
            return 1
        
        logger.info(f"Customizing Heardle for: {APP_DISPLAY_NAME}")
        
        if args.dry_run:
            logger.info(f"DRY RUN - Would customize with: App={APP_NAME}, Artist={ARTIST_NAME}, URL={GAME_URL}")
            return 0
        
        # Define and execute update tasks
        update_tasks = [
            (update_app_name, 'app_name', args.skip_app_name),
            (update_google_analytics, 'ga', args.skip_ga),
            (update_favicon, 'favicon', args.skip_favicon),
            (update_colors, 'colors', args.skip_colors),
            (update_html_content, 'html', args.skip_html),
            (ensure_css_imports, 'css', args.skip_css),
            (lambda: update_ko_fi_link(config), 'ko_fi', args.skip_ko_fi),
            (lambda: update_about_text(config), 'about', args.skip_about)
        ]
        
        failed_tasks = []
        for task_func, config_key, arg_skip in update_tasks:
            if not (arg_skip or skip_config.get(config_key, False)) and not task_func():
                failed_tasks.append(task_func.__name__)
        
        if not failed_tasks:
            logger.info(f"\n✅ All customizations complete! Your Heardle is now available at: {GAME_URL}")
            return 0
        else:
            logger.warning(f"\n⚠️ Some customizations failed: {', '.join(failed_tasks)}")
            return 1
            
    except Exception as e:
        logger.error(f"Error during customization: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
