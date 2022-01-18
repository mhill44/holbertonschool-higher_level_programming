#!/usr/bin/python3

"""
This module contains: the add_integer function
"""


def add_integer(a, b=98):
    """
    Returns: sum of a and b. Prints an error
    message if values of a and b are not integers or floats
    """
    if type(a) == float:
        a = int(a)
    elif type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) == float:
        b = int(b)
    elif type(b) != int:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
