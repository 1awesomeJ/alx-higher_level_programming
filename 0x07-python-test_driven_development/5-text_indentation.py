#!/usr/bin/python3
"""This module contains one function"""


def text_indentation(text):
    """
    This function prints a string addint to every
    occurrence of '.', '?' and ':'  two 2 lines
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i, k in enumerate(text):
        if k in ['.', '?', ':']:
            print(k, end="\n\n")
        elif k == " " and text[i-1] in ['.', '?', ':']:
            print("", end="")
        else:
            print(k, end="")
