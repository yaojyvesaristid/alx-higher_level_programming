#!/usr/bin/python3
"""
This is the "Rectangle"  module.

This module provides a simple Rectangle class with attribute width and height.
Default values of both attributes are 0.
public class attribute number_of_instances initialized to 0
instance method area perimeter str repr and del
"""


class Rectangle:
    """
    A Rectangle class with private instance attributes width and height
    private class attribute to count the number of instance
    constructor and getters and setters for the 2 attributes
    method area to compute the rectangle area
    method perimeter to compute the rectangle perimeter
    method str prints the rectangle
    method repr return a string representation e.g. Rectangle(2, 4)
    method del prints a msg
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
