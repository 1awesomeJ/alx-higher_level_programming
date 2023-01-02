#!/usr/bin/python3
"""This module contains the definition of a rectangle"""


class Rectangle:
    """
    This is a rectangle whose initialization,
    width and height setter and getter methods defined
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        ret = ""
        for a in range(self.__height):
            for b in range(self.__width):
                ret += str(self.print_symbol)
            if a is not self.__height - 1:
                ret += ("\n")
        return ret

    def __repr__(self):
        ret = f"Rectangle({self.__width}, {self.__height})"
        return ret

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, k):
        if type(k) is not int:
            raise TypeError("width must be an integer")
        if k < 0:
            raise ValueError("width must be >= 0")
        self.__width = k

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, k):
        if type(k) is not int:
            raise TypeError("height must be an integer")
        if k < 0:
            raise ValueError("height must be >= 0")
        self.__height = k

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2*(self.__height + self.__width)

    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return 1
