#!/usr/bin/python3
"""
Contains:
    Functions
    =========
    island_perimeter(grid) - solves the island perimeter problem for given grid
"""


def island_perimeter(grid):
    """Solves the island perimeter problem for the given grid"""
    perimeter = 0
    rows = len(grid)
    columns = len(grid[0])
    for i in range(rows):
        for j in range(columns):
            if grid[i][j]:
                if j == 0 or not grid[i][j - 1]:
                    perimeter += 1
                if j == columns - 1 or not grid[i][j + 1]:
                    perimeter += 1
                if i == 0 or not grid[i - 1][j]:
                    perimeter += 1
                if i == rows - 1 or not grid[i + 1][j]:
                    perimeter += 1
    return perimeter
