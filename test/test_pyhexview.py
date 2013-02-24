#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from os import remove
from subprocess import call
import pyhex


class TestPyHexView(unittest.TestCase):
    def setUp(self):
        self.text = "Lobster ALL the Fetish!?"
        self.input_file = "input_test.txt"
        self.output_file = "output_test.hex"

        with open(self.input_file, "w") as output_stream:
            output_stream.write(self.text)

    def tearDown(self):
        remove(self.input_file)
        remove(self.output_file)

    def test_prints_hexview_correctly_with_io_options(self):
        expected = "\n".join(pyhex.pyhex_format(self.text, 0)) + "\n"

        process = call(["python", "pyhexview.py", "-i", self.input_file, "-o", self.output_file])

        with open(self.output_file, "r") as input_stream:
            output_text = ''.join(input_stream.readlines())

        self.assertEqual(0, process)
        self.assertEqual(expected, output_text)
