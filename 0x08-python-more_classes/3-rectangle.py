#!/usr/bin/python3
"""
This is the "Rectangle"  module.

This module provides a simple Rectangle class with attribute width and height.
Default values of both attributes are 0.
instance method area and perimeter
"""


class Rectangle:
    """
    A Rectangle class with attributes  width and height
    constructor and getters and setters for the 2 attributes
    method area to compute the rectangle area
    method perimeter to compute the rectangle perimeter
    method print and str print the rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        figure = ""
        if self.__width == 0 or self.height == 0:
            return figure
        for i in range(self.__height):
            if i > 0:
                figure += '\n'
            for j in range(self.__width):
                figure += "#"
        return figure 
