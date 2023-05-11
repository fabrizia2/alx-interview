#!/usr/bin/python3

"""reads stdin line by line and computes metrics"""

import sys
import signal


# Initialize variables
total_size = 0
status_codes = {}


# Define a signal handler for KeyboardInterrupt
def signal_handler(signal, frame):
    """signal handler"""
    print_statistics()
    sys.exit(0)


# Function to print statistics
def print_statistics():
    """print statistics"""
    print("Total file size:", total_size)
    for code in sorted(status_codes.keys()):
        print(code, ":", status_codes[code])


# Register the signal handler for KeyboardInterrupt
signal.signal(signal.SIGINT, signal_handler)

# Read input lines
for line_number, line in enumerate(sys.stdin, start=1):
    line = line.strip()

    # Parse the line
    parts = line.split()
    if len(parts) < 7 or parts[6] not in
    ('200', '301', '400', '401', '403', '404', '405', '500'):
        continue

    try:
        file_size = int(parts[7])
    except ValueError:
        continue

    # Update total file size
    total_size += file_size

    # Update status code count
    status_code = parts[6]
    status_codes[status_code] = status_codes.get(status_code, 0) + 1

    # Print statistics every 10 lines
    if line_number % 10 == 0:
        print_statistics()

# Print final statistics
print_statistics()
