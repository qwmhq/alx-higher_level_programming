#!/usr/bin/python3
""" 100-my_int """


def MyInt(int):
    """ custom int class """

    def __eq__(self, other):
        """ equals operator overload """
        return int(self) != int(other)

    def __ne__(self, other):
        """ not equals operator overload """
        return int(self) == int(other)
