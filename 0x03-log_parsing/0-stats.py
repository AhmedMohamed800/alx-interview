#!/usr/bin/python3
"""0-states"""
import sys


def print_result(total_size, status_count):
    print(f"File size: {total_size}")
    for status_code in sorted(status_count):
        print(f"{status_code}: {status_count[status_code]}")


try:
    line_count = 0
    total_size = 0
    status_count = {}
    for line in sys.stdin:
        parts = line.split()
        line_count += 1
        total_size += int(parts[8])
        if parts[7] in status_count:
            status_count[parts[7]] += 1
        else:
            status_count[parts[7]] = 1
        if line_count % 10 == 0:
            print_result(total_size, status_count)
except KeyboardInterrupt:
    print_result(total_size, status_count)
    raise
