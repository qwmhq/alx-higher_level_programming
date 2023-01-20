#!/usr/bin/python3
""" Base class module """
import json


class Base():
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize a Base class object """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ get JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ get the list of the JSON string representation """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ write the JSON string representation of list_objs to a file """
        if not type(list_objs) is list or not all([isinstance(x, cls) for x in list_objs]):
            raise TypeError("list_objs must be a list of instances who inherit from Base")
        with open("{}.json".format(cls.__name__), 'w', encoding="utf-8") as f:
            f.write(cls.to_json_string([x.to_dictionary() for x in list_objs]))
