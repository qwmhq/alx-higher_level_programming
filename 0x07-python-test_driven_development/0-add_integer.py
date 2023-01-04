#!/usr/bin/python3

"""0-add_integer module"""


def add_integer(a, b=98):
    """Return the sum of the two integers

    Args:
        a (int): the first integer
        b (int): the second integer
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
