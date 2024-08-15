#!/usr/bin/python3
"""
Contains:
    Global
    ======
    Script to read and parse input and display related statistics
    every 10 lines read or when CTRL+C is clicked
"""
import re
import signal
import sys


def handler(signum, frame):
    print_stats()


signal.signal(signal.SIGINT, handler)

counter = 0
status_log = dict()
total_f_size = 0
pattern = re.compile(
    r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3} - \[.*\] "
    + r"\"GET /projects/260 HTTP/1.1\" ([0-9]{3}) ([0-9]+)"
)


def print_stats():
    print("File size: {}".format(total_f_size))
    for stat_code, freq in sorted([*status_log.items()]):
        print("{}: {}".format(stat_code, freq))


def validate_line(line):
    """
    Checks that the line is of the correct format
    """
    return pattern.match(line)


if __name__ == "__main__":
    for line in sys.stdin:
        counter += 1
        matched = validate_line(line.strip())
        if matched:
            # counter += 1
            stat, f_size = matched[1], matched[2]
            if stat in status_log:
                status_log[stat] += 1
            else:
                status_log[stat] = 1
            total_f_size += int(f_size)
            if counter % 10 == 0:
                print_stats()
