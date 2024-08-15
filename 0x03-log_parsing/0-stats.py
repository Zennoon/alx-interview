#!/usr/bin/python3
"""
Contains:
    Global
    ======
    Script to read and parse input and display related statistics
    every 10 lines read or when CTRL+C is clicked
"""
import re


def print_stats(total_f_size, status_log):
    """Displays info about stats recorded until calling time"""
    print("File size: {}".format(total_f_size), flush=True)
    for stat_code, freq in sorted([*status_log.items()]):
        print("{}: {:d}".format(stat_code, freq), flush=True)


def validate_line(line):
    """
    Checks that the line is of the correct format
    """
    pattern = (
        r'\s*\S+\s*',
        r'\s*\[\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+\]',
        r'\s*"[^"]*"\s*',
        r'\s*(\S+)',
        r'\s*(\d+)'
    )
    info = None
    formt = '{}\\-{}{}{}{}\\s*'.format(*pattern)
    matched = re.fullmatch(formt, line.strip())
    if matched:
        splitted = line.split()
        info = [
            splitted[-2],
            splitted[-1]
        ]
    return info


def run():
    """Main function"""
    counter = 0
    status_log = dict()
    total_f_size = 0
    possible_codes = (
        '200', '301', '400', '401', '403', '404', '405', '500'
    )

    try:
        while True:
            line = input()
            counter += 1
            matched = validate_line(line)
            if matched:
                stat, f_size = matched
                if stat in possible_codes:
                    if stat in status_log:
                        status_log[stat] += 1
                    else:
                        status_log[stat] = 1
                total_f_size += int(f_size)
                if counter % 10 == 0:
                    print_stats(total_f_size, status_log)
    except (KeyboardInterrupt, EOFError):
        print_stats(total_f_size, status_log)


if __name__ == "__main__":
    run()
