#!/usr/bin/python3
"""Function returns a list of lists of n representing Pascal triangle"""


def pascal_triangle(n):
    """Returns an empty list if n <= 0, assume n will be always int"""
    if n <= 0:
        return []

    triangle = [0] * n

    for i in range(n):
        row = [0] * (i+1)
        row[0] = 1
        row[len(row) - 1] = 1

        for j in range(1, i):
            if j > 0 and j < len(row):
                x1 = triangle[i - 1][j]
                x2 = triangle[i - 1][j - 1]
                row[j] = x1 + x2

        triangle[i] = row

    return triangle
