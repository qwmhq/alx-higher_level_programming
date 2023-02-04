#!/usr/bin/python3
""" 100-append_after """


def append_after(filename="", search_string="", new_string=""):
    """
    insert a line of text into a file, after each line containing
    a specific string
    Args:
        filename (str): the name of the file to insert into
        search_string (str): the string to insert after
        new_string (str): the string to insert into the file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        contents = f.readlines()
    search_string_indexes = []
    for index, item in enumerate(contents):
        if search_string in item:
            search_string_indexes.append(index)
    insert_offset = 1
    for index in search_string_indexes:
        if (index < len(contents) - 1):
            contents.insert(index + insert_offset, new_string)
        else:
            contents.append(new_string)
        insert_offset += 1
    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(contents))
