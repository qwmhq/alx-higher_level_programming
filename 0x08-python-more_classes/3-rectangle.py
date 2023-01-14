#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """
        initialize a Rectangle object

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.width = width
        self.height = height

    def __str__(self):
        """string representation of a Rectangle object"""
        if self.width == 0 or self.height == 0:
            return ""
        s = ""
        for i in range(self.height):
            s += "{}{}".format('#' * self.width,
                               '\n' if i < self.height - 1 else '')
        return s

    @property
    def width(self):
        """get the width of a Rectangle object"""
        return self.__width

    @width.setter
    def width(self, width):
        """set the width of a Rectangle object"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """get the height of a Rectangle object"""
        return self.__height

    @height.setter
    def height(self, height):
        """set the height of a Rectangle object"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """get the area of a Rectangle object"""
        return self.width * self.height

    def perimeter(self):
        """get the perimeter of a Rectangle object"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * self.width + 2 * self.height
