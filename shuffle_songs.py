#!/usr/bin/env python3
import re
import random
import os
import argparse
import shutil
from collections import Counter, defaultdict
from urllib.parse import urlparse, unquote
from difflib import SequenceMatcher
import unicodedata

def normalize_string(s):
    """Normalize a string by removing accents, converting to lowercase, and removing extra whitespace."""
    # Remove accents and convert to ASCII
    s = unicodedata.normalize('NFKD', s).encode('ASCII', 'ignore').decode('ASCII')
    # Convert to lowercase and remove extra whitespace
    return ' '.join(s.lower().split())

def normalize_url(url):
    """Normalize a URL by removing protocol, www, trailing slashes, and query parameters."""
    try:
        # Parse the URL
        parsed = urlparse(url)
        # Get the path and remove trailing slashes
        path = parsed.path.rstrip('/')
        # Remove query parameters and fragments
        return path
    except:
        return url

def are_similar_answers(ans1, ans2, threshold=0.85):
    """Check if two answers are similar using string similarity ratio."""
    return SequenceMatcher(None, normalize_string(ans1), normalize_string(ans2)).ratio() >= threshold

def find_duplicate_groups(songs, similarity_threshold=0.85):
    """Find groups of similar songs based on URL and answer similarity."""
    groups = []
    processed = set()
    
    for i, song1 in enumerate(songs):
        if i in processed:
            continue
            
        current_group = [song1]
        processed.add(i)
        
        for j, song2 in enumerate(songs[i+1:], start=i+1):
            if j in processed:
                continue
                
            # Check URL similarity
            url1 = normalize_url(song1["url"])
            url2 = normalize_url(song2["url"])
            
            # Check answer similarity
            answer1 = song1["answer"]
            answer2 = song2["answer"]
            
            if (url1 == url2 or 
                are_similar_answers(answer1, answer2, similarity_threshold)):
                current_group.append(song2)
                processed.add(j)
        
        if len(current_group) > 1:
            groups.append(current_group)
    
    return groups

