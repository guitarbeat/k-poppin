#!/usr/bin/env python3
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir)))
SONGS_JS = os.path.join(REPO_ROOT, 'data', 'songs.js')

URL_RE = re.compile(r'\burl\s*:\s*"([^"]+)"')
ANSWER_RE = re.compile(r'\banswer\s*:\s*"([^"]+)"')


def parse_songs_js(path):
    entries = []
    url, answer = None, None
    with open(path, 'r', encoding='utf-8') as f:
        for raw_line in f:
            line = raw_line.strip()
            if line.startswith('//'):
                continue
            mu = URL_RE.search(line)
            if mu:
                url = mu.group(1).strip()
            ma = ANSWER_RE.search(line)
            if ma:
                answer = ma.group(1).strip()
            if url and answer:
                entries.append({'url': url, 'answer': answer})
                url, answer = None, None
    return entries


def validate(entries):
    errors = []
    seen_url = {}
    seen_answer = {}
    for idx, e in enumerate(entries):
        u = e['url']
        a = e['answer']
        if not u:
            errors.append(f'Entry {idx+1}: missing url')
        if not a:
            errors.append(f'Entry {idx+1}: missing answer')
        if a and a[0].isdigit():
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
    if not os.path.exists(SONGS_JS):
        print(f'Cannot find songs.js at {SONGS_JS}', file=sys.stderr)
        return 2
    entries = parse_songs_js(SONGS_JS)
    if not entries:
        print('No entries parsed from songs.js. Has the format changed?', file=sys.stderr)
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