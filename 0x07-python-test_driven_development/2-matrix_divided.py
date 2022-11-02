#!/usr/bin/python3
"""
Module Matrix Divided
"""


def matrix_divided(matrix, div):
    """
    Matrix must be a list of lists of integers or floats
    otherwise raise a TypeError
    Each row of the matrix must be of the same size
    otherwise raise a TypeError
    'div' must be a number (integer or float)
    otherwise raise a TypeError
    """

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")

    msg = "matrix must be a matrix (list of lists) of integers/floats"
    msgE = "Each row of the matrix must have the same size"
    for vec in matrix:
        if not all(isinstance(elt, (int, float)) for elt in vec):
            raise TypeError(msg)

    if not all(len(vec) == len(matrix[0]) for vec in matrix):
        raise TypeError(msgE)

    mat = [[round(x/div, 2) for x in vec] for vec in matrix]
    return mat
