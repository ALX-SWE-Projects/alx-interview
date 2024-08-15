#!/usr/bin/python3

import sys

def print_msg(dict_sc, total_file_size):
    """
    Print the accumulated statistics.
    Args:
        dict_sc: dict of status codes
        total_file_size: total of the file
    Returns:
        Nothing
    """
    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_file_size = 0
counter = 0
dict_sc = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        parsed_line = line.split()

        # Ensure the line has at least 2 elements for status code and file size
        if len(parsed_line) >= 2:
            counter += 1

            # File size is the last element in the original line, status code is second to last
            file_size = int(parsed_line[-1])
            code = parsed_line[-2]

            # Update total file size
            total_file_size += file_size

            # Update status code count if the code is valid
            if code in dict_sc:
                dict_sc[code] += 1

            # Print the stats after every 10 lines
            if counter == 10:
                print_msg(dict_sc, total_file_size)
                counter = 0

finally:
    # Print the final stats after the loop ends or on interruption
    print_msg(dict_sc, total_file_size)
