# -*- coding: utf-8 -*-
import argparse
import os
import sys

from .functions import format_file


def to_unicode_character(value):
    return u"%s" % value[:1]


def get_version(fmt="%%(prog)s %(version)s"):
    my_path = os.path.abspath(__file__)
    my_dir = os.path.dirname(my_path)
    pyhex_init_path = os.path.join(my_dir, "__init__.py")
    with open(pyhex_init_path) as f:
        for line in f.readlines():
            if "__version__" in line:
                version = line.strip().split("=")[-1].strip(" '\"")
                return fmt % {'version': version}
    raise ValueError("could not find version")


def get_argument_parser(prog=u"pyhex", description=u"Quickly view hex-view representation of binary files."):
    parser = argparse.ArgumentParser(prog, description=description)
    parser.add_argument("--version",
                        action="version",
                        version=get_version())
    parser.add_argument("-a", "--no-address",
                        action="store_true",
                        default=False,
                        dest="no_address",
                        help=u"Don't show address.")
    parser.add_argument("-e", "--no-hex",
                        action="store_true",
                        default=False,
                        dest="no_hex",
                        help=u"Don't show HEX.")
    parser.add_argument("-v", "--no-value",
                        action="store_true",
                        default=False,
                        dest="no_value",
                        help=u"Don't show value.")
    parser.add_argument("-s", "--start-address",
                        action="store",
                        type=int,
                        default=0,
                        metavar="ADDR",
                        dest="start_address",
                        help=u"A number to start addressing bytes from.")
    parser.add_argument("-l", "--bytes-per-line",
                        action="store",
                        type=int,
                        default=16,
                        metavar="NUM",
                        dest="bytes_per_line",
                        help=u"Number of bytes per line.")
    parser.add_argument("-g", "--bytes-per-group",
                        action="store",
                        type=int,
                        default=8,
                        metavar="NUM",
                        dest="bytes_per_group",
                        help=u"Number of bytes per group.")
    parser.add_argument("-c", "--safe-char",
                        action="store",
                        type=to_unicode_character,
                        default=u".",
                        metavar="CHAR",
                        dest="safe_char",
                        help=u"Character to show in place of non-printable characters.")
    parser.add_argument("file",
                        action="store",
                        required=True,
                        dest="file",
                        help=u"File to read bytes from.")
    return parser


def main(argv=None):
    if not argv:
        argv = sys.argv
    argument_parser = get_argument_parser()
    parsed = argument_parser.parse_args(argv[1:])

    format_file(parsed.file, not parsed.no_address, not parsed.no_hex, not parsed.no_value,
                parsed.start_address, parsed.bytes_per_line, parsed.bytes_per_group, parsed.safe_char)
    return 0
