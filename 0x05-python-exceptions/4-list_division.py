#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_res_vector):
    cpt = 0
    res_vector = []
    while cpt < list_res_vector:
        try:
            res = my_list_1[cpt] / my_list_2[cpt]
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except TypeError:
            res = 0
            print("wrong type")
        except IndexError:
            res = 0
            print("out of range")
        finally:
            cpt += 1
            res_vector.append(res)
    return res_vector
