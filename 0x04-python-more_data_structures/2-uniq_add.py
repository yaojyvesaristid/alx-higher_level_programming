#!/usr/bin/python3
def uniq_add(my_list=[]):
    if len(my_list) > 0:
        nlist = list()
        for val in my_list:
            if val not in nlist:
                nlist.append(val)
                sum = 0
        while len(nlist) > 0:
            sum = sum + nlist.pop()
            return sum
    return 0
