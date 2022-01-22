#!/usr/bin/python3
""" Class to JSON """


def class_to_json(obj):
    """
    Args:
        obj: the object to convert to JSON
    Returns:
        a JSON representation of object
    """
    return obj.__dict__
