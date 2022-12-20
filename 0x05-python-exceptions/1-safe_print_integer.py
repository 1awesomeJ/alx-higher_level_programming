#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        k = True
    except(NameError, TypeError, ValueError):
        k = False
    return k
