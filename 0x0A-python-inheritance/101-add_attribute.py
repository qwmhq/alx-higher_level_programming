#!/usr/bin/python3
""" 101-add_attribute """


def add_attribute(obj, name, value):
    """
    add a new attribute to an object, if possible

    Args:
        obj: object
        name: attribute name
        value: attribute value
    """
    if ((hasattr(obj, "__slots__") and name not in obj.__slots__)
            or not hasattr(obj, "__dict__")):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
