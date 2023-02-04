#!/usr/bin/python3
"""This module contains a function definition"""


def append_write(filename="", text=""):
    """This function writes a string into a text file"""
    with open(filename, "a") as k:
        num = k.write(text)
        k.close()
    return num
