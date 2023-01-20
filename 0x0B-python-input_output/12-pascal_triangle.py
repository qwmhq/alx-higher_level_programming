#!/usr/bin/python3
""" 12-pascal_triangle """


def pascal_triangle(n):
    """
    get the Pascal's triangle of n in the
    form of a list of lists of integers

    Args:
        n (int): the height of the triangle
    """
    if n <= 0:
        return []
    triangle = [[], [1]]
    for i in range(2, n + 1):
        line = [1]
        prev_line = triangle[i - 1]
        for j in range(1, i - 1):
            line.append(prev_line[j - 1] + prev_line[j])
        line.append(1)
        triangle.append(line)
    return triangle[1:]
