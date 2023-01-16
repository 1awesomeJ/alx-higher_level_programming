#!/usr/bin/python3
"""This module contains a function"""


def matrix_divided(matrix, div):
    """
    This function takes a list of lists(matrix)
    and divides it by a divisor(div)
    """
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    div = float(div)
    ret = []
    lt = len(matrix[0])
    for i in range(len(matrix)):
        x = []
        if len(matrix[i]) != lt:
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in [int, float]:
                raise TypeError(
                  "matrix must be a matrix (list of lists) of integers/floats")
            k = matrix[i][j]/div
            k = round(k, 2)
            x.append(k)
        ret.append(x)
    return ret
