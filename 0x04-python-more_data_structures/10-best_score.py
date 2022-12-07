#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    best = list(a_dictionary)[0]
    for k, v in a_dictionary.items():
        if v > a_dictionary[best]:
            best = k
    return best
