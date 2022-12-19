#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    y, printed = 0, 0
    while y < x:
        try:
            print("{:d}".format(my_list[y]), end="")
            printed += 1
        except (ValueError, TypeError):
            y += 1
            continue
        y += 1
    print("")
    return printed
