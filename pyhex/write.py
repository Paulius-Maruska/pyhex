#!/usr/bin/python
# -*- coding: utf-8 -*-
from format import pyhex_format, pyhex_format_stream


def pyhex_write(string, start_address, output_stream):
    """
    Writes hexview formatted string to output stream.

    :param string: string to be represented in hexview format.
    :param start_address: integer representing a starting address.
    :param output_stream: stream to write output to.
    :return: None.
    """
    for row in pyhex_format(string, start_address):
        output_stream.write("{row}\n".format(row=row))


def pyhex_write_stream(input_stream, output_stream):
    """
    Writes hexview formatted data from input stream to output stream.

    :param input_stream: stream to read input from.
    :param output_stream: stream to write output to.
    :return: None.
    """
    for row in pyhex_format_stream(input_stream):
        output_stream.write("{row}\n".format(row=row))
