#!/usr/bin/env python3
import argparse
import os
import random
import re
import shutil
from difflib import SequenceMatcher
from urllib.parse import urlparse
import unicodedata

REPO_ROOT = os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir)))
DEFAULT_INPUT = os.path.join(REPO_ROOT, 'data', 'songs.js')


def normalize_string(s: str) -> str:
    s = unicodedata.normalize('NFKD', s).encode('ASCII', 'ignore').decode('ASCII')
    return ' '.join(s.lower().split())


def normalize_url(url: str) -> str:
    try:
        parsed = urlparse(url)
        path = parsed.path.rstrip('/')
        return path
    except Exception:
        return url


def are_similar_answers(ans1: str, ans2: str, threshold: float = 0.85) -> bool:
    return SequenceMatcher(None, normalize_string(ans1), normalize_string(ans2)).ratio() >= threshold


def find_duplicate_groups(songs, similarity_threshold=0.85):
    groups = []
    processed = set()
    for i, song1 in enumerate(songs):
        if i in processed:
            continue
        current_group = [song1]
        processed.add(i)
        for j, song2 in enumerate(songs[i + 1 :], start=i + 1):
            if j in processed:
                continue
            url1 = normalize_url(song1["url"]) 
            url2 = normalize_url(song2["url"]) 
            answer1 = song1["answer"]
            answer2 = song2["answer"]
            if url1 == url2 or are_similar_answers(answer1, answer2, similarity_threshold):
                current_group.append(song2)
                processed.add(j)
        if len(current_group) > 1:
            groups.append(current_group)
    return groups


def shuffle_songs(input_file, remove_duplicates=True, use_seed=None, backup=False, show_duplicates=False, similarity_threshold=0.85):
    if use_seed is not None:
        random.seed(use_seed)
        print(f"Using random seed: {use_seed}")

    try:
        previous_file = os.path.join(os.path.dirname(input_file), 'songs.archive.js')
        shutil.copy2(input_file, previous_file)
        print(f"Saved original file as {os.path.relpath(previous_file, REPO_ROOT)}")
    except Exception as e:
        print(f"Warning: Failed to create archive: {e}")

    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

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

    header = "".join(lines[:start_line])

    songs = []
    current_song = {}
    in_song = False
    song_start_line = -1
    url_pattern = re.compile(r'(?:"url"|url)\s*:\s*"([^"]+)"')
    answer_pattern = re.compile(r'(?:"answer"|answer)\s*:\s*"([^"]+)"')

    for i in range(start_line + 1, end_line):
        line = lines[i].strip()
        if line.startswith("//") or not line:
            continue
        if line == "{" or line.startswith("{"):
            in_song = True
            current_song = {}
            song_start_line = i + 1
            continue
        if "}" in line:
            in_song = False
            if current_song.get("url") and current_song.get("answer"):
                current_song["line_number"] = song_start_line
                songs.append(current_song.copy())
            continue
        url_match = url_pattern.search(line)
        if url_match:
            current_song["url"] = url_match.group(1)
            continue
        answer_match = answer_pattern.search(line)
        if answer_match:
            current_song["answer"] = answer_match.group(1)
            continue

    if not songs:
        print("Error: Could not parse any songs from the file.")
        return

    print(f"Found {len(songs)} songs in the file.")

    duplicate_groups = find_duplicate_groups(songs, similarity_threshold)
    unique_songs = set()
    for group in duplicate_groups:
        for song in group:
            unique_songs.add((song["url"], song["answer"]))
    print(f"Duplicate groups: {len(duplicate_groups)}")
    total_duplicates = sum(len(group) - 1 for group in duplicate_groups)
    print(f"Total duplicate entries: {total_duplicates}")

    songs_to_shuffle = songs
    if remove_duplicates:
        filtered = []
        seen_urls = set()
        seen_answers = set()
        for song in songs:
            normalized_url = normalize_url(song["url"]) 
            normalized_answer = normalize_string(song["answer"]) 
            is_duplicate = False
            for seen_url, seen_answer in zip(seen_urls, seen_answers):
                if normalized_url == seen_url or are_similar_answers(normalized_answer, seen_answer, similarity_threshold):
                    is_duplicate = True
                    break
            if not is_duplicate:
                seen_urls.add(normalized_url)
                seen_answers.add(normalized_answer)
                filtered.append(song)
        songs_to_shuffle = filtered
        print(f"Removing duplicates, keeping {len(songs_to_shuffle)} unique songs.")
    else:
        print("Keeping all songs including duplicates.")

    random.shuffle(songs_to_shuffle)

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

    with open(input_file, 'w', encoding='utf-8') as f:
        f.write(header)
        f.write(js_songs)

    print(f"Successfully shuffled {len(songs_to_shuffle)} songs and updated {os.path.relpath(input_file, REPO_ROOT)}")


def main():
    parser = argparse.ArgumentParser(description='Shuffle songs in data/songs.js')
    parser.add_argument('--input', '-i', default=DEFAULT_INPUT, help='Input JavaScript file containing songs array')
    parser.add_argument('--keep-duplicates', '-k', action='store_true', help='Keep duplicate songs (default: remove duplicates)')
    parser.add_argument('--seed', '-s', type=int, help='Random seed for reproducible shuffling')
    parser.add_argument('--backup', '-b', action='store_true', help='Create an additional .bak backup file')
    parser.add_argument('--show-duplicates', '-d', action='store_true', help='Show duplicate songs and their line numbers')
    parser.add_argument('--similarity-threshold', '-t', type=float, default=0.85, help='Similarity threshold (0.0..1.0)')
    args = parser.parse_args()

    shuffle_songs(
        input_file=args.input,
        remove_duplicates=not args.keep_duplicates,
        use_seed=args.seed,
        backup=args.backup,
        show_duplicates=args.show_duplicates,
        similarity_threshold=args.similarity_threshold,
    )


if __name__ == '__main__':
    main()