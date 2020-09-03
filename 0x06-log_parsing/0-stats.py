#!/usr/bin/python3
"""
    Script that reads stdin line by line and computes metrics
"""
import sys


codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

file_size = 0
count_lines = 1


def parse_line(line):
    """
    parse_line: function that compute the line
    """
    try:
        parsed_line = line.split()
        status_code = parsed_line[-2]
        if status_code in codes.keys():
            codes[status_code] += 1
        return int(parsed_line[-1])
    except Exception:
        return 0


def print_codes():
    """
    print_codes: function that print the codes and his count
    """
    print("File size: {}".format(file_size))
    for key in sorted(codes.keys()):
        if codes[key]:
            print("{}: {}".format(key, codes[key]))


if __name__ == "__main__":
    try:
        for line in sys.stdin:
            file_size += parse_line(line)
            if count_lines % 10 == 0:
                print_codes()
            count_lines += 1
    except KeyboardInterrupt:
        print_codes()
        raise
    print_codes()
