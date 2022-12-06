#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        k = (len(sentence), None)
    else:
        k = (len(sentence), sentence[0])
    return k
