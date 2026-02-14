#!/usr/bin/env python3
import argparse
import os
import random
import json
import shutil
from difflib import SequenceMatcher
from urllib.parse import urlparse
import unicodedata

REPO_ROOT = os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir)))
DEFAULT_INPUT = os.path.join(REPO_ROOT, "data", "songs.json")


def normalize_string(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ASCII", "ignore").decode("ASCII")
    return " ".join(s.lower().split())


def normalize_url(url: str) -> str:
    try:
        parsed = urlparse(url)
        path = parsed.path.rstrip("/")
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
            url1 = normalize_url(song1.get("url", ""))
            url2 = normalize_url(song2.get("url", ""))
            answer1 = song1.get("answer", "")
            answer2 = song2.get("answer", "")
            if (url1 and url2 and url1 == url2) or are_similar_answers(answer1, answer2, similarity_threshold):
                current_group.append(song2)
                processed.add(j)
        if len(current_group) > 1:
            groups.append(current_group)
    return groups


def shuffle_songs(
    input_file, remove_duplicates=True, use_seed=None, backup=False, show_duplicates=False, similarity_threshold=0.85
):
    if use_seed is not None:
        random.seed(use_seed)
        print(f"Using random seed: {use_seed}")

    if backup:
        try:
            previous_file = input_file + ".bak"
            shutil.copy2(input_file, previous_file)
            print(f"Saved backup as {os.path.relpath(previous_file, REPO_ROOT)}")
        except Exception as e:
            print(f"Warning: Failed to create backup: {e}")

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            songs = json.load(f)
    except Exception as e:
        print(f"Error reading JSON file {input_file}: {e}")
        return

    if not songs:
        print("Error: No songs found in the file.")
        return

    print(f"Found {len(songs)} songs in the file.")

    if show_duplicates or remove_duplicates:
        duplicate_groups = find_duplicate_groups(songs, similarity_threshold)
        print(f"Duplicate groups: {len(duplicate_groups)}")
        total_duplicates = sum(len(group) - 1 for group in duplicate_groups)
        print(f"Total duplicate entries: {total_duplicates}")

        if show_duplicates:
            for i, group in enumerate(duplicate_groups):
                print(f"\nGroup {i+1}:")
                for song in group:
                    print(f"  - {song.get('answer')} ({song.get('url')})")

    songs_to_shuffle = songs
    if remove_duplicates:
        filtered = []
        seen_urls = set()
        seen_answers = set()
        for song in songs:
            normalized_url = normalize_url(song.get("url", ""))
            normalized_answer = normalize_string(song.get("answer", ""))
            is_duplicate = False

            # Simple check against processed set
            if normalized_url in seen_urls:
                is_duplicate = True
            else:
                # Check for similar answers
                for seen_answer in seen_answers:
                    if are_similar_answers(normalized_answer, seen_answer, similarity_threshold):
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

    try:
        with open(input_file, "w", encoding="utf-8") as f:
            json.dump(songs_to_shuffle, f, indent=2, ensure_ascii=False)
        print(
            f"Successfully shuffled {len(songs_to_shuffle)} songs and updated {os.path.relpath(input_file, REPO_ROOT)}"
        )
    except Exception as e:
        print(f"Error writing to file {input_file}: {e}")


def main():
    parser = argparse.ArgumentParser(description="Shuffle songs in data/songs.json")
    parser.add_argument("--input", "-i", default=DEFAULT_INPUT, help="Input JSON file containing songs array")
    parser.add_argument(
        "--keep-duplicates", "-k", action="store_true", help="Keep duplicate songs (default: remove duplicates)"
    )
    parser.add_argument("--seed", "-s", type=int, help="Random seed for reproducible shuffling")
    parser.add_argument("--backup", "-b", action="store_true", help="Create an additional .bak backup file")
    parser.add_argument("--show-duplicates", "-d", action="store_true", help="Show duplicate songs")
    parser.add_argument(
        "--similarity-threshold", "-t", type=float, default=0.85, help="Similarity threshold (0.0..1.0)"
    )
    args = parser.parse_args()

    shuffle_songs(
        input_file=args.input,
        remove_duplicates=not args.keep_duplicates,
        use_seed=args.seed,
        backup=args.backup,
        show_duplicates=args.show_duplicates,
        similarity_threshold=args.similarity_threshold,
    )


if __name__ == "__main__":
    main()
