#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for i in range(len(matrix) - 1):
            for j in range(len(matric[i])):
                print("{}".format(matrix[i][j], end=""))
            print()
