#!/usr/bin/python3
""" Square module """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ initialize a Square object """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ get string representation of a Square object """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
