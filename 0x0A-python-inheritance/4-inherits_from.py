#!/usr/bin/python3
""" 4-inherits_from """


def inherits_from(obj, a_class):
    """
    check if obj is an instance of a class
    that inherits from a_class

    Args:
        obj: object
        a_class: class
    """
    return type(obj) is not a_class and isinstance(obj, a_class)
