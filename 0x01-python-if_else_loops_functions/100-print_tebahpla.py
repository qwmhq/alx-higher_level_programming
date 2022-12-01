#!/usr/bin/python3
upper = True
for i in range(122, 96, -1):
    print("{}".format(chr(i) if upper else chr(i - 32)), end="")
    upper = not upper
