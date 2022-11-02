#!/usr/bin/python3
"""
Module Say My Name
"""


def say_my_name(first_name, last_name=""):
    """
    function that prints a string
    2 params must be a string otherwise raise a TypeError
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
