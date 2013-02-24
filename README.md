PyHex
=====

[![Build Status](https://travis-ci.org/Paulius-Maruska/pyhex.png?branch=master)](https://travis-ci.org/Paulius-Maruska/pyhex)

Python package for easy printing of strings as hexview strings.

PyHexView
=========

Command-Line utility script, that prints contents of a file or whatever is read from the standard input formated as
hexview.

Code Examples for Format Functions
==================================

Formatting a string:

    from pyhex import pyhex_format

    string = "Lobster ALL the Fetish!?"
    hex = "\n".join(pyhex_format(string, 0))
    print hex

Output:

    0000000000: 4c 6f 62 73 74 65 72 20 | 41 4c 4c 20 74 68 65 20  Lobster ALL the
    0000000010: 46 65 74 69 73 68 21 3f                            Fetish!?

Formatting an entire file:

    from pyhex import pyhex_format_stream

    with open("example.txt", "rb") as stream:
        hex = "\n".join(pyhex_format_stream(stream)))
    print hex

If the contents of "example.txt" are:

    Lobster ALL the Fetish!?

    Ah yes! We like to lobster our fetish!

Output:

    0000000000: 4c 6f 62 73 74 65 72 20 | 41 4c 4c 20 74 68 65 20  Lobster ALL the
    0000000010: 46 65 74 69 73 68 21 3f | 0a 0a 41 68 20 79 65 73  Fetish!?..Ah yes
    0000000020: 21 20 57 65 20 6c 69 6b | 65 20 74 6f 20 6c 6f 62  ! We like to lob
    0000000030: 73 74 65 72 20 6f 75 72 | 20 66 65 74 69 73 68 21  ster our fetish!
    0000000040: 0a                                                 .

Code Examples for Write Functions
==================================

Printing a converted string:

    from sys import stdout
    from pyhex import pyhex_write

    string = "Lobster ALL the Fetish!?"
    pyhex_write(string, 0, stdout))

Output:

    0000000000: 4c 6f 62 73 74 65 72 20 | 41 4c 4c 20 74 68 65 20  Lobster ALL the
    0000000010: 46 65 74 69 73 68 21 3f                            Fetish!?

Printing an entire file:

    from sys import stdout
    from pyhex import pyhex_format_stream

    with open("example.txt", "rb") as input_stream:
        pyhex_write_stream(stream, stdout))

If the contents of "example.txt" are:

    Lobster ALL the Fetish!?

    Ah yes! We like to lobster our fetish!

Output:

    0000000000: 4c 6f 62 73 74 65 72 20 | 41 4c 4c 20 74 68 65 20  Lobster ALL the
    0000000010: 46 65 74 69 73 68 21 3f | 0a 0a 41 68 20 79 65 73  Fetish!?..Ah yes
    0000000020: 21 20 57 65 20 6c 69 6b | 65 20 74 6f 20 6c 6f 62  ! We like to lob
    0000000030: 73 74 65 72 20 6f 75 72 | 20 66 65 74 69 73 68 21  ster our fetish!
    0000000040: 0a                                                 .

Examples of pyhexview.py Usage
==============================

