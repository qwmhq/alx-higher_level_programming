#!/usr/bin/python3
""" 0-read_file """


def read_file(filename=""):
    """ read a text file and print it to standard output """
    with open(filename, encoding="utf-8") as f:
        file_content = f.read()
    print(file_content, end="")
