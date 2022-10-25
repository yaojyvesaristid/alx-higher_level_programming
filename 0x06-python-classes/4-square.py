#!/usr/bin/python3
"""
This is a square module which define a square class
"""


class Square:
    """ square class with private instance attribute size
        size must be a digit and have a value >= 0
        method getter and setter propertties for size
        method area return the square value of attribute size
    """
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.__size**2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")
