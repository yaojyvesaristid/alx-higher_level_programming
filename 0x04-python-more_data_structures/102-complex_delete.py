#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value not in a_dictionary.values():
        return a_dictionary
    val_to_delete = []
    for k, v in a_dictionary.items():
        if v == value:
            val_to_delete.append(k)
    for val in val_to_delete:
        del a_dictionary[val]
    return a_dictionary
