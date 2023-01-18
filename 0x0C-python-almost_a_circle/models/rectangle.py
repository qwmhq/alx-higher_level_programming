#!/usr/bin/python3
""" Rectangle class module """


from models.base import Base


class Rectangle(Base):
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize a Rectangle Object """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """ get string representation of a Rectangle object """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    @property
    def width(self):
        """ get the width of a Rectangle object """
        return self.__width

    @width.setter
    def width(self, width):
        """ set the width of a Rectangle object """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ get the height of a Rectangle object """
        return self.__height

    @height.setter
    def height(self, height):
        """ set the height of a Rectangle object """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ get the x parameter of a Rectangle object """
        return self.__x

    @x.setter
    def x(self, x):
        """ set the x parameter of a Rectangle object """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ get the y parameter of a Rectangle object """
        return self.__y

    @y.setter
    def y(self, y):
        """ set the y parameter of a Rectangle object """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ get the area of a Rectangle object """
        return self.width * self.height

    def display(self):
        """ print a Rectangle object with the character # """
        s = ""
        s += self.y * "\n"
        s += "{}{}\n".format(self.x * " ", "#" * self.width) * self.height
        print(s, end="")

    def update(self, *args, **kwargs):
        """ update attributes of a Rectangle object """
        if len(args) > 0:
            attributes = ["id", "width", "height", "x", "y"]
            for index, value in enumerate(args):
                setattr(self, attributes[index], value)
        elif kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ get the dictionary representation of a Rectangle object """
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
