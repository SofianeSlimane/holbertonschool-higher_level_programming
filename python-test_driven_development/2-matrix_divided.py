#!/usr/bin/python3
"This module contains the matrix_divided function"""


def matrix_divided(matrix, div):
    """Divide each number in a matrix by given divisor
    Args:
        matrix: matrix (list of lists)
        div: divisor

    Raises:
        TypeError: if elements in matrix are not all integer or all floats
        TypeError: if rows are not all the same size
        TypeError: if div is not an integer or a float
        ZeroDivisionError: if div is 0

    Returns:
        New matrix of all elements divided by div
    """
    if isinstance(div, float) is False and isinstance(div, int) is False:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    if len(matrix) > 1:
        for i in matrix:
            if len(i) != len(matrix[1]):
                raise TypeError("Each row of the matrix must "
                                "have the same size")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    len_m = len(matrix)
    numberOfColumns = len(matrix[0])

    new_matrix = [[0] * numberOfColumns for i in range(len_m)]
    value_div = 0
    is_int = True
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
    elif isinstance(matrix, list) is False:
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    else:
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    return new_matrix
