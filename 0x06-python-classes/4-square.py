#!/usr/bin/python3
"""This module contains the definition of a class Square"""


class Square:
    """This is an empty class"""
    def __init__(self, size=0):
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size)**2

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
