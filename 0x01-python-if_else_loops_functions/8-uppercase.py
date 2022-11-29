#!/usr/bin/python3
def uppercase(str):
    str1= str + "\n"
    for k in str1:
        if 97 <= ord(k) <= 122:
           print("{}".format(chr(ord(k) - 32)), end = "")
        else:
           print("{}".format(k), end = "")
