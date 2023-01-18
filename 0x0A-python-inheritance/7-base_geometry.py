#!/usr/bin/python3
""" 7-base_geometry """


class BaseGeometry():
    """ BaseGeometry class """

    def area(self):
        """ area method """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validate value """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
