#!/usr/bin/python3
""" 6-load_from_json_file """
import json


def load_from_json_file(filename):
    """
    create an object from a JSON file

    Args:
        filename(string): the name of the file to read from
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
