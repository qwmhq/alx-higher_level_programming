#!/usr/bin/python3
""" 8-class_to_json """


def class_to_json(obj):
    """
    get the dictionary description of an object

    Args:
        obj: the object
    """
    return obj.__dict__
