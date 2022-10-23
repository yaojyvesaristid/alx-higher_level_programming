#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    quotient = 0
    numerateur = list(t[0] * t[1] for t in my_list)
    denominateur = list(t[1] for t in my_list)
    quotient = sum(numerateur) / sum(denominateur)
    return quotient
