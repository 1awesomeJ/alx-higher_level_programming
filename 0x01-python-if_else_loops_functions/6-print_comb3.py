#!/usr/bin/python3

for i in range(10):
    for j in range (10):
        if i == 8:
            continue
        if i < j:
            print("{}{}".format(i, j), end=", ")

print(89)
