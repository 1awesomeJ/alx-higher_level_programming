#!/usr/bin/python3
"""
    This module contains a function
"""


def add_integer(a, b=98):
    """
    This funtion adds two numbers and returns their sum
    """

    if a == float('inf'):
        raise OverflowError("cannot convert float infinity to integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (a + b)
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (a + b)
