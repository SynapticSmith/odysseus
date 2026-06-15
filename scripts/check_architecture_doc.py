#!/usr/bin/env python3
import sys

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

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: check_architecture_doc.py <path_to_md_file>")
        sys.exit(1)

    success = check_details_balance(sys.argv[1])
    sys.exit(0 if success else 1)
