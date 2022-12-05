#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix[0] == []: 
        print ("{}".format("\n"), end="")
    for a in matrix:
        k = len(a)
        
        for i in range(k):
            if i < (k - 1):
                print("{:d}".format(a[i]), end=" ")
            else:
                print("{:d}".format(a[i]))
