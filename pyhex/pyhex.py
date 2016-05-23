# -*- coding: utf-8 -*-
try:
    import io
except ImportError:
    import StringIO as io
import os


def write(stream, buffer, start_address=0, chunk_size=16, safe_char=ord('.')):
    """Formats given bytes as hexview and writes them to stream.

    :param stream: output stream.
    :param buffer: bytes to be formatted.
    :param start_address: address of the first byte in the buffer.
    :param chunk_size: how many bytes to show on a single line.
    :param safe_char: an ordinal code of a character to be used in place of non-printable characters.
    """
    chunk_start = 0
    chunk_address = start_address
    while chunk_start <= len(buffer):
        chunk_end = min(chunk_start + chunk_size, len(buffer))
        chunk = buffer[chunk_start:chunk_end]

        if len(chunk) > 0:
            hexview = io.StringIO()
            byteview = io.StringIO()
            for byte in chunk:
                if not isinstance(byte, int):
                    byte = ord(byte)
                hexview.write(u"%02x " % byte)
                if byte < 32 or byte == 127:
                    byte = safe_char
                char = chr(byte)
                byteview.write(u"%s" % char)
            for whitespace in range(0, chunk_size - (chunk_end - chunk_start)):
                hexview.write(u"   ")
                byteview.write(u" ")

            stream.write(u"%08x: %s| %s%s" % (chunk_address, hexview.getvalue(), byteview.getvalue(), os.linesep))

        chunk_start += chunk_size
        chunk_address += chunk_size


def format(buffer, start_address=0, chunk_size=16, safe_char=ord('.')):
    """Formats given bytes as hexview.

    :param buffer: bytes to be formatted.
    :param start_address: address of the first byte in the buffer.
    :param chunk_size: how many bytes to show on a single line.
    :param safe_char: an ordinal code of a character to be used in place of non-printable characters.
    :return: formatted bytes as a string.
    """
    formatted = io.StringIO()
    write(formatted, buffer, start_address, chunk_size, safe_char)
    return formatted.getvalue()
