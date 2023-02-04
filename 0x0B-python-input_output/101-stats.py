#!/usr/bin/python3
""" 101-stats """
import sys


def print_stats(total_file_size, status_codes_count):
    """
    print the parsed stats
    Args:
        total_file_size (int): the total file size
        status_codes_count (int): dictionary of status codes and their counts
    """
    print("File size: {}".format(total_file_size))
    for status_code, count in status_codes_count.items():
        if count > 0:
            print("{}: {}".format(status_code, count))


def main():
    """ main routine """
    total_file_size = 0
    line_count = 0
    status_codes_count = {"200": 0, "301": 0, "400": 0, "401": 0,
                          "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        for line in sys.stdin:
            split_line = line.split(" ")
            try:
                file_size = int(split_line[-1])
                status_code = split_line[-2]
                total_file_size += file_size
                status_codes_count[status_code] += 1
                line_count += 1
                if line_count % 10 == 0:
                    print_stats(total_file_size, status_codes_count)
            except (ValueError, KeyError):
                pass
        print_stats(total_file_size, status_codes_count)
    except KeyboardInterrupt:
        print_stats(total_file_size, status_codes_count)
    sys.exit(0)


if __name__ == "__main__":
    main()
