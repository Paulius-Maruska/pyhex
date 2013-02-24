#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
import StringIO
import pyhex


class TestPyHexWrite(unittest.TestCase):
    def test_writes_to_stream_correctly(self):
        string = "Lobster ALL the Fetish!?"
        stream = StringIO.StringIO()

        expected = "\n".join(pyhex.pyhex_format(string, 0)) + "\n"

        pyhex.pyhex_write(string, 0, stream)
        stream.seek(0)

        self.assertEqual(expected, stream.buf)


class TestPyHexWriteStream(unittest.TestCase):
    def test_writes_to_stream_correctly(self):
        string = "Lobster ALL the Fetish!?"
        stream_input = StringIO.StringIO(string)
        stream_output = StringIO.StringIO()

        expected = "\n".join(pyhex.pyhex_format_stream(stream_input)) + "\n"
        stream_input.seek(0)

        pyhex.pyhex_write_stream(stream_input, stream_output)
        stream_output.seek(0)
        self.assertEqual(expected, stream_output.buf)
