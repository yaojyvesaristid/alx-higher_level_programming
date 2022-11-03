#!/usr/bin/python3
"""
Module Inherits From
"""


def inherits_from(obj, a_class):
    """
    return True if a object 'obj' is an instance of a class 'a_class'
        that inherited directly or undirectly from the specified class
    otherwise return False
    """

    if type(obj) != a_class and isinstance(obj, a_class):
        return True
    return False
