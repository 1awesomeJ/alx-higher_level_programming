#!/usr/bin/python3

import sys
argv = sys.argv[1:]

k = len(argv)

if k == 1:
    print("{} argument:".format(k))
    i = 1
    for a in argv:
        print("{}: {}".format(i, a))
        i += 1
if k < 1:
    print("{} arguments.".format(k))

if k > 1:
    print("{} arguments:".format(k))
    i = 1
    for a in argv:
        print("{}: {}".format(i, a))
        i += 1
