#!/usr/bin/python3
"""
Module Print Square
"""


def print_square(size):
    """
    function that prints a square with the character #
    size is the size length of the square
    size must be an integer otherwise raise a TypeError
    size must be >= 0 otherwise raise a TypeError
    size must be an integer otherwise raise a TypeError
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
