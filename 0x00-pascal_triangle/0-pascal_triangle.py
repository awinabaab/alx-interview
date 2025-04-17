#!/usr/bin/python3
"""Pascal triangle module"""


def pascal_triangle(n):
    """
    Computes Pascal's triangle from 1 to `n`

    Parameters:
        n (int): limit of the Pascal triangle

    Returns:
        A list of lists on integers representin the Pascal's triangle of `n`.
    """

    if n <= 0:
        return []

    rows = [[1]]

    for number in range(1, n):
        row = [1]

        for column in range(1, number):
            row.append(rows[number-1][column-1] + rows[number-1][column])
        row.append(1)
        rows.append(row)

    return rows
