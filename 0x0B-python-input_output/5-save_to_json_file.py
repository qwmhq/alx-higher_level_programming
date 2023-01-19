#!/usr/bin/python3
""" 5-save_to_json_file """
import json


def save_to_json_file(my_obj, filename):
    """
    write an object to a text file using JSON representation

    Args:
        my_obj: the object to write
        filename: the name of the file to write to
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
