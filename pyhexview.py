#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2013 Paulius Maruška
from optparse import OptionParser
from sys import stdin, stdout
from pyhex import pyhex_write_stream


def opt_parser():
    """Creates OptionParser."""
    parser = OptionParser(version="pyhexview 1.0")
    parser.add_option("-i", "--input-file", dest="input_file", help="file to read input from")
    parser.add_option("-o", "--output-file", dest="output_file", help="file to write output to")
    return parser


def main():
    """Script logic."""
    parser = opt_parser()
    options, arguments = parser.parse_args()

    input_stream = stdin
    output_stream = stdout

    if options.input_file is not None:
        input_stream = open(options.input_file, "rb")
    if options.output_file is not None:
        output_stream = open(options.output_file, "w")

    with input_stream, output_stream:
        pyhex_write_stream(input_stream, output_stream)


if __name__ == "__main__":
    main()
