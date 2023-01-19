#!/usr/bin/python3
""" 100-my_int """


class MyInt(int):
    """ custom int class with inverted == and != operators"""

    def __eq__(self, other):
        """ equals operator overload """
        return int(self) != int(other)

    def __ne__(self, other):
        """ not equals operator overload """
        return int(self) == int(other)
