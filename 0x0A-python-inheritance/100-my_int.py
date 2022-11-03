#!/usr/bin/python3
"""
Module My Int
"""


class MyInt(int):
    """
    class MyInt inherits from int
    """

    def __eq__(self, value):
        return super().__ne__(value)

    def __ne__(self, value):
        return super().__eq__(value)
