#!/usr/bin/python3
"""This module contains a function definition"""


def read_file(filename=""):
    """This function reads a text file and prints it to stdout"""
    with open(filename, "r") as k:
        print(k.read(), end="")
        k.close()
