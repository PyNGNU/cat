#!/usr/bin/env python3
"""Generate every possible set of 2 bytes.

This is used for testing that cat is capable of outputting every possible
pair of bytes. We need to do this to check that stdout is behaving as we expect
it to, since it's opened as a text interface.
"""

import sys

file = open(sys.argv[1], 'wb')

chars = bytearray(512)
for i in range(256):
    for j in range(256):
        chars[2 * j] = i
        chars[2 * j + 1] = j
    file.write(chars)
