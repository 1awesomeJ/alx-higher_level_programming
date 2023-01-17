#!/usr/bin/python3
""" This module contains one function"""


def print_square(size):
    """This function prints a specified size of square
    of the character '#' """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for k in range(size):
            print("#", end="")
        print("")
