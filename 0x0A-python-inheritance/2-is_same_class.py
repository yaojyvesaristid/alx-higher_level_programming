#!/usr/bin/python3
"""
Module Is Same Class
"""

def is_same_class(obj, a_class):
    """
    return True if a object 'obj' is an instance of a class 'a_class'
        otherwise return False
    """

    return isinstance(type(obj), a_class)
