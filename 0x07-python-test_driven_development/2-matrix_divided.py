#!/usr/bin/python3

"""2-matrix_divided module"""


def matrix_divided(matrix, div):
    """divide all elements of a matrix"""

    # check that matrix is actually a matrix of floats/integers
    if (type(matrix) is not list
            or not all([type(i) is list for i in matrix])
            or not all(
                [all(type(j) in [float, int] for j in i) for i in matrix])):
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    # check that the rows in the matrix are of equal length
    size = len(matrix[0])
    for i in matrix:
        if (len(i) != size):
            raise TypeError("Each row of the matrix must have the same size")

    if (type(div) not in [float, int]):
        raise TypeError("div must be a number")

    if (div == 0):
        raise ZeroDivisionError("division by zero")

    divided = [list(map(lambda x: round(x/div, 2), i)) for i in matrix]

    return divided
