#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[i])):
            col = matrix[i][j]
            print("{}".format(col), end=" " if col != matrix[-1] else "" ))
        print()