View .gitattributes code formatted as hexview:

    $> python pyhexview.py -i .gitattributes
    0000000000: 23 20 41 75 74 6f 20 64 | 65 74 65 63 74 20 74 65  # Auto detect te
    0000000010: 78 74 20 66 69 6c 65 73 | 20 61 6e 64 20 70 65 72  xt files and per
    0000000020: 66 6f 72 6d 20 4c 46 20 | 6e 6f 72 6d 61 6c 69 7a  form LF normaliz
    0000000030: 61 74 69 6f 6e 0d 0a 2a | 20 74 65 78 74 3d 61 75  ation..* text=au
    0000000040: 74 6f 0d 0a 0d 0a 23 20 | 53 74 61 6e 64 61 72 64  to....# Standard
    0000000050: 20 74 6f 20 6d 73 79 73 | 67 69 74 0d 0a 2a 2e 64   to msysgit..*.d
    0000000060: 6f 63 09 20 64 69 66 66 | 3d 61 73 74 65 78 74 70  oc. diff=astextp
    0000000070: 6c 61 69 6e 0d 0a 2a 2e | 44 4f 43 09 20 64 69 66  lain..*.DOC. dif
    0000000080: 66 3d 61 73 74 65 78 74 | 70 6c 61 69 6e 0d 0a 2a  f=astextplain..*
    0000000090: 2e 64 6f 63 78 20 64 69 | 66 66 3d 61 73 74 65 78  .docx diff=astex
    00000000a0: 74 70 6c 61 69 6e 0d 0a | 2a 2e 44 4f 43 58 20 64  tplain..*.DOCX d
    00000000b0: 69 66 66 3d 61 73 74 65 | 78 74 70 6c 61 69 6e 0d  iff=astextplain.
    00000000c0: 0a 2a 2e 64 6f 74 20 20 | 64 69 66 66 3d 61 73 74  .*.dot  diff=ast
    00000000d0: 65 78 74 70 6c 61 69 6e | 0d 0a 2a 2e 44 4f 54 20  extplain..*.DOT
    00000000e0: 20 64 69 66 66 3d 61 73 | 74 65 78 74 70 6c 61 69   diff=astextplai
    00000000f0: 6e 0d 0a 2a 2e 70 64 66 | 20 20 64 69 66 66 3d 61  n..*.pdf  diff=a
    0000000100: 73 74 65 78 74 70 6c 61 | 69 6e 0d 0a 2a 2e 50 44  stextplain..*.PD
    0000000110: 46 09 20 64 69 66 66 3d | 61 73 74 65 78 74 70 6c  F. diff=astextpl
    0000000120: 61 69 6e 0d 0a 2a 2e 72 | 74 66 09 20 64 69 66 66  ain..*.rtf. diff
    0000000130: 3d 61 73 74 65 78 74 70 | 6c 61 69 6e 0d 0a 2a 2e  =astextplain..*.
    0000000140: 52 54 46 09 20 64 69 66 | 66 3d 61 73 74 65 78 74  RTF. diff=astext
    0000000150: 70 6c 61 69 6e 0d 0a                               plain..

Same as before, but read it from standard input:

    $> python pyhexview.py < .gitattributes
    0000000000: 23 20 41 75 74 6f 20 64 | 65 74 65 63 74 20 74 65  # Auto detect te
    0000000010: 78 74 20 66 69 6c 65 73 | 20 61 6e 64 20 70 65 72  xt files and per
    0000000020: 66 6f 72 6d 20 4c 46 20 | 6e 6f 72 6d 61 6c 69 7a  form LF normaliz
    0000000030: 61 74 69 6f 6e 0d 0a 2a | 20 74 65 78 74 3d 61 75  ation..* text=au
    0000000040: 74 6f 0d 0a 0d 0a 23 20 | 53 74 61 6e 64 61 72 64  to....# Standard
    0000000050: 20 74 6f 20 6d 73 79 73 | 67 69 74 0d 0a 2a 2e 64   to msysgit..*.d
    0000000060: 6f 63 09 20 64 69 66 66 | 3d 61 73 74 65 78 74 70  oc. diff=astextp
    0000000070: 6c 61 69 6e 0d 0a 2a 2e | 44 4f 43 09 20 64 69 66  lain..*.DOC. dif
    0000000080: 66 3d 61 73 74 65 78 74 | 70 6c 61 69 6e 0d 0a 2a  f=astextplain..*
    0000000090: 2e 64 6f 63 78 20 64 69 | 66 66 3d 61 73 74 65 78  .docx diff=astex
    00000000a0: 74 70 6c 61 69 6e 0d 0a | 2a 2e 44 4f 43 58 20 64  tplain..*.DOCX d
    00000000b0: 69 66 66 3d 61 73 74 65 | 78 74 70 6c 61 69 6e 0d  iff=astextplain.
    00000000c0: 0a 2a 2e 64 6f 74 20 20 | 64 69 66 66 3d 61 73 74  .*.dot  diff=ast
    00000000d0: 65 78 74 70 6c 61 69 6e | 0d 0a 2a 2e 44 4f 54 20  extplain..*.DOT
    00000000e0: 20 64 69 66 66 3d 61 73 | 74 65 78 74 70 6c 61 69   diff=astextplai
    00000000f0: 6e 0d 0a 2a 2e 70 64 66 | 20 20 64 69 66 66 3d 61  n..*.pdf  diff=a
    0000000100: 73 74 65 78 74 70 6c 61 | 69 6e 0d 0a 2a 2e 50 44  stextplain..*.PD
    0000000110: 46 09 20 64 69 66 66 3d | 61 73 74 65 78 74 70 6c  F. diff=astextpl
    0000000120: 61 69 6e 0d 0a 2a 2e 72 | 74 66 09 20 64 69 66 66  ain..*.rtf. diff
    0000000130: 3d 61 73 74 65 78 74 70 | 6c 61 69 6e 0d 0a 2a 2e  =astextplain..*.
    0000000140: 52 54 46 09 20 64 69 66 | 66 3d 61 73 74 65 78 74  RTF. diff=astext
    0000000150: 70 6c 61 69 6e 0d 0a                               plain..

