#!/usr/bin/python3
import sys
import re

"""
A script that reads stdin line by line and computes metrics
"""


def validateuser_Input(user_input: str) -> bool:
    """
    Validate the user_input to conform with the format
    """
    ip = r'^(\d{1,255}\.){3,3}\d{1,255} '
    mid = r'- \[.+] "GET \/projects\/260 HTTP\/1.1" '
    code = r'(200|301|400|401|403|404|405|500) \d+$'
    pat = ip + mid + code
    pattern = re.compile(pat)
    return re.match(pattern, user_input)


def get_sc_and_fs(user_input: str):
    """
    Get the status code and the file size from the validated user_input
    """
    splited = re.split(r'(\d+ \d+$)', user_input)
    status_code, file_size = re.split(' ', splited[1])
    return status_code, file_size


def print_all(file_size, status_codes):
    """
    Print the current total file size and the counts of status codes
    """
    print(f"File size: {file_size}")
    for status_code in sorted(status_codes):
        if not status_code.isnumeric():
            pass
        print(f"{status_code}: {status_codes.get(status_code)} ")


def log_parser():
    """
    The main function. Continue to loop until the Keyboard Interrupt is
    pressed
    """
    total_file_size = 0
    status_codes_count = {}
    loop_count = 0
    try:
        while (True):
            user_input = sys.stdin.readline()
            loop_count += 1
            if validateuser_Input(user_input) is None:
                user_input = sys.stdin.readline()
                continue
            status_code, file_size = get_sc_and_fs(user_input)
            total_file_size += int(file_size)
            if status_codes_count.get(status_code) is None:
                status_codes_count[status_code] = 0
            status_codes_count[status_code] += 1
            if loop_count == 10:
                print_all(total_file_size, status_codes_count)
                loop_count = 0
    except KeyboardInterrupt:
        print_all(total_file_size, status_codes_count)


if "__main__" == __name__:
    log_parser()
