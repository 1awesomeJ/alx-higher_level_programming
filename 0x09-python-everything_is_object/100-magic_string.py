#!/usr/bin/python3
def magic_string():
    count = 1 
    while True:
        ret = "BestSchool, " * count; yield str(ret[:-2]); count += 1
