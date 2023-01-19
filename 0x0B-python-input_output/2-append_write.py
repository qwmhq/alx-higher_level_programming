#!/usr/bin/python3
""" 2-append_write """


def append_write(filename="", text=""):
    """ append a string at the end of a text file """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
