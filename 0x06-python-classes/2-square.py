#!/usr/bin/python3
"""This module contains the definition of a class Square"""


class Square:
    """This is an empty class"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
