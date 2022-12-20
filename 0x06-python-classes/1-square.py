#!/usr/bin/python3
""" Defining a Square class with size """


class Square:
    """ Square class with size """
    def __init__(self, size):
        """
        initializing a class instance

        Args:
            size (int): size of the square
        """
        self.__size__ = size
