#!/usr/bin/python3

"""
A method that determines if a given data set represents a
valid utf-8 encoding.
Return:
    True: if data is a valid utf-8 encoding
    False: if otherwise
    A character in UTF-8 can be 1 to 4 bytes long
The data set can contain multiple characters
The data will be represented by a list of integers
Each integer represents 1 byte of data, therefore you only need
to handle the 8 least significant bits of each integer
"""


def validUTF8(data):
    num_bytes = 0
    for byte in data:
        if num_bytes == 0:
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1
    return num_bytes == 0
