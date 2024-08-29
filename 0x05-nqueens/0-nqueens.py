#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""101-nqueens.py

Author: Yunus Kedir

This module holds a program that attempts to solve the N-Queens puzzle given
the N value from the command line.

"""
import sys


# def find_solutions(n):
#     """Returns a list of all the possible solutions of the puzzle for n.

#     Args:
#         n (int): The number of queens to be placed in an n*n board.

#     Returns:
#         (list<list<list<int>>>): A list of all possible solutions.
#     """
#     solutions = []
#     factor = 2
#     starter = 1
#     for i in range(n - 2):
#         solution = []
#         y = starter
#         for x in range(n):
#             if y >= n:
#                 y = y - 1 - n if y > n else 0
#             solution.append([x, y])
#             y += factor
#         starter += 1
#         factor += 1
#         solutions.append(solution)
#     return (solutions)

def find_solutions(recur, lst, column, i, n):
    """Returns a list of all the possible solutions of the puzzle for n."""
    if (i > n):
        lst.append(recur[:])
        return lst

    for j in range(n + 1):
        if i == 0 or ([i - 1, j - 1] not in recur and
                      [i - 1, j + 1] not in recur and
                      j not in column):
            if i > 1:
                diagonal = 0
                for k in range(2, i + 1):
                    if ([i - k, j - k] in recur) or ([i - k, j + k] in recur):
                        diagonal = 1
                        break
                if diagonal:
                    continue
            recur.append([i, j])
            column.append(j)
            find_solutions(recur, lst, column, i + 1, n)
            column.pop()
            recur.pop()

    return lst


def main():
    """Initiates the program, extracts the command line arguments, checks for
    their validity, and prints the solutions one line at a time."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = find_solutions([], [], [], 0, n - 1)
    for solution in solutions:
        print(solution)


main()
