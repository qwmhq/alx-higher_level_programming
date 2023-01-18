#!/usr/bin/python3
""" 3-is_kind_of_class """


def is_kind_of_class(obj, a_class):
    """
    check if an object is an instance of a class,
    or an instance of a subclass of a class

    Args:
        obj: the object
        a_class: the class
    """
    return isinstance(obj, a_class)
