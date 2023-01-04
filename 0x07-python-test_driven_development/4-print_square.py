#!/usr/bin/python3

"""4-print_square module"""


def print_square(size):
    """print a square using the character '#'
    the square has a width and height the value of size

    Args:
        size (int): the size of the square to print
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        print("")
    for i in range(size):
        print("#" * size)
