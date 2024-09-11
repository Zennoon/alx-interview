#!/usr/bin/python3
"""
Rotating a 2D matrix
___________       ___________
| 1  2  3 |       | 7  4  1 |
| 4  5  6 | --->  | 8  5  2 |
| 7  8  9 |       | 9  6  3 |
-----------       -----------
"""


def rotate_2d_matrix(matrix):
    """Rotates matrix 90 degrees"""
    n = len(matrix)
    k = 0
    while n > 1:
        for i in range(n-1):
            carrier = None
            replacements = [
                [k, k + i],
                [k + i, k + n - 1],
                [k + n - 1, k + n - 1 - i],
                [k + n - 1 - i, k],
                [k, k + i]
            ]
            for repl in replacements:
                tmp = matrix[repl[0]][repl[1]]
                if carrier is not None:
                    matrix[repl[0]][repl[1]] = carrier
                carrier = tmp
        n -= 2
        k += 1