def shuffle_songs(input_file, output_file, remove_duplicates=True, use_seed=None, backup=False, show_duplicates=False, similarity_threshold=0.85):
    """
    Shuffle the songs array in the JavaScript file while preserving the structure
    and avoiding commented-out songs.
    """
    # Set random seed if provided
    if use_seed is not None:
        random.seed(use_seed)
        print(f"Using random seed: {use_seed}")
    
    # Create backup of the original file as previous_songs.js
    try:
        previous_file = "previous_songs.js"
        shutil.copy2(input_file, previous_file)
        print(f"Saved original file as {previous_file}")
    except Exception as e:
        print(f"Warning: Failed to create backup as {previous_file}: {e}")
    
    # Create additional backup if requested
    if backup:
        backup_file = f"{input_file}.bak"
        try:
            shutil.copy2(input_file, backup_file)
            print(f"Created additional backup at {backup_file}")
        except Exception as e:
            print(f"Warning: Failed to create additional backup: {e}")
    
    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find start and end of the songs array
    start_line = -1
    end_line = -1
    
    for i, line in enumerate(lines):
        if "let songs = [" in line:
            start_line = i
        if line.strip() == "];" or line.strip() == "]":
            end_line = i
            break
    
    if start_line == -1 or end_line == -1:
        print("Error: Could not find songs array in the file.")
        return
    
    # Extract header (comments at the beginning of the file)
    header = "".join(lines[:start_line])
    
    # Process songs line by line to handle all variations
    songs = []
    current_song = {}
    in_song = False
    song_start_line = -1
    
    # Updated patterns to handle both quoted and unquoted property names
    url_pattern = re.compile(r'(?:"url"|url)\s*:\s*"([^"]+)"')
    answer_pattern = re.compile(r'(?:"answer"|answer)\s*:\s*"([^"]+)"')
    
    for i in range(start_line + 1, end_line):
        line = lines[i].strip()
        
        # Skip comments and empty lines
        if line.startswith("//") or not line:
            continue
            
        # Start of a song object
        if line == "{" or line.startswith("{"):
            in_song = True
            current_song = {}
            song_start_line = i + 1  # Store 1-indexed line number
            continue
            
        # End of a song object
        if "}" in line:
            in_song = False
            if current_song.get("url") and current_song.get("answer"):
                current_song["line_number"] = song_start_line
                songs.append(current_song.copy())
            continue
            
        # Extract URL
        url_match = url_pattern.search(line)
        if url_match:
            current_song["url"] = url_match.group(1)
            continue
            
        # Extract answer
        answer_match = answer_pattern.search(line)
        if answer_match:
            current_song["answer"] = answer_match.group(1)
            continue
    
    if not songs:
        print("Error: Could not parse any songs from the file.")
        return
    
    print(f"Found {len(songs)} songs in the file.")
    
    # Find duplicate groups using enhanced detection
    duplicate_groups = find_duplicate_groups(songs, similarity_threshold)
    
    # Count unique and duplicate songs
    unique_songs = set()
    for group in duplicate_groups:
        for song in group:
            unique_songs.add((song["url"], song["answer"]))
    
    print(f"Unique songs: {len(unique_songs)}")
    print(f"Duplicate groups: {len(duplicate_groups)}")
    
    total_duplicates = sum(len(group) - 1 for group in duplicate_groups)
    print(f"Total duplicate entries: {total_duplicates}")
    
    # Show duplicate groups if requested
    if show_duplicates and duplicate_groups:
        print("\nDuplicate groups found:")
        for i, group in enumerate(duplicate_groups, 1):
            print(f"\nGroup {i} ({len(group)} entries):")
            for song in group:
                print(f"  - Line {song['line_number']}: \"{song['answer']}\"")
                print(f"    URL: {song['url']}")
    
    # Process songs based on user options
    songs_to_shuffle = songs
    
    # Remove duplicates if requested
    if remove_duplicates:
        unique_songs = []
        seen_urls = set()
        seen_answers = set()
        
        for song in songs:
            normalized_url = normalize_url(song["url"])
            normalized_answer = normalize_string(song["answer"])
            
            # Check if this song is similar to any we've seen
            is_duplicate = False
            for seen_url, seen_answer in zip(seen_urls, seen_answers):
                if (normalized_url == seen_url or 
                    are_similar_answers(normalized_answer, seen_answer, similarity_threshold)):
                    is_duplicate = True
                    break
            
            if not is_duplicate:
                seen_urls.add(normalized_url)
                seen_answers.add(normalized_answer)
                unique_songs.append(song)
        
        songs_to_shuffle = unique_songs
        print(f"\nRemoving duplicates, keeping {len(songs_to_shuffle)} unique songs.")
    else:
        print("\nKeeping all songs including duplicates.")
    
    # Shuffle the songs
    random.shuffle(songs_to_shuffle)
    
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Convert back to JavaScript format with consistent formatting
    js_songs = "let songs = [\n"
    for i, song in enumerate(songs_to_shuffle):
        js_songs += "  {\n"
        js_songs += f'    url: "{song["url"]}",\n'
        js_songs += f'    answer: "{song["answer"]}"\n'
        js_songs += "  }"
        if i < len(songs_to_shuffle) - 1:
            js_songs += ","
        js_songs += "\n"
    js_songs += "];"
    
    # Write the output file
    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(header)
        f.write(js_songs)
    
    print(f"Successfully shuffled {len(songs_to_shuffle)} songs and updated {input_file}")

def main():
    parser = argparse.ArgumentParser(description='Shuffle songs in the songs.js file')
    parser.add_argument('--input', '-i', default='songs.js', help='Input JavaScript file containing songs array')
    parser.add_argument('--output', '-o', help='Output file path for shuffled songs (default: overwrites input file)')
    parser.add_argument('--keep-duplicates', '-k', action='store_true', help='Keep duplicate songs (default: remove duplicates)')
    parser.add_argument('--seed', '-s', type=int, help='Random seed for reproducible shuffling')
    parser.add_argument('--backup', '-b', action='store_true', help='Create an additional .bak backup file')
    parser.add_argument('--show-duplicates', '-d', action='store_true', help='Show all duplicate songs and their line numbers')
    parser.add_argument('--similarity-threshold', '-t', type=float, default=0.85,
                      help='Similarity threshold for detecting duplicate answers (0.0 to 1.0, default: 0.85)')
    
    args = parser.parse_args()
    
    # If no output file is specified, use the input file
    output_file = args.output if args.output else args.input
    
    shuffle_songs(
        input_file=args.input,
        output_file=output_file,
        remove_duplicates=not args.keep_duplicates,
        use_seed=args.seed,
        backup=args.backup,
        show_duplicates=args.show_duplicates,
        similarity_threshold=args.similarity_threshold
    )

if __name__ == "__main__":
    main() 