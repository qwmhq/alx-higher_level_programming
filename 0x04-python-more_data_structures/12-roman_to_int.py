#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    numerals_key = {'I': 1, 'V': 5, 'X': 10,
                    'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sub = {'I': "VX", 'X': "LC", 'C': "DM"}
    value = 0
    for i, v in enumerate(roman_string):
        if (i + 1 < len(roman_string) and v in sub and
                roman_string[i + 1] in sub[v]):
            value -= numerals_key[v]
        else:
            value += numerals_key[v]
    return value
