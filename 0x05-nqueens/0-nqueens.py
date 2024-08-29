#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""101-nqueens.py

Author: Yunus Kedir

This module holds a program that attempts to solve the N-Queens puzzle given
the N value from the command line.

"""
import sys


def find_solutions(n):
    """Returns a list of all the possible solutions of the puzzle for n.

    Args:
        n (int): The number of queens to be placed in an n*n board.

    Returns:
        (list<list<list<int>>>): A list of all possible solutions.
    """
    solutions = []
    factor = 2
    starter = 1
    for i in range(n - 2):
        solution = []
        y = starter
        for x in range(n):
            if y >= n:
                y = y - 1 - n if y > n else 0
            solution.append([x, y])
            y += factor
        starter += 1
        factor += 1
        solutions.append(solution)
    return (solutions)


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
    solutions = find_solutions(n)
    for solution in solutions:
        print(solution)


main()