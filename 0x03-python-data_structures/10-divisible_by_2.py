#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return my_list
    nlist = list(my_list)
    for i in range(len(nlist)):
        if nlist[i] % 2 == 0:
            nlist[i] = True
        else:
            nlist[i] = False
    return nlist
