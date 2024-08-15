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


def validate_line(line, pattern):
    """
    Checks that the line is of the correct format
    """
    return pattern.match(line)


def run():
    """Main function"""
    counter = 0
    status_log = dict()
    total_f_size = 0
    pattern = re.compile(
        r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3} - \[.*\] "
        + r"\"GET /projects/260 HTTP/1.1\" ([0-9]{3}) ([0-9]+)"
    )
    possible_codes = ('200', '301', '400', '401', '403', '404', '405', '500')

    try:
        while True:
            line = input()
            counter += 1
            matched = validate_line(line.strip(), pattern)
            if matched:
                stat, f_size = matched[1], matched[2]
                try:
                    if stat in possible_codes:
                        if stat in status_log:
                            status_log[stat] += 1
                        else:
                            status_log[stat] = 1
                except Exception:
                    pass
                else:
                    total_f_size += int(f_size)
                if counter % 10 == 0:
                    print_stats(total_f_size, status_log)
    except (KeyboardInterrupt, EOFError):
        print_stats(total_f_size, status_log)


if __name__ == "__main__":
    run()
