#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    print("{} argument{}{}".format(argc - 1,
                                   '' if argc == 2 else 's',
                                   '.' if argc < 2 else ':'))
    for i in range(1, argc):
        print("{}: {}".format(i, sys.argv[i]))
