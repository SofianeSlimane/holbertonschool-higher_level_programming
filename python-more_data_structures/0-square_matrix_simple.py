#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mx_ = len(matrix)
    numberOfColumns = len(matrix[0])
    new_matrix = [[0] * numberOfColumns for i in range(mx_)]
    print(new_matrix)
    for i in range(mx_):
        for j in range(numberOfColumns):
            value_squared = matrix[i][j] ** 2
            new_matrix[i][j] = value_squared
    print("len matrix : {}".format(mx_))
    print("len new_matrix : {}".format(len(new_matrix)))
    return new_matrix
