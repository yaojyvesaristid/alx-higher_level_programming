#!/usr/bin/python3
def uniq_add(my_list=[]):
    if len(my_list) > 0:
        my_set = set(my_list)
        sum = 0
        while len(my_set) > 0:
            sum = sum + my_set.pop()
        return sum
    return 0
