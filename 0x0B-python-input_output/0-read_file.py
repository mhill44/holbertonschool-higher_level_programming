#!/usr/bin/python3
""" This reads a file and prints it to the stdout """


def read_file(filename=""):
    """
    read_file:
    This reads a file and prints its content
    """
    with open(filename, 'r') as f:
        print(f.read(), end='')
