#!/usr/bin/python3
""" function that returns the JSON
    represent. of an object (a string)
"""
import json


def to_json_string(my_obj):
    """ function that returns the JSON """
    return json.dumps(my_obj)
