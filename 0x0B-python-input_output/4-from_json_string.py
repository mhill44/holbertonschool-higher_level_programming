#!/usr/bin/python3
""" A function that returns an
    object (python data structure) represented
    by a JSON string
"""

import json


def from_json_string(my_str):
    """ This returns an object (Python data structure)
        represented by a JSON string
    """
    return json.loads(my_str)
