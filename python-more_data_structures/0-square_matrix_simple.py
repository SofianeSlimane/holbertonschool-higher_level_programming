#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mx_ = len(matrix)
    numberOfColumns = len(matrix[0])
    new_matrix = [[0] * numberOfColumns for i in range(mx_)]
    for i in range(mx_):
        for j in range(numberOfColumns):
            value_squared = matrix[i][j] ** 2
            new_matrix[i][j] = value_squared
    return new_matrix
