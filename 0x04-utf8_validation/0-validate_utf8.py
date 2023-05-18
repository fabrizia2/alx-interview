#!/usr/bin/python3
"""determines if a given data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    # Variable to keep track of the number of remaining bytes for a character
    remaining_bytes = 0

    for byte in data:
        # Check if the current byte is a continuation byte (starts with "10")
        if remaining_bytes > 0 and (byte >> 6) == 0b10:
            remaining_bytes -= 1
        # Check if the current byte is the start of a new character
        elif remaining_bytes == 0:
            # Determine the number of bytes for the current character
            if (byte >> 7) == 0b0:
                remaining_bytes = 0  # Single-byte character
            elif (byte >> 5) == 0b110:
                remaining_bytes = 1  # Two-byte character
            elif (byte >> 4) == 0b1110:
                remaining_bytes = 2  # Three-byte character
            elif (byte >> 3) == 0b11110:
                remaining_bytes = 3  # Four-byte character
            else:
                return False  # Invalid byte for the start of a character
        else:
            return False  # Invalid continuation byte

    return remaining_bytes == 0
