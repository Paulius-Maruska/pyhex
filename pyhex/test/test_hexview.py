# -*- coding: utf-8 -*-
import io

import pytest

import pyhex.hexview as ph


def test_hex_view_reasonable_defaults():
    hv = ph.HexView()

    assert hv.stream is None
    assert hv.show_address is True
    assert hv.show_hex is True
    assert hv.show_value is True
    assert hv.start_address == 0
    assert hv.bytes_per_line == 16
    assert hv.safe_char == "."
    assert hv.unsafe_chars == tuple(range(32)) + (127,)


def test_hex_view_can_be_iterated_over():
    stream = io.BytesIO(b"1234567890")
    hv = ph.HexView(stream)
    it = iter(hv)
    assert it is not None
    assert next(it) is not None
    assert pytest.raises(StopIteration, next, it)


def test_hex_view_iterator_returns_lines_of_text_that_are_formatted_hex_view_byte_chunks():
    stream = io.BytesIO(b"1234567890" * 3)
    hv = ph.HexView(stream)
    formatted = list(iter(hv))
    expected = [
        u"00000000: 31 32 33 34 35 36 37 38  39 30 31 32 33 34 35 36 | 1234567890123456",
        u"00000010: 37 38 39 30 31 32 33 34  35 36 37 38 39 30       | 78901234567890",
    ]
    assert formatted == expected


def test_hex_view_iterator_can_hide_address():
    stream = io.BytesIO(b"1234567890" * 3)
    hv = ph.HexView(stream, show_address=False)
    formatted = list(iter(hv))
    expected = [
        u"31 32 33 34 35 36 37 38  39 30 31 32 33 34 35 36 | 1234567890123456",
        u"37 38 39 30 31 32 33 34  35 36 37 38 39 30       | 78901234567890",
    ]
    assert formatted == expected


def test_hex_view_iterator_can_hide_hex():
    stream = io.BytesIO(b"1234567890" * 3)
    hv = ph.HexView(stream, show_hex=False)
    formatted = list(iter(hv))
    expected = [
        u"00000000: 1234567890123456",
        u"00000010: 78901234567890",
    ]
    assert formatted == expected


def test_hex_view_iterator_can_hide_value():
    stream = io.BytesIO(b"1234567890" * 3)
    hv = ph.HexView(stream, show_value=False)
    formatted = list(iter(hv))
    expected = [
        u"00000000: 31 32 33 34 35 36 37 38  39 30 31 32 33 34 35 36",
        u"00000010: 37 38 39 30 31 32 33 34  35 36 37 38 39 30      ",
    ]
    assert formatted == expected


def test_hex_view_can_use_custom_address():
    stream = io.BytesIO(b"1234567890" * 3)
    hv = ph.HexView(stream, start_address=0x1337)
    formatted = list(iter(hv))
    expected = [
        u"00001337: 31 32 33 34 35 36 37 38  39 30 31 32 33 34 35 36 | 1234567890123456",
        u"00001347: 37 38 39 30 31 32 33 34  35 36 37 38 39 30       | 78901234567890",
    ]
    assert formatted == expected


def test_hex_view_can_use_custom_bytes_per_line():
    stream = io.BytesIO(b"1234567890" * 3)
    hv = ph.HexView(stream, bytes_per_line=8)
    formatted = list(iter(hv))
    expected = [
        u"00000000: 31 32 33 34 35 36 37 38 | 12345678",
        u"00000008: 39 30 31 32 33 34 35 36 | 90123456",
        u"00000010: 37 38 39 30 31 32 33 34 | 78901234",
        u"00000018: 35 36 37 38 39 30       | 567890",
    ]
    assert formatted == expected


def test_hex_view_can_use_custom_bytes_per_group():
    stream = io.BytesIO(b"1234567890" * 3)
    hv = ph.HexView(stream, bytes_per_group=4)
    formatted = list(iter(hv))
    expected = [
        u"00000000: 31 32 33 34  35 36 37 38  39 30 31 32  33 34 35 36 | 1234567890123456",
        u"00000010: 37 38 39 30  31 32 33 34  35 36 37 38  39 30       | 78901234567890",
    ]
    assert formatted == expected


def test_hex_view_can_use_custom_safe_char():
    stream = io.BytesIO(b"1\t34567\n90" * 3)
    hv = ph.HexView(stream, safe_char=u"?")
    formatted = list(iter(hv))
    expected = [
        u"00000000: 31 09 33 34 35 36 37 0a  39 30 31 09 33 34 35 36 | 1?34567?901?3456",
        u"00000010: 37 0a 39 30 31 09 33 34  35 36 37 0a 39 30       | 7?901?34567?90",
    ]
    assert formatted == expected


def test_hex_view_can_use_custom_unsafe_chars():
    stream = io.BytesIO(b"1234567890" * 3)
    hv = ph.HexView(stream, unsafe_chars=(0x30, 0x35))
    formatted = list(iter(hv))
    expected = [
        u"00000000: 31 32 33 34 35 36 37 38  39 30 31 32 33 34 35 36 | 1234.6789.1234.6",
        u"00000010: 37 38 39 30 31 32 33 34  35 36 37 38 39 30       | 789.1234.6789.",
    ]
    assert formatted == expected


def test_hex_view_raises_when_trying_to_iterate_without_setting_stream_first():
    hv = ph.HexView()
    assert pytest.raises(ValueError, iter, hv)
