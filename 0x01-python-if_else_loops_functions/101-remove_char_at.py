#!/usr/bin/python3
def remove_char_at(str, n):
    str_mut = list(str)
    del str_mut[n]
    return "".join(str_mut)
