#!/usr/bin/python3
"""This module contains a locked class"""


class LockedClass:
    """This is a locked class"""
    def __init__(self, first_name=None):
        self.first_name = first_name

    def __setattr__(self, name, k):
        if name != "first_name":
            raise AttributeError(
                  f"'LockedClass' object has no attribute '{name}'")
        self.__dict__[name] = k
