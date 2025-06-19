#!/usr/bin/python3
""" Island perimeter module
"""


def island_perimeter(grid):
    """ Returns the perimeter of the island described in grid
    """

    if not grid or not grid[0]:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # Start with 4 sides for each land cell
                perimeter += 4

                # Subtract 2 for each adjacent land cell (up and left)
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter
