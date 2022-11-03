#!/usr/bin/python3
"""
Module BaseGeometry
"""


class BaseGeometry:
    """
    Class Geometry
    public instance method 'area' that raise an Exception
    public instance method 'integer_validator' that validate 'value'
        name is always a string
        if value is not integer raise TypeError
        if value <= 0 raise ValueError
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
