#!/usr/bin/env python3
import sys
import os
import re

def check_details_balance(filepath):
    open_count = 0
    with open(filepath, 'r') as f:
        for line_num, line in enumerate(f, 1):
            if '<details>' in line:
                open_count += 1
            elif '</details>' in line:
                open_count -= 1

            if open_count < 0:
                print(f"Error at line {line_num}: unmatched </details>")
                return False

    if open_count > 0:
        print(f"Error: {open_count} unclosed <details> tags at EOF")
        return False

    print("All <details> tags are properly balanced.")
    return True

def get_all_repo_files():
    files = set()
    for root, dirs, filenames in os.walk('.'):
        if '.git' in root or '__pycache__' in root or 'node_modules' in root:
            continue
        for f in filenames:
            if f.endswith('.py') or f.endswith('.js') or f.endswith('.html') or f.endswith('.md'):
                path = os.path.join(root, f)[2:] # strip ./
                files.add(path)
    return files

def get_doc_mentioned_files(doc_path):
    with open(doc_path, 'r') as f:
        content = f.read()

    mentions = set(re.findall(r'`([a-zA-Z0-9_\-\./]+\.(?:py|js|html|md|css))`', content))
    mentions.update(re.findall(r'\*\*`([a-zA-Z0-9_\-\./]+\.(?:py|js|html|md|css))`\*\*', content))

    return mentions

def check_missing_files(filepath):
    repo_files = get_all_repo_files()
    doc_mentions = get_doc_mentioned_files(filepath)

    missing = []
    for file in sorted(repo_files):
        if file not in doc_mentions:
            if 'tests/' in file: continue
            if 'scripts/' in file: continue
            if 'docker/' in file: continue
            if '.github/' in file: continue
            if file == 'README.md' or file == 'ARCHITECTURE.md' or file == 'CONTRIBUTING.md': continue
            if file.startswith('docs/'): continue
            if file.startswith('companion/'): continue
            if file.startswith('static/lib/'): continue
            missing.append(file)

    if missing:
        print(f"Warning: Found {len(missing)} core files that are not documented in {filepath}:")
        for m in missing[:10]:
            print(f"  - {m}")
        if len(missing) > 10:
            print(f"  ... and {len(missing)-10} more.")
        # We don't necessarily want to fail CI just for a single new file, or maybe we do?
        # A good architectural check might just warn. The request says "make it better, mainly we need it to check the architecture document against the codebase structure and state, so that any codebase changes are easier to maintain".
        # Let's fail the build if there are missing files so that it enforces documentation updates.
        return False

    print("All core codebase files are documented.")
    return True

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: check_architecture_doc.py <path_to_md_file>")
        sys.exit(1)

    filepath = sys.argv[1]

    balance_ok = check_details_balance(filepath)
    missing_ok = check_missing_files(filepath)

    sys.exit(0 if (balance_ok and missing_ok) else 1)
