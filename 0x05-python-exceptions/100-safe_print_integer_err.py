#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        k = True
    except(NameError, TypeError, ValueError) as err:
        k = False
        print("Exception: {}".format(err), file=sys.stderr)
    return k
