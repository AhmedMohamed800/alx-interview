#!/usr/bin/python3
"""0-states"""
import sys


if __name__ == '__main__':
    line_count = 0
    total_size = 0
    code = ["200", "301", "400", "401", "403", "404", "405", "500"]
    status_count = {c: 0 for c in code}

    def print_result(total_size, status_count):
        print("File size: {:d}".format(total_size))
        for key, value in sorted(status_count.items()):
            print("{}: {}".format(key, value))

    try:
        for line in sys.stdin:
            parts = line.split()
            line_count += 1
            total_size += int(parts[8])
            if parts[7] in status_count:
                status_count[parts[7]] += 1
            if line_count % 10 == 0:
                print_result(total_size, status_count)
        print_result(total_size, status_count)
    except KeyboardInterrupt:
        print_result(total_size, status_count)
        raise
