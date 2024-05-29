#!/usr/bin/python3




def pascal_triangle(n):
    matrix = []
    for i in range(1, n + 1):
        matrix.append([0] * i)
    print(matrix)
