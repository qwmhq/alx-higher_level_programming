#!/usr/bin/python3
""" 10-square """
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Square Class """

    def __init__(self, size):
        """ initialize a Square object """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ get the area of a Square object """
        return self.__size ** 2
