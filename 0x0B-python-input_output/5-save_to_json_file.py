#!/usr/bin/python3
""" save_to_json_file.py: saves to json file """
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using JSON representation
    """
    with open(filename, 'w') as f:
        return json.dump(my_obj, f)
