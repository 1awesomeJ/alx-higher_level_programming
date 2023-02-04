#!/usr/bin/python3
"""This module contains a function definition"""


def write_file(filename="", text=""):
    """This function writes a string into a text file"""
    with open(filename, "w") as k:
        num = k.write(text)
        k.close()
    return num
