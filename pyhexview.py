#!/usr/bin/python
# -*- coding: utf-8 -*-
from optparse import OptionParser
from sys import stdin, stdout
from pyhex import pyhex_write_stream


def opt_parser():
    """Creates OptionParser."""
    parser = OptionParser(version="pyhexview 1.0")
    parser.add_option("-f", "--file", dest="filename", help="file to read input from")
    return parser


def main():
    """Script logic."""
    parser = opt_parser()
    options, arguments = parser.parse_args()

    if options.filename is not None:
        with open(options.filename, "rb") as input_stream:
            pyhex_write_stream(input_stream, stdout)
    else:
        pyhex_write_stream(stdin, stdout)


if __name__ == "__main__":
    main()
