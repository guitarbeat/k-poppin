#!/usr/bin/env python3
import re
import random
import os
import argparse
from collections import Counter, defaultdict

def shuffle_songs(input_file, output_file, remove_duplicates=True, use_seed=None, backup=False, show_duplicates=False):
    """
    Shuffle the songs array in the JavaScript file while preserving the structure
    and avoiding commented-out songs.
    """
    # Set random seed if provided
    if use_seed is not None:
        random.seed(use_seed)
        print(f"Using random seed: {use_seed}")
    
    # Create backup if requested
    if backup:
        backup_file = f"{input_file}.bak"
        try:
            with open(input_file, 'r', encoding='utf-8') as src, open(backup_file, 'w', encoding='utf-8') as dst:
                dst.write(src.read())
            print(f"Created backup at {backup_file}")
        except Exception as e:
            print(f"Warning: Failed to create backup: {e}")
    
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
    
    # Analyze duplicates
    pair_counter = Counter()
    pair_locations = defaultdict(list)
    
    for song in songs:
        pair = (song["url"], song["answer"])
        pair_counter[pair] += 1
        pair_locations[pair].append(song["line_number"])
    
    # Count unique and duplicate songs
    unique_pairs = [pair for pair, count in pair_counter.items() if count == 1]
    duplicate_pairs = [pair for pair, count in pair_counter.items() if count > 1]
    
    print(f"Unique songs: {len(unique_pairs)}")
    print(f"Duplicate songs: {len(duplicate_pairs)} (appearing multiple times)")
    
    total_duplicates = sum(count - 1 for pair, count in pair_counter.items() if count > 1)
    print(f"Total duplicate entries: {total_duplicates}")
    
    # Show some of the most duplicated songs
    if duplicate_pairs:
        print("\nTop 5 most duplicated songs:")
        most_common = pair_counter.most_common(5)
        for (url, answer), count in most_common:
            if count > 1:  # Only show duplicates
                print(f"  - \"{answer}\" appears {count} times")
                
                # Show line numbers if requested
                if show_duplicates:
                    lines_info = sorted(pair_locations[(url, answer)])
                    if len(lines_info) > 10:
                        # Show first 5 and last 5 if there are many
                        line_display = ', '.join(map(str, lines_info[:5])) + ', ... , ' + ', '.join(map(str, lines_info[-5:]))
                    else:
                        line_display = ', '.join(map(str, lines_info))
                    print(f"    Line numbers: {line_display}")
    
    # Show all duplicates if requested
    if show_duplicates and duplicate_pairs:
        print("\nAll duplicate songs and their locations:")
        # Sort by number of occurrences (descending)
        for (url, answer), count in sorted(pair_counter.items(), key=lambda x: x[1], reverse=True):
            if count > 1:  # Only show duplicates
                lines_info = sorted(pair_locations[(url, answer)])
                if len(lines_info) > 10:
                    # Show first 5 and last 5 if there are many
                    line_display = ', '.join(map(str, lines_info[:5])) + ', ... , ' + ', '.join(map(str, lines_info[-5:]))
                else:
                    line_display = ', '.join(map(str, lines_info))
                print(f"  - \"{answer}\" appears {count} times at lines: {line_display}")
    
    # Process songs based on user options
    songs_to_shuffle = songs
    
    # Remove duplicates if requested
    if remove_duplicates:
        unique_songs = []
        seen_pairs = set()  # Store (url, answer) pairs
        
        for song in songs:
            # Create a tuple of (url, answer) as the unique identifier
            song_pair = (song["url"], song["answer"])
            
            if song_pair not in seen_pairs:
                seen_pairs.add(song_pair)
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
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(header)
        f.write(js_songs)
    
    print(f"Successfully shuffled {len(songs_to_shuffle)} songs and saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Shuffle songs in the songs.js file')
    parser.add_argument('--input', '-i', default='songs.js', help='Input JavaScript file containing songs array')
    parser.add_argument('--output', '-o', default='songs_shuffled.js', help='Output file path for shuffled songs')
    parser.add_argument('--keep-duplicates', '-k', action='store_true', help='Keep duplicate songs (default: remove duplicates)')
    parser.add_argument('--seed', '-s', type=int, help='Random seed for reproducible shuffling')
    parser.add_argument('--backup', '-b', action='store_true', help='Create a backup of the input file before processing')
    parser.add_argument('--show-duplicates', '-d', action='store_true', help='Show all duplicate songs and their line numbers')
    
    args = parser.parse_args()
    
    shuffle_songs(
        input_file=args.input,
        output_file=args.output,
        remove_duplicates=not args.keep_duplicates,
        use_seed=args.seed,
        backup=args.backup,
        show_duplicates=args.show_duplicates
    )

if __name__ == "__main__":
    main() 