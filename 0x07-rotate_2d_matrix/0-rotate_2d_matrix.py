#!/usr/bin/python3
""" An in-place algorithm to rotate an n x n 2D matrix by 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """ Rotate an n x n 2D @matrix by 90 degrees clockwise
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
