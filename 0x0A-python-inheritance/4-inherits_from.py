#!/usr/bin/python3
""" A class that inherits from another class """


def inherits_from(obj, a_class):
    """
    Return: Returns true if the object is an instance of a class that has inherited
    (in)directly from the specified class. Returns false otherwise.
    """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
