# -*- coding: utf-8 -*-
import io

from .hexview import HexView


def from_stream(stream,
                show_address=True,
                show_hex=True,
                show_value=True,
                start_address=0,
                bytes_per_line=16,
                bytes_per_group=8,
                safe_char=u".",
                unsafe_chars=tuple(range(32)) + (127,)):
    hv = HexView(stream, show_address, show_hex, show_value, start_address,
                 bytes_per_line, bytes_per_group, safe_char, unsafe_chars)
    return hv


def from_buffer(buffer,
                show_address=True,
                show_hex=True,
                show_value=True,
                start_address=0,
                bytes_per_line=16,
                bytes_per_group=8,
                safe_char=u".",
                unsafe_chars=tuple(range(32)) + (127,)):
    stream = io.BytesIO(buffer)
    return from_stream(stream, show_address, show_hex, show_value, start_address,
                       bytes_per_line, bytes_per_group, safe_char, unsafe_chars)


def format_stream(stream,
                  show_address=True,
                  show_hex=True,
                  show_value=True,
                  start_address=0,
                  bytes_per_line=16,
                  bytes_per_group=8,
                  safe_char=u".",
                  unsafe_chars=tuple(range(32)) + (127,)):
    output = io.StringIO()
    for line in from_stream(stream, show_address, show_hex, show_value, start_address,
                            bytes_per_line, bytes_per_group, safe_char, unsafe_chars):
        output.write(line)
        output.write(u"\n")
    return output.getvalue()


def format_buffer(buffer,
                  show_address=True,
                  show_hex=True,
                  show_value=True,
                  start_address=0,
                  bytes_per_line=16,
                  bytes_per_group=8,
                  safe_char=u".",
                  unsafe_chars=tuple(range(32)) + (127,)):
    stream = io.BytesIO(buffer)
    return format_stream(stream, show_address, show_hex, show_value, start_address,
                         bytes_per_line, bytes_per_group, safe_char, unsafe_chars)


def format_file(filename,
                show_address=True,
                show_hex=True,
                show_value=True,
                start_address=0,
                bytes_per_line=16,
                bytes_per_group=8,
                safe_char=u".",
                unsafe_chars=tuple(range(32)) + (127,)):
    with open(filename, "rb") as stream:
        return format_stream(stream, show_address, show_hex, show_value, start_address,
                             bytes_per_line, bytes_per_group, safe_char, unsafe_chars)
