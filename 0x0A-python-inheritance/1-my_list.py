#!/usr/bin/python3
"""
Module MyList
"""


class MyList(list):
    """
    Class that inherit from list
    public instance method print_sorted that prints the list
    in ascending order
    assumes that all elements of the list is of type int
    """

    def print_sorted(self):
        print("{}".format(sorted(self)))
