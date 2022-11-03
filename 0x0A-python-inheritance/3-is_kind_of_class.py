#!/usr/bin/python3
"""
Module Is Kind of Class
"""


def is_kind_of_class(obj, a_class):
    """
    return True if a object 'obj' is an instance of a class 'a_class'
	or if the object is an instance of a class that inherited from
        otherwise return False
    """

    return isinstance(obj, a_class)
