#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2013 Paulius Maruška
import unittest
import pyhex


class TestSplitString(unittest.TestCase):
    def test_splits_string_into_chunks_of_given_size(self):
        string = "Lobster ALL the Fetish!?"
        split = list(pyhex.helper.split_string(string, 4))
        self.assertEqual(["Lobs", "ter ", "ALL ", "the ", "Feti", "sh!?"], split)

    def test_splits_string_into_chunks_even_when_length_is_not_a_multiple_of_chunk_size(self):
        string = "Lobster ALL the Fetish!?"
        split = list(pyhex.helper.split_string(string, 5))
        self.assertEqual(["Lobst", "er AL", "L the", " Feti", "sh!?"], split)

    def test_raises_when_string_parameter_is_not_a_str(self):
        with self.assertRaises(TypeError):
            list(pyhex.helper.split_string(0, 2))

    def test_raises_when_chunk_size_parameter_is_not_an_int(self):
        with self.assertRaises(TypeError):
            list(pyhex.helper.split_string("Lobster ALL the Fetish!?", "foo"))


class TestHexSeparator(unittest.TestCase):
    def test_hexes_the_string_using_given_separators(self):
        string = "\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F" \
                 "\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1A\x1B\x1C\x1D\x1E\x1F"
        expected = "00 01 02 03 04 05 06 07 | 08 09 0a 0b 0c 0d 0e 0f | " \
                   "10 11 12 13 14 15 16 17 | 18 19 1a 1b 1c 1d 1e 1f"
        actual = pyhex.helper.hex_string(string, " ", " | ", 8)
        self.assertEqual(expected, actual)

    def test_hexes_the_string_when_it_is_not_a_multiple_of_8(self):
        string = "\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09"
        expected = "00 01 02 03 04 05 06 07 | 08 09"
        actual = pyhex.helper.hex_string(string, " ", " | ", 8)
        self.assertEqual(expected, actual)

    def test_raises_when_string_parameter_is_not_a_str(self):
        with self.assertRaises(TypeError):
            pyhex.helper.hex_string(0, " ", " | ", 8)

    def test_raises_when_byte_separator_parameter_is_not_a_str(self):
        with self.assertRaises(TypeError):
            pyhex.helper.hex_string("Lobster ALL the Fetish!?", 1, " | ", 8)

    def test_raises_when_chunk_separator_parameter_is_not_a_str(self):
        with self.assertRaises(TypeError):
            pyhex.helper.hex_string("Lobster ALL the Fetish!?", " ", 1, 8)

    def test_raises_when_chunk_size_parameter_is_not_an_int(self):
        with self.assertRaises(TypeError):
            pyhex.helper.hex_string("Lobster ALL the Fetish!?", " ", " | ", "foo")

    def test_raises_when_chunk_size_parameter_is_less_than_2(self):
        with self.assertRaises(ValueError):
            pyhex.helper.hex_string("Lobster ALL the Fetish!?", " ", " | ", 1)

        with self.assertRaises(ValueError):
            pyhex.helper.hex_string("Lobster ALL the Fetish!?", " ", " | ", -1)


class TestSafeString(unittest.TestCase):
    def test_converts_control_characters_to_safe_char(self):
        string = "Lobster\x00ALL\x7Fthe\x13Fetish!?"
        self.assertEqual("Lobster.ALL.the.Fetish!?", pyhex.helper.safe_string(string, "."))

    def test_raises_when_string_parameter_is_not_a_str(self):
        with self.assertRaises(TypeError):
            pyhex.helper.safe_string(0, ".")

    def test_raises_when_safe_char_parameter_is_not_a_str(self):
        with self.assertRaises(TypeError):
            pyhex.helper.safe_string("Lobster ALL the Fetish!?", 0)

    def test_raises_when_safe_char_parameter_is_not_a_single_character(self):
        with self.assertRaises(ValueError):
            pyhex.helper.safe_string("Lobster ALL the Fetish!?", "><")

        with self.assertRaises(ValueError):
            pyhex.helper.safe_string("Lobster ALL the Fetish!?", "")
