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
    """Handles CTRL+C interruption"""
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
    """Displays info about stats recorded until calling time"""
    sys.stdout.write("File size: {}\n".format(total_f_size))
    sys.stdout.flush()
    for stat_code, freq in sorted([*status_log.items()]):
        sys.stdout.write("{}: {}\n".format(stat_code, freq))
        sys.stdout.flush()


def validate_line(line):
    """
    Checks that the line is of the correct format
    """
    return pattern.match(line)


for line in sys.stdin:
    # counter += 1
    matched = validate_line(line.strip())
    if matched:
        counter += 1
        stat, f_size = matched[1], matched[2]
        try:
            if stat in status_log:
                status_log[int(stat)] += 1
            else:
                status_log[int(stat)] = 1
        except Exception:
            pass
        else:
            total_f_size += int(f_size)
        if counter % 10 == 0:
            print_stats()
