#!/usr/bin/python3

"""This module contains one function"""
import numpy as mp


def lazy_matrix_mul(m_a, m_b):
    """This function multiplies two matrices"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for k in m_a:
        if type(k) is not list:
            raise TypeError("m_a must be a list of lists")
    for k in m_b:
        if type(k) is not list:
            raise TypeError("m_b must be a list of lists")
    if not len(m_a) or not len(m_a[0]):
        raise ValueError("m_a can't be empty")
    if not len(m_b) or not len(m_b[0]):
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
    A = len(m_a[0])
    B = len(m_b)
    rows = len(m_a)
    columns = len(m_b[0])
    if A != B:
        raise ValueError("m_a and m_b can't be multiplied")

    C = mp.matmul(m_a, m_b)
    return C
