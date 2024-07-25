#!/usr/bin/python3
"""
Contains:
    Functions
    =========
    pascal_triangle - Accepts a single integer n, and generates the first
    n rows of Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Accepts a single integer n, and generates the first n rows
    of Pascal's Triangle

    Args:
        n (int): The number of rows of the triangle to generate

    Returns:
        list: A list of the first n rows of the triangle
    """
    if n <= 0:
        return ([])
    triangle = [[1]]
    for i in range(1, n):
        row_len = i + 1
        prev_row = triangle[i - 1]
        curr_row = []
        for j in range(row_len):
            op_idx_1 = j - 1
            op_idx_2 = j
            if op_idx_1 < 0 or op_idx_2 >= len(prev_row):
                curr_row.append(1)
            else:
                curr_row.append(prev_row[op_idx_1] + prev_row[op_idx_2])
        triangle.append(curr_row)
    return (triangle)
