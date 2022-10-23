#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda vec: list(map(lambda x: x**2, vec)), matrix))
