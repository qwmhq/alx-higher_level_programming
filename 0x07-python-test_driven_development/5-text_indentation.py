#!/usr/bin/python3

"""5-text_indentation module"""


def text_indentation(text):
    """
    print a text with two new lines after each of these
    characters: '.', '?', and ':'

    Args:
        text (str): the text to print
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for char in text:
        if char in ['.', '?', ':']:
            print(f"{char}\n\n", end="")
        else:
            print(char, end="")
