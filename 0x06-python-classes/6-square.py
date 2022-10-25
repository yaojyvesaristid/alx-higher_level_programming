#!/usr/bin/python3
"""
This is a square module which define a square class
"""


class Square:
    """ square class with private instance attribute size
        size must be a digit and have a value >= 0
        method getter and setter propertties for size
        method area return the square value of attribute size
        method my_print display the figure of the square"
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        msg = "position must be a tuple of 2 positive integers"
        if type(value) != tuple:
            raise TypeError(msg)
        if len(value) != 2:
            raise TypeError(msg)
        for val in value:
            if type(val) != int or val < 0:
                raise TypeError(msg)

        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            nb_space = " " * self.__position[0]
            for i in range(self.__position[1]):
                print()
            print(nb_space, end="")
            for i in range(1, self.__size**2+1):
                if i % 3 == 0:
                    print("#")
                    if i != self.__size**2:
                        print(nb_space, end="")
                else:
                    print("#", end="")
