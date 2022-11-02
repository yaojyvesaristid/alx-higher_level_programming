#!/usr/bin/python3
"""
Module Add integer
"""


def add_integer(a, b=89):
	"""
	method add integer with two params
	a and b must be integers of floats, otherwise raise a TypeError
	a and b must be first casted to integer if they are float
	return the addition of a and b as an integer
	"""

	if type(a) != int or type(a) != float:
		raise TypeError("a msut be an integer")
	
	if type(b) != int or type(b) != float:
		raise TypeError("b must be an integer")

	return int(a) + int(b)
