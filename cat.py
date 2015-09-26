#!/usr/bin/env python3
""" cat - concatenate files and print on the standard output.

This is a basic implementation of cat in Python.

Options supported:

None (yet)
"""

import argparse
import os.path
import sys

def output_file(filename: str, output_file=sys.stdout):
    """Output a file to stdout.

    Arguments:
        filename: a string containing the path to the file to output.
        output_file: A file-like object to which we write.
    """
    BUFFER_SIZE = 16384
    buffer = bytearray(BUFFER_SIZE)
    with open(filename, 'rb') as file:
        while True:
            bytes_read = None
            while bytes_read is None:
                bytes_read = file.readinto(buffer)
            if bytes_read == 0:
                break
            bytes_written = 0
            while bytes_written < bytes_read:
                bytes_written = output_file.write(
                    buffer[bytes_written:bytes_read].decode(errors='ignore'))

def main(args=sys.argv) -> int:
    """Enter cat as run on a command line."""
    parser = argparse.ArgumentParser(
        description='Concatenate files and print to standard output.')
    parser.add_argument('files', type=str, nargs='*')
    args = parser.parse_args(args)
    for file in args.files:
        output_file(file)


if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit(130)
