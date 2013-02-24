#!/usr/bin/python
# -*- coding: utf-8 -*-
from helper import split_string, hex_string, safe_string


def pyhex_format(string, start_address):
    """
    Generator function that yields individual lines formatted as hexview lines.

    :param string: string to be represented in hexview format.
    :param start_address: integer representing a starting address.
    :return: yields individual lines.
    """
    if not isinstance(string, str):
        raise TypeError('string parameter must be an instance of str')
    if not isinstance(start_address, int):
        raise TypeError('start_address parameter must be an instance of int')
    if start_address % 16 != 0:
        raise ValueError('start_address parameter must be a multiple of 16')

    for index, row in enumerate(split_string(string, 16)):
        yield '{address:010x}: {hex:<50} {safe}'.format(
            address=start_address + 16 * index,
            hex=hex_string(row, ' ', ' | ', 8),
            safe=safe_string(row, '.')
        )


def pyhex_format_stream(stream):
    """
    Generator function that yields individual lines formated as hexview lines.
    :param stream: stream to read original bytes from (should be opened as binary).
    :return: yields individual lines.
    """
    address = 0
    size = 16 * 100
    while True:
        chunk = stream.read(size)
        if chunk is not None and len(chunk) > 0:
            for row in pyhex_format(chunk, address):
                yield row
        else:
            break
        address += size
