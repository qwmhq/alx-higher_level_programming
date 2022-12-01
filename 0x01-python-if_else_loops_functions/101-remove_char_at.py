#!/usr/bin/python3
def remove_char_at(str, n):
    new_str = ""
    index = 0
    for i in str:
        if not index == n:
            new_str += i
        index += 1
    return new_str
