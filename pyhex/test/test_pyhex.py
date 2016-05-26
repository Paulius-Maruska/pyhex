# -*- coding: utf-8 -*-
import io

import pyhex


def test_from_stream_creates_hex_view_from_a_given_stream():
    stream = io.BytesIO(b"1234567890")
    hv = pyhex.from_stream(stream)
    assert isinstance(hv, pyhex.HexView)
    assert hv.stream is stream


def test_from_buffer_creates_hex_view_from_a_given_byte_buffer():
    buffer = b"1234567890"
    hv = pyhex.from_buffer(buffer)
    assert isinstance(hv, pyhex.HexView)
    assert hv.stream.getvalue() == buffer


def test_format_stream_returns_fully_hex_formatted_contents_of_the_stream():
    stream = io.BytesIO(b"1234567890" * 2)
    formatted = pyhex.format_stream(stream)
    expected = ("00000000: 31 32 33 34 35 36 37 38  39 30 31 32 33 34 35 36 | 1234567890123456\n"
                "00000010: 37 38 39 30                                      | 7890\n")
    assert formatted == expected


def test_format_buffer_returns_fully_hex_formatted_contents_of_the_buffer():
    buffer = b"1234567890" * 2
    formatted = pyhex.format_buffer(buffer)
    expected = ("00000000: 31 32 33 34 35 36 37 38  39 30 31 32 33 34 35 36 | 1234567890123456\n"
                "00000010: 37 38 39 30                                      | 7890\n")
    assert formatted == expected


def test_format_file_returns_fully_hex_formatted_contents_of_the_file(tmpdir):
    file = tmpdir.mkdir("testing").join("binary.bin")
    file.write_binary(b"1234567890" * 2, True)
    formatted = pyhex.format_file(str(file))
    expected = ("00000000: 31 32 33 34 35 36 37 38  39 30 31 32 33 34 35 36 | 1234567890123456\n"
                "00000010: 37 38 39 30                                      | 7890\n")
    assert formatted == expected
