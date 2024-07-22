#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    '''
        Method that determines if a given data set represents a valid
        encoding (UTF-8).
    '''
    number_bytes = 0

    detail_1 = 1 << 7
    detail_2 = 1 << 6

    for i in data:

        detail_byte = 1 << 7

        if number_bytes == 0:

            while detail_byte & i:
                number_bytes += 1
                detail_byte = detail_byte >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if not (i & detail_1 and not (i & detail_2)):
                return False

        number_bytes -= 1

    if number_bytes == 0:
        return True

    return False
