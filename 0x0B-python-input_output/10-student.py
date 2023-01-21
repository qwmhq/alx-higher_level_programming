#!/usr/bin/python3
""" 10-student """


class Student():
    """ Student class """

    def __init__(self, first_name, last_name, age):
        """
        initialize a Student object

        Args:
            first_name (str): student's first name
            last_name (str): student's last name
            age (int): student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieve the dictionary representation of a Student object """
        if type(attrs) is list and all([type(x) is str for x in attrs]):
            dct = {}
            for attr in attrs:
                if attr in self.__dict__.keys():
                    dct[attr] = self.__dict__[attr]
            return dct
        return self.__dict__
