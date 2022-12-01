#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]

    sum = 0
    for a in argv:
        sum += int(a)
    print("{:d}".format(sum))
