#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return None
    tot = 0
    weight = 0
    for k in my_list:
        tot += (k[0] * k[1])
        weight += k[1]
    return (tot/weight)
