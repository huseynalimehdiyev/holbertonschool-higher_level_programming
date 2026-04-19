#!/usr/bin/python3
"""Shebang"""

import sys


def print_stats(total_size, status_counts):
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))


def main():
    total_size = 0
    line_count = 0

    valid_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    status_counts = {}

    try:
        for line in sys.stdin:
            parts = line.split()

            if len(parts) < 2:
                continue

            # Extract file size
            try:
                size = int(parts[-1])
                total_size += size
            except:
                pass

            # Extract status code
            code = parts[-2]
            if code in valid_codes:
                status_counts[code] = status_counts.get(code, 0) + 1

            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

    # Final print after EOF
    print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()