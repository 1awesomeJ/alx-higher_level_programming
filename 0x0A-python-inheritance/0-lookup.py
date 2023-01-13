#!/usr/bin/python3
""" This module contains a function """


def lookup(obj):
    """
        This function returns a list of all the methods applicable on an object
    """
    return dir(obj)
