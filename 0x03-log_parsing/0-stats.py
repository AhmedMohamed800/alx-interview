#!/usr/bin/python3
"""Read output"""
import sys


if __name__ == '__main__':
    line_count = 0
    total_size = 0
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    status_count = {}

    def print_result(total_size, status_count):
        """print result"""
        print("File size: {:d}".format(total_size))
        for status_code in sorted(status_count):
            print("{}: {}".format(status_code, status_count[status_code]))

    try:
        for line in sys.stdin:
            parts = line.split()
            line_count += 1
            total_size += int(parts[8])
            if parts[7] in valid_codes:
                if parts[7] in status_count:
                    status_count[parts[7]] += 1
                else:
                    status_count[parts[7]] = 1
            if line_count % 10 == 0:
                print_result(total_size, status_count)
        print_result(total_size, status_count)
    except KeyboardInterrupt:
        print_result(total_size, status_count)
        raise
