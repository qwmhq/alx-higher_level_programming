#!/usr/bin/python3
"""Matrix multiplication module"""


def check_rectangle_matrix(matrix):
    """check if a matrix is rectangular (has all rows the same size)

    Args:
        matrix(list of list of integers/floats): the matrix
    """

    size = len(matrix[0])
    for i in matrix:
        if len(i) != size:
            return False
    return True


def matrix_mul(m_a, m_b):
    """multiply two matrices and return the result

    Args:
        m_a (matrix of integers/floats): the first matrix
        m_b (matrix of integers/floats): the second matrix
    """

    # check if m_a and m_b are lists
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    elif type(m_b) is not list:
        raise TypeError("m_b must be a list")

    # check if m_a and m_b are lists of lists
    if not all(type(i) is list for i in m_a):
        raise TypeError("m_a must be a list of lists")
    elif not all(type(i) is list for i in m_b):
        raise TypeError("m_b must be a list of lists")

    # check if m_a and m_b are not empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    elif m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # check if m_a and m_b contain only integers/floats
    if not all([all([type(j) in [int, float] for j in i]) for i in m_a]):
        raise TypeError("m_a should contain only integers or floats")
    elif not all([all([type(j) in [int, float] for j in i]) for i in m_b]):
        raise TypeError("m_b should contain only integers or floats")

    # check if m_a and m_b are rectangular matrices
    if not check_rectangle_matrix(m_a):
        raise TypeError("each row of m_a must be of the same size")
    elif not check_rectangle_matrix(m_b):
        raise TypeError("each row of m_b must be of the same size")

    # check if m_a and m_b are multipliable
    if not len(m_a[0]) == len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    height_a = len(m_a)
    width_a = len(m_a[0])
    width_b = len(m_b[0])
    for i in range(height_a):
        row = []
        for j in range(width_b):
            s = 0
            for k in range(width_a):
                s += m_a[i][k] * m_b[k][j]
            row.append(s)
        result.append(row)

    return result
