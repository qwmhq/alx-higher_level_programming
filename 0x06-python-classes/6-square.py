#!/usr/bin/python3
""" Defining a Square class """


class Square:
    """ Square class """
    def __init__(self, size=0, position=(0, 0)):
        """
        initializing a class instance

        Args:
            size (int): size of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ get the size of a square """
        return self.__size

    @size.setter
    def size(self, size):
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """ get the position (co-ordinates) of a square """
        return self.__position

    @position.setter
    def position(self, position):
        if ((type(position) is not tuple)
                or (len(position) != 2)
                or (type(position[0]) is not int)
                or (type(position[1]) is not int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """ calculate the area of the square """
        return self.size ** 2

    def my_print(self):
        """ print the square with character '#' """
        if (self.size == 0):
            print("")
            return
        print("\n" * self.position[1], end="")
        for i in range(self.size):
            print("{}{}".format(self.position[0] * ' ', self.size * '#'))
