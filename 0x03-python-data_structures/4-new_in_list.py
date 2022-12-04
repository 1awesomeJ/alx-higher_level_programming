#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    k = len(my_list)
    if idx >= k:
        return my_list
    newlist = my_list.copy()
    newlist[idx] = element
    return newlist
