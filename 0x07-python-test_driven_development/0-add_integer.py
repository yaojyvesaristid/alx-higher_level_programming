#!/usr/bin/python3
"""
Module Add integer
"""


def add_integer(a, b=98):
    """
    method add integer with two params
    a and b must be integers of floats, otherwise raise a TypeError
    a and b must be first casted to integer if they are float
    return the addition of a and b as an integer
    """

    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")

    return a + b
