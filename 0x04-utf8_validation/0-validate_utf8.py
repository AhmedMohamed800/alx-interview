#!/usr/bin/python3
"""
0-validate_utf8
"""


def validUTF8(data):
    trail = 0

    for byte in data:
        byte = byte & 0xFF

        if trail == 0:
            if byte >> 7 == 0b0:
                continue
            elif byte >> 5 == 0b110:
                trail = 1
            elif byte >> 4 == 0b1110:
                trail = 2
            elif byte >> 3 == 0b11110:
                trail = 3
            else:
                return False
        else:
            if byte >> 6 == 0b10:
                trail -= 1
            else:
                return False

    return trail == 0
