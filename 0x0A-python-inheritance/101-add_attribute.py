#!/usr/bin/python3
"""
Module Add Attribute
"""


def add_attribute(obj, name, value):
    """
    add new attribute to an object 'obj' if it's possible
    """

    immuable_object = [int, float, str, dict, list, tuple, object, type, frozenset]
    if type(obj) in immuable_object:
        raise TypeError("can't add new attribute")

    obj.__setattr__(name, value)
