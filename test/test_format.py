#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import StringIO
import pyhex


class TestPyHexFormat(unittest.TestCase):
    def test_formats_correctly(self):
        string = "Lobster ALL the Fetish!?"

        string0, string1 = pyhex.helper.split_string(string, 16)
        expected = "0000000000: {hex0:<50} {safe0}\n0000000010: {hex1:<50} {safe1}".format(
            hex0=pyhex.helper.hex_string(string0, " ", " | ", 8),
            safe0=pyhex.helper.safe_string(string0, "."),
            hex1=pyhex.helper.hex_string(string1, " ", " | ", 8),
            safe1=pyhex.helper.safe_string(string1, ".")
        )

        self.assertEqual(expected, "\n".join(pyhex.pyhex_format(string, 0)))

        expected = "0000000020: {hex0:<50} {safe0}0000000030: {hex1:<50} {safe1}".format(
            hex0=pyhex.helper.hex_string(string0, " ", " | ", 8),
            safe0=pyhex.helper.safe_string(string0, "."),
            hex1=pyhex.helper.hex_string(string1, " ", " | ", 8),
            safe1=pyhex.helper.safe_string(string1, ".")
        )

        self.assertEqual(expected, "".join(pyhex.pyhex_format(string, 32)))

    def test_raises_when_string_parameter_is_not_a_str(self):
        with self.assertRaises(TypeError):
            list(pyhex.pyhex_format(0, 0))

    def test_raises_when_start_address_parameter_is_not_an_int(self):
        with self.assertRaises(TypeError):
            list(pyhex.pyhex_format("Lobster ALL the Fetish!?", "foo"))

    def test_raises_when_start_address_parameter_is_not_a_multiple_of_16(self):
        with self.assertRaises(ValueError):
            list(pyhex.pyhex_format("Lobster ALL the Fetish!?", 3))

        with self.assertRaises(ValueError):
            list(pyhex.pyhex_format("Lobster ALL the Fetish!?", 21))


class TestPyHexFormatStream(unittest.TestCase):
    def test_formats_correctly(self):
        string = "Lobster ALL the Fetish!?"
        stream = StringIO.StringIO(string)

        self.assertEqual(list(pyhex.pyhex_format(string, 0)), list(pyhex.pyhex_format_stream(stream)))
