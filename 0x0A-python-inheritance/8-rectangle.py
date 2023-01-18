#!/usr/bin/python3
""" 8-rectangle """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle class """

    def __init__(self, width, height):
        """
        initialize a Rectangle object

        Args:
            width(int): the width of the rectangle
            height(int): the height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
