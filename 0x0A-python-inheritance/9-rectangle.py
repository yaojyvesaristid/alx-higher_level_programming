#!/usr/bin/python3
"""
Module Rectangle
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle inherits from BaseGeometry
    instantiation method with attributes width and height
    width and height must be private and positive integer
        validate by integer_validator
    public method area() must be implemented
    print() should print
    str() should return [Rectangle] <width>/<height>
    """

    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
