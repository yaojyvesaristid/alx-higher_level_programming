#!/usr/bin/python3
"""
Module Square
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Class Square inherits from Rectangle
    size must be private and be validate by integer_validator
    """

    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size**2
