#!/usr/bin/python3
def common_elements(set_1, set_2):
    return {val for val in set_1 for str in set_2 if val == str}
