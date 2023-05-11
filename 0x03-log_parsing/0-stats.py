#!/usr/bin/python3

"""Script that reads stdin line by line and computes metrics"""

import sys


def print_status(code_dict, total_size):
    """Prints the computed metrics"""
    print("Total file size: {:d}".format(total_size))
    for code in sorted(code_dict.keys()):
        if code_dict[code] != 0:
            print("{}: {:d}".format(code, code_dict[code]))


status_codes = {"200": 0, "301": 0, "400": 0,
                "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

count = 0
total_size = 0

try:
    for line in sys.stdin:
        if count != 0 and count % 10 == 0:
            print_status(status_codes, total_size)

        line_parts = line.split()
        count += 1

        try:
            file_size = int(line_parts[-1])
            total_size += file_size
        except Exception:
            pass

        try:
            status_code = line_parts[-2]
            if status_code in status_codes:
                status_codes[status_code] += 1
        except Exception:
            pass

    print_status(status_codes, total_size)

except KeyboardInterrupt:
    print_status(status_codes, total_size)
    raise
