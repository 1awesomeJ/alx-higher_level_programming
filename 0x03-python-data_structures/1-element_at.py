#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    k = len(my_list)
    if idx >= k or idx < -k:
        return None
    return my_list[idx]
