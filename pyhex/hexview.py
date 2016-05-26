# -*- coding: utf-8 -*-
import sys


if sys.version_info[0] >= 3:

    class HexView:
        """A class that converts provided binary buffer into hex-view.
        """
        show_address = True
        show_hex = True
        show_value = True
        start_address = 0
        bytes_per_line = 16
        bytes_per_group = 8
        safe_char = "."
        unsafe_chars = tuple(range(32)) + (127,)
        stream = None

        def __init__(self,
                     stream=None,
                     show_address=True,
                     show_hex=True,
                     show_value=True,
                     start_address=0,
                     bytes_per_line=16,
                     bytes_per_group=8,
                     safe_char=".",
                     unsafe_chars=tuple(range(32)) + (127,)):
            self.stream = stream
            self.show_address = show_address
            self.show_hex = show_hex
            self.show_value = show_value
            self.start_address = start_address
            self.bytes_per_line = bytes_per_line
            self.bytes_per_group = bytes_per_group
            self.safe_char = safe_char
            self.unsafe_chars = unsafe_chars

        def __iter__(self):
            def iterator():
                # copy all settings, so that modifying object inside loop would not affect the iterator
                show_address = self.show_address
                show_hex = self.show_hex
                show_value = self.show_value
                start_address = self.start_address
                bytes_per_line = self.bytes_per_line
                bytes_per_group = self.bytes_per_group
                safe_char = self.safe_char
                unsafe_chars = self.unsafe_chars

                address = start_address
                buffer = self.stream.read(bytes_per_line)
                while buffer is not None and len(buffer) > 0:
                    str_address = ""
                    if show_address:
                        str_address = "%08x: " % address
                    str_hex = ""
                    if show_hex:
                        prefix_ws = 0
                        for idx in range(bytes_per_line):
                            byte_hex = "  "
                            if idx < len(buffer):
                                byte_hex = "%02x" % buffer[idx]
                            str_hex += " " * prefix_ws
                            str_hex += byte_hex
                            prefix_ws = 1
                            if (idx + 1) % bytes_per_group == 0:
                                prefix_ws = 2
                    str_value = ""
                    if show_value:
                        if show_hex:
                            str_value = " | "
                        str_value += "".join(safe_char if byte in unsafe_chars else chr(byte) for byte in buffer)
                    yield "%s%s%s" % (str_address, str_hex, str_value)
                    address += bytes_per_line
                    buffer = self.stream.read(bytes_per_line)

            if self.stream is None:
                raise ValueError("stream is not set")
            return iterator()

else:

    class HexView(object):
        """A class that converts provided binary buffer into hex-view.
        """
        show_address = True
        show_hex = True
        show_value = True
        start_address = 0
        bytes_per_line = 16
        bytes_per_group = 8
        safe_char = u"."
        unsafe_chars = tuple(range(32)) + (127,)
        stream = None

        def __init__(self,
                     stream=None,
                     show_address=True,
                     show_hex=True,
                     show_value=True,
                     start_address=0,
                     bytes_per_line=16,
                     bytes_per_group=8,
                     safe_char=".",
                     unsafe_chars=tuple(range(32)) + (127,)):
            self.stream = stream
            self.show_address = show_address
            self.show_hex = show_hex
            self.show_value = show_value
            self.start_address = start_address
            self.bytes_per_line = bytes_per_line
            self.bytes_per_group = bytes_per_group
            self.safe_char = safe_char
            self.unsafe_chars = unsafe_chars

        def __iter__(self):
            def iterator():
                # copy all settings, so that modifying object inside loop would not affect the iterator
                show_address = self.show_address
                show_hex = self.show_hex
                show_value = self.show_value
                start_address = self.start_address
                bytes_per_line = self.bytes_per_line
                bytes_per_group = self.bytes_per_group
                safe_char = self.safe_char
                unsafe_chars = self.unsafe_chars

                address = start_address
                buffer = self.stream.read(bytes_per_line)
                while buffer is not None and len(buffer) > 0:
                    str_address = u""
                    if show_address:
                        str_address = u"%08x: " % address
                    str_hex = u""
                    if show_hex:
                        prefix_ws = 0
                        for idx in range(bytes_per_line):
                            byte_hex = u"  "
                            if idx < len(buffer):
                                byte_hex = u"%02x" % ord(buffer[idx])
                            str_hex += u" " * prefix_ws
                            str_hex += byte_hex
                            prefix_ws = 1
                            if (idx + 1) % bytes_per_group == 0:
                                prefix_ws = 2
                    str_value = u""
                    if show_value:
                        if show_hex:
                            str_value = u" | "
                        str_value += u"".join(safe_char if ord(byte) in unsafe_chars else chr(ord(byte))
                                              for byte in buffer)
                    yield u"%s%s%s" % (str_address, str_hex, str_value)
                    address += bytes_per_line
                    buffer = self.stream.read(bytes_per_line)

            if self.stream is None:
                raise ValueError("stream is not set")
            return iterator()
