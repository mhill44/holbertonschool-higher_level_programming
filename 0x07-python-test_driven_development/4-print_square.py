#!/usr/bin/python3
"""
This module contains: the text_indentation function
"""

def print_square(size, end=None):
    """
    Result prints a square where size is the length and width
    of the square
    """
    if type(size) is not int or (type(size) is float and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("size is zero")
    for i in range(size):
        for k in range(size):
            print("#", end="")
        print()
