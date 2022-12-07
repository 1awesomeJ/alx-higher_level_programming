#!/usr/bin/python3
def uniq_add(my_list=[]):
    k = set(my_list)
    sum = 0
    for a in k:
        sum += a
    return sum
