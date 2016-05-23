import pyhex


def test_pyhex_format_formats_provided_byte_buffer_as_hexview():
    actual = pyhex.format(b"\t2345678")
    expected = "00000000: 09 32 33 34 35 36 37 38                         | .2345678        \n"
    assert actual == expected


def test_pyhex_format_with_custom_address():
    actual = pyhex.format(b"12345678", start_address=4)
    expected = "00000004: 31 32 33 34 35 36 37 38                         | 12345678        \n"
    assert actual == expected


def test_pyhex_format_with_custom_chunk_size():
    actual = pyhex.format(b"12345678", chunk_size=4)
    expected = "00000000: 31 32 33 34 | 1234\n00000004: 35 36 37 38 | 5678\n"
    assert actual == expected


def test_pyhex_format_with_custom_safe_char():
    actual = pyhex.format(b"\t2345678", safe_char=ord('?'))
    expected = "00000000: 09 32 33 34 35 36 37 38                         | ?2345678        \n"
    assert actual == expected
