#!/usr/bin/python3
"""
Module Text Indentation
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after finding some characters
    text must be a string otherwise raise a TypeError
    no space at the beginning or at the end of each printed line
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    sep = ['.', ':', '?']
    txtsplit = ""
    ltext = []
    for w in text:
        if w in sep:
            txtsplit = txtsplit + w + "\n\n"
            ltext.append(txtsplit.lstrip())
            txtsplit = ""
            continue
        txtsplit = txtsplit + w

    ltext.append(txtsplit.lstrip())
    for elt in ltext:
        print(elt, end="")
