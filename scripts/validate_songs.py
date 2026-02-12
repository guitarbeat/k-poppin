#!/usr/bin/env python3
import os
import json
import sys

REPO_ROOT = os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir)))
SONGS_JSON = os.path.join(REPO_ROOT, 'data', 'songs.json')


def parse_songs_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON in {path}: {e}", file=sys.stderr)
        return []
    except Exception as e:
        print(f"Error reading {path}: {e}", file=sys.stderr)
        return []


def validate(entries):
    errors = []
    seen_url = {}
    seen_answer = {}
    for idx, e in enumerate(entries):
        u = e.get('url')
        a = e.get('answer')
        if not u:
            errors.append(f'Entry {idx+1}: missing url')
        if not a:
            errors.append(f'Entry {idx+1}: missing answer')
        if a and a.lstrip() and a.lstrip()[0].isdigit() and not a.startswith(' '):
            errors.append(f"Entry {idx+1}: answer starts with a digit; add a leading space -> '{a}'")
        if u in seen_url:
            errors.append(f'Duplicate URL at entries {seen_url[u]} and {idx+1}: {u}')
        else:
            seen_url[u] = idx+1
        if a in seen_answer:
            errors.append(f'Duplicate answer at entries {seen_answer[a]} and {idx+1}: {a}')
        else:
            seen_answer[a] = idx+1
    return errors


def main():
    if not os.path.exists(SONGS_JSON):
        print(f'Cannot find songs.json at {SONGS_JSON}', file=sys.stderr)
        return 2
    entries = parse_songs_json(SONGS_JSON)
    if not entries:
        print('No entries parsed from songs.json. Is the file empty or invalid?', file=sys.stderr)
        return 2
    errors = validate(entries)
    if errors:
        print('Validation issues found:\n')
        for e in errors:
            print(f'- {e}')
        print(f'\nChecked {len(entries)} entries.')
        return 1
    else:
        print(f'All good! Checked {len(entries)} entries. No duplicates or format issues found.')
        return 0


if __name__ == '__main__':
    sys.exit(main())
