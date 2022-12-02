#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    words = dir(hidden_4)

    for a in words:
        if a[:2] != '__':
            print("{:s}".format(a))
