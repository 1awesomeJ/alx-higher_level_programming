#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        k = a/b
    except(ValueError, TypeError, ZeroDivisionError, NameError):
        k = None
    finally:
        print("Inside result: {}".format(k))
    return k
