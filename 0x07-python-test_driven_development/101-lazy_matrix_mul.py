#!/usr/bin/python3
"""Lazy matrix multiplication"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Matrix multiplication using numpy

    Args:
        m_a (matrix): the first matrix
        m_b (matrix): the second matrix
    """

    return np.matmul(m_a, m_b)
