#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    k = len(my_list)
    if idx >= k or idx < -k:
# the or part is not necessary cos negative indexes have been handled on line3
        return None
    return my_list[idx]
