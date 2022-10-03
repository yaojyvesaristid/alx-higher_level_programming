#!/usr/bin/python3
def no_c(my_string):
    my_string = list(my_string)
    my_stringi = []
    for i in range(len(my_string)-1):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        else:
            my_stringi = my_stringi + [my_string[i]]
    return "".join(my_stringi)
