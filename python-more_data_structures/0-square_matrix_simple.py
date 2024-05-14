#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mx_ = len(matrix)
    new_matrix = [[0] * mx_ for i in range(mx_)]
    for i in range(mx_):
        for j in range(mx_):
            value_squared = matrix[i][j] ** 2
            new_matrix[i][j] = value_squared
    return new_matrix
