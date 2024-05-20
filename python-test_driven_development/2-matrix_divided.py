#!/usr/bin/python3
def matrix_divided(matrix, div):
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    elif isinstance(div, float) is False and isinstance(div, int) is False:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    len_m = len(matrix)
    numberOfColumns = len(matrix[0])
    new_matrix = [[0] * numberOfColumns for i in range(len_m)]
    value_div = 0
    is_int= True
    is_float = True
    for i in range(len_m):
        if is_int is False:
            break
        for j in range(numberOfColumns):
            if not isinstance(matrix[i][j], int):
                is_int = False
                break
    for i in range(len_m):
        if is_float is False:
            break
        for j in range(numberOfColumns):
            if not isinstance(matrix[i][j], float):
                is_float = False
                break


    if is_float is True or is_int is True:
        for j in range(len_m):
            for k in range(numberOfColumns):
                value_div = round(matrix[j][k] / div, 2)
                new_matrix[j][k] = value_div
    else:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return new_matrix

