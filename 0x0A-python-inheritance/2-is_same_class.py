#!/usr/bin/python3
""" 2-is_same_class """


def is_same_class(obj, a_class):
    """
    check if an object is an exact instance of a class

    Args:
        obj: the object
        a_class: the class
    """
    return type(obj) is a_class
