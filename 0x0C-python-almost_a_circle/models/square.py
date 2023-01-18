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

    @property
    def size(self):
        """ get the size of a Square object """
        return self.width

    @size.setter
    def size(self, size):
        """ set the size of a Square object """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ update attributes of a Square object """
        if len(args) > 0:
            attributes = ["id", "", "x", "y"]
            for index, value in enumerate(args):
                setattr(self, attributes[index], value)
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ get the dictionary representation of a Rectangle object """
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
