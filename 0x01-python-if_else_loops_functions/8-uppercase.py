#!/usr/bin/python3
def uppercase(str):
    str_mut = list(str)
    for i in range(len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            str_mut[i] = chr(ord(str[i]) - 32)
    print("{}".format("".join(str_mut)))
