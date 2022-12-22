#!/usr/bin/python3
"""This module contains the definition of a class Square"""


class Square:
    """This is an empty class"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

    def my_print(self):
        if self.__size == 0:
            print("")
        i = 0
        for i in range(self.__size):
            if self.__position is not None:
                if self.__position[1] > 0 and i == 0:
                    print("")
                    i += 1
                for i in range(self.__position[0]):
                    print(" ", end="")
            for i in range(self.__size):
                print("#", end="")
            print("")

    @property
    def position(self):
        return(self.__postion)

    @position.setter
    def position(self, value):
        if type(position) is not tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
