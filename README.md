PyHex
=====

Python package for easy printing of strings as hexview strings

Code Examples
=============
Converting a string:

    from pyhex import pyhex_format

    string = "Lobster ALL the Fetish!?"
    hex = "\n".join(pyhex_format(string, 0))
    print hex

Output:

    0000000000: 4c 6f 62 73 74 65 72 20 | 41 4c 4c 20 74 68 65 20  Lobster ALL the
    0000000010: 46 65 74 69 73 68 21 3f                            Fetish!?

Printing an entire file:

    from pyhex import pyhex_format_stream

    with open("example.txt", "rb") as stream:
        for row in pyhex_format_stream(stream)):
            print row

If the contents of "example.txt" are:

    Lobster ALL the Fetish!?

    Ah yes! We like to lobster our fetish!

Output:

    0000000000: 4c 6f 62 73 74 65 72 20 | 41 4c 4c 20 74 68 65 20  Lobster ALL the
    0000000010: 46 65 74 69 73 68 21 3f | 0a 0a 41 68 20 79 65 73  Fetish!?..Ah yes
    0000000020: 21 20 57 65 20 6c 69 6b | 65 20 74 6f 20 6c 6f 62  ! We like to lob
    0000000030: 73 74 65 72 20 6f 75 72 | 20 66 65 74 69 73 68 21  ster our fetish!
    0000000040: 0a                                                 .
