#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    k = []
    for i in my_list:
        if i % 2:
            k.append(False)
        else:
            k.append(True)
    return k
