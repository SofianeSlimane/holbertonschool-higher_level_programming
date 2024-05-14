#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mx_ = len(matrix)
    new_matrix = [[0] * mx_] * mx_
    square = lambda num: num * num
    for i in range(mx_):
        for j in range(mx_):
            new_matrix[i][j] = square(matrix[i][j])
    return new_matrix 
