#!/usr/bin/python3

""" Script that reads input from stdin line by line and computes metrics """

import sys


def print_status(code_counts, file_size):
    """ Prints information """
    print(f"File size: {file_size}")
    for code, count in sorted(code_counts.items()):
        if count != 0:
            print(f"{code}: {count}")


status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
"403": 0, "404": 0, "405": 0, "500": 0}

line_count = 0
file_size = 0

try:
    for line in sys.stdin:
        line_count += 1

        if line_count % 10 == 0:
            print_status(status_codes, file_size)

        parts = line.split()

        try:
            file_size += int(parts[-1])
        except (ValueError, IndexError):
            pass

        try:
            code = parts[-2]
            if code in status_codes:
                status_codes[code] += 1
        except IndexError:
            pass

    print_status(status_codes, file_size)

except KeyboardInterrupt:
    print_status(status_codes, file_size)
    raise
