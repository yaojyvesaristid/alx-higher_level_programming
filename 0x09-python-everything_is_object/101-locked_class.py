#!/usr/bin/python3
"""
Module LockedClass
"""


class LockedClass:
    """
    class with no class or object attribute that prevents the user
    from dynamically creating new instance.
    Except if the new instance attribute is called first_name
    """

    def __setattr__(self, attribute, value):
        if attribute == "first_name":
            self.__dict__[attribute] = value
        else:
            mg = "'LockedClass' object has no attribute '{}'".format(attribute)
            raise AttributeError(mg)
