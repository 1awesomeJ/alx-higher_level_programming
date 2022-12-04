#!/usr/bin/python3
def no_c(my_string):
    p = []
    i = 0
    while i < len(my_string):
        if my_string[i] == "c" or my_string[i] == "C":
            i += 1
            continue
        p.append(my_string[i])
        i += 1
    c = ""
    i = 0
    while i < len(p):
        c += p[i]
        i += 1
    return c
