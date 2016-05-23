# -*- coding: utf-8 -*-


def split_string(string, chunk_size):
    """
    Generator function that splits string into chunks.

    :param string: string to be split.
    :param chunk_size: size of a single chunk.
    :return: yields individual chunks.
    """
    if not isinstance(string, str):
        raise TypeError("string parameter must be an instance of str")
    if not isinstance(chunk_size, int):
        raise TypeError("chunk_size parameter must be an instance of int")

    for index in range(0, len(string), chunk_size):
        yield string[index:index + chunk_size]


def hex_string(string, byte_separator, chunk_separator, chunk_size):
    """
    Returns HEXized string.

    :param string: string to be converted to hex representation.
    :param byte_separator: string to be inserted in-between bytes.
    :param chunk_separator: string to be inserted in-between chunks.
    :param chunk_size: integer specifying the size of a single chunk (in bytes).
    :return: hexadecimal representation of the string.
    """
    if not isinstance(string, str):
        raise TypeError("string parameter must be an instance of str")
    if not isinstance(byte_separator, str):
        raise TypeError("byte_separator parameter must be an instance of str")
    if not isinstance(chunk_separator, str):
        raise TypeError("chunk_separator parameter must be an instance of str")
    if not isinstance(chunk_size, int):
        raise TypeError("chunk_size parameter must be an instance of int")
    if chunk_size < 2:
        raise ValueError("chunk_size must be greater than 1")

    return chunk_separator.join(
        [byte_separator.join(
            ["{0:02x}".format(ord(byte)) for byte in x]
        ) for x in split_string(string, chunk_size)]
    )


def safe_string(string, safe_char):
    """
    Replaces all non-printable characters with safe_char.

    :param string: string to be scanned for unprintable characters.
    :param safe_char: a single character string to be used in place of unsafe characters.
    :return: safe to print string.
    """
    if not isinstance(string, str):
        raise TypeError("string parameter must be an instance of str")
    if not isinstance(safe_char, str):
        raise TypeError("safe_char parameter must be an instance of str")
    if len(safe_char) != 1:
        raise ValueError("safe_char length must be 1")

    unsafe_char_codes = list(range(0, 32)) + [127]
    return "".join([char if ord(char) not in unsafe_char_codes else safe_char for char in string])
