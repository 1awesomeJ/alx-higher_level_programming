#!/usr/bin/python3
"""This module contains a function definition"""


def read_file(filename=""):
    """This function reads a text file and prints it to stdout"""
    k = open(filename, "r")
    print(k.read(), end="")
