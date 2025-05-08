#!/usr/bin/python3
"""Reads stdin line by line and computes metrics:

    Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" \
    <status code> <file size>
    (if the format is not this one, the line must be skipped)
    After every 10 lines and/or a keyboard interruption (CTRL + C), \
    print these statistics from the beginning:
        - Total file size: File size: <total size>
        - where <total size> is the sum of all previous <file size> \
        (see input format above)
        - Number of lines by status code:
            - possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
            - if a status code doesn’t appear or is not an integer, \
            don’t print anything for this status code
            - format: <status code>: <number>
            - status codes should be printed in ascending order
"""

import sys
import re


def print_stats(total_size, status_code_occurrences):
    """Prints some stats from a web server log file

    Parameters:
        total_size (int): total size of the files logged
        status_code_occurrences (dict): contains the status code
        and the number of times it appears
    """

    print("File size: {}".format(total_size))
    for code, count in sorted(status_code_occurrences.items()):
        print("{}: {}".format(code, count))


def main():
    status_code_occurrences = {}
    total_size = 0
    line_count = 0
    possible_status_codes = ["200", "301", "400", "401",
                             "403", "404", "405", "500"]
    line_pattern = re.compile(
        r'^(?P<ip>\S+) - \[(?P<date>.*?)\] "GET /projects/260 HTTP/1.1" '
        r'(?P<status>\d{3}) (?P<size>\d+)$'
    )

    try:
        for line in sys.stdin:
            line = line.strip()
            match = line_pattern.match(line)

            # If the line matches the regular expression parse it

            if match:
                status_code = match.group('status')
                file_size = int(match.group('size'))
                total_size += file_size

                # If the status code section of the line is a possible status
                # code add it to the dictionary and increment the value.

                if status_code in possible_status_codes:
                    if status_code in status_code_occurrences.keys():
                        status_code_occurrences[status_code] += 1
                    else:
                        status_code_occurrences[status_code] = 1

            line_count += 1
            if line_count == 10:
                print_stats(total_size, status_code_occurrences)
                line_count = 0
    except KeyboardInterrupt:
        pass
    finally:
        print_stats(total_size, status_code_occurrences)


if __name__ == "__main__":
    main()
