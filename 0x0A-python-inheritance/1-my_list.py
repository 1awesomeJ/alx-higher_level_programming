#!/usr/bin/python3
""" This module contains a function """


class MyList(list):
    """
    This class inherits from the list class
    """
    def print_sorted(self):
        k = self.copy()
        k.sort()
        print(k)
