#!/usr/bin/python3
"""This module contains the pascal_triangle function"""


def pascal_triangle(n):
    """This function returns a matrix of integers
    representing the Pascal's triangle of n.
    Args:
        n: number of rows in the triangle
    Returns: Pascal triangle matrix
    """
    matrix = []
    if n <= 0:
        return matrix

    for i in range(1, n + 1):
        matrix.append([1] * i)

    for i in range(n):
        if not len(matrix[i]) <= 2:
            for j in range(1, len(matrix[i]) - 1):
                matrix[i][j] = matrix[i - 1][j - 1] + matrix[i - 1][j]

    return matrix
