#!/usr/bin/env python3
"""
Shuffle Songs Script

This script shuffles the songs in the songs.js file for the K-Pop Girl Group Heardle game.
It preserves the format of the file while randomizing the order of the songs.
"""

import json
import random
import re
import os
import argparse
from datetime import datetime

def extract_songs(file_path):
    """Extract song entries from the songs.js file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # First try to find the array of songs using regex
    match = re.search(r'let\s+songs\s*=\s*\[(.*?)\]', content, re.DOTALL)
    
    # If regex fails, try a more manual approach
    if not match:
        print("Could not find songs array using regex, trying manual extraction...")
        
        # Find the start of the songs array
        start_idx = content.find("let songs = [")
        if start_idx == -1:
            start_idx = content.find("let songs=[")
        
        if start_idx == -1:
            raise ValueError("Could not find the start of the songs array in the file")
        
        # Find the end of the songs array
        end_idx = content.find("]", start_idx)
        if end_idx == -1:
            raise ValueError("Could not find the end of the songs array in the file")
        
        # Extract the songs text
        songs_text = content[start_idx:end_idx+1]
        
        # Extract the header and footer
        header = content[:start_idx]
        footer = content[end_idx+1:]
        
        # Extract individual song objects
        song_objects = []
        current_song = ""
        brace_count = 0
        in_song = False
        
        for char in songs_text:
            if char == '{' and not in_song:
                in_song = True
                brace_count = 1
                current_song = "{"
            elif in_song:
                current_song += char
                if char == '{':
                    brace_count += 1
                elif char == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        # We've found a complete song object
                        song_objects.append(current_song.strip())
                        current_song = ""
                        in_song = False
        
        # Parse each song object
        songs = []
        for song_text in song_objects:
            # Extract url and answer using regex
            url_match = re.search(r'url:\s*"([^"]+)"', song_text)
            answer_match = re.search(r'answer:\s*"([^"]+)"', song_text)
            
            if url_match and answer_match:
                songs.append({
                    'url': url_match.group(1),
                    'answer': answer_match.group(1),
                    'original_text': song_text
                })
        
        return songs, header, footer
    
    # If regex worked, use the original approach
    songs_text = match.group(1)
    
    # Extract the header and footer
    header = content[:match.start(1)]
    footer = content[match.end(1):]
    
    # Extract individual song objects
    song_objects = []
    current_song = ""
    brace_count = 0
    in_song = False
    
    for char in songs_text:
        if char == '{' and not in_song:
            in_song = True
            brace_count = 1
            current_song = "{"
        elif in_song:
            current_song += char
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    # We've found a complete song object
                    song_objects.append(current_song.strip())
                    current_song = ""
                    in_song = False
    
    # Parse each song object
    songs = []
    for song_text in song_objects:
        # Extract url and answer using regex
        url_match = re.search(r'url:\s*"([^"]+)"', song_text)
        answer_match = re.search(r'answer:\s*"([^"]+)"', song_text)
        
        if url_match and answer_match:
            songs.append({
                'url': url_match.group(1),
                'answer': answer_match.group(1),
                'original_text': song_text
            })
    
    return songs, header, footer

def shuffle_songs(songs):
    """Shuffle the list of songs."""
    random.shuffle(songs)
    return songs

def write_songs_to_file(file_path, songs, header, footer):
    """Write the shuffled songs back to the file."""
    # Create the new content
    new_content = header + "[\n"
    
    # Add each song
    for i, song in enumerate(songs):
        new_content += f"  {song['original_text']}"
        if i < len(songs) - 1:
            new_content += ","
        new_content += "\n"
    
    new_content += "]" + footer
    
    # Write the new content to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

def main():
    parser = argparse.ArgumentParser(description='Shuffle songs in the songs.js file')
    parser.add_argument('--file', default='songs.js', help='Path to the songs.js file')
    parser.add_argument('--seed', type=int, help='Random seed for reproducibility')
    parser.add_argument('--backup', action='store_true', help='Create a backup of the original file')
    parser.add_argument('--fix', action='store_true', help='Fix the songs.js file format')
    args = parser.parse_args()
    
    # Set random seed if provided
    if args.seed is not None:
        random.seed(args.seed)
    else:
        # Use current timestamp as seed
        random.seed(datetime.now().timestamp())
    
    # Create backup if requested
    if args.backup:
        backup_path = f"{args.file}.bak"
        with open(args.file, 'r', encoding='utf-8') as src, open(backup_path, 'w', encoding='utf-8') as dst:
            dst.write(src.read())
        print(f"Created backup at {backup_path}")
    
    # Extract, shuffle, and write songs
    try:
        songs, header, footer = extract_songs(args.file)
        print(f"Extracted {len(songs)} songs from {args.file}")
        
        if len(songs) == 0:
            print("No songs were extracted. The file may be malformed.")
            if args.fix:
                print("Attempting to fix the file format...")
                # Try to fix the file format
                with open(args.file, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # Fix the unterminated string literal
                content = content.replace('let songs = [\n"', 'let songs = [\n')
                
                # Write the fixed content back to the file
                with open(args.file, 'w', encoding='utf-8') as file:
                    file.write(content)
                
                print("File format fixed. Please run the script again.")
            return 1
        
        shuffled_songs = shuffle_songs(songs)
        print("Songs shuffled successfully")
        
        write_songs_to_file(args.file, shuffled_songs, header, footer)
        print(f"Shuffled songs written to {args.file}")
        
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main()) 