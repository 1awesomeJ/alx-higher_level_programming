#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    i = 0
    for k in new:
        if k == search:
            new[i] = replace
        i += 1
    return new
