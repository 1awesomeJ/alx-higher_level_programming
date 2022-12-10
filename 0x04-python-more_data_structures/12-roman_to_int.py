#!/usr/bin/python3
def roman_to_int(roman_string):
    ret = 0
    for k in roman_string:
        if k == "I":
            ret += 1
        elif k == "V":
            ret += 5
        elif k == "X":
            ret += 10
        elif k == "L":
            ret += 50
        elif k == "C":
            ret += 100
        elif k == "D":
            ret += 500
        elif k == "M":
            ret += 1000
        else:
            return None
    return ret
