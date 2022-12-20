#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        k = fct(args[0], args[1])
    except(NameError, TypeError, IndexError,
           ValueError, ZeroDivisionError) as err:
        k = None
        print("Exception: {}".format(err), file=sys.stderr)
    return k
