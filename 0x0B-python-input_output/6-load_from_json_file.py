#!/usr/bin/python3
""" This loads from a JSON file """
import json


def load_from_json_file(filename):
    """ Load from a JSON file """
    with open(filename, "r", encoding="utf-8") as a_file:
        return json.load(a_file)
