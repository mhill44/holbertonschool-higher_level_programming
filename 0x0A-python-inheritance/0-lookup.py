#!/usr/bin/python3
""" Lookup class """


def lookup(obj):
    """ Gets attributse and methods from an object

        Args:
            obj: The object to get the attributes and methods from

        Returns:
            Returns list[str]: a list of attributes and methods
    """
    return dir(obj)
