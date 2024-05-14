#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mx_ = len(matrix)
    new_matrix = [[0] * mx_] * mx_
    square = lambda num: num * num
    for i in range(mx_):
        for j in range(mx_):
            value_squared = square(matrix[i][j])
            new_matrix[i][j] = value_squared
    return new_matrix 
