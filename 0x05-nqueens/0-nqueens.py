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

# def find_solutions(recur, lst, column, i, n):
#     """Returns a list of all the possible solutions of the puzzle for n."""
#     if (i > n):
#         lst.append(recur[:])
#         return lst

#     for j in range(n + 1):
#         if i == 0 or ([i - 1, j - 1] not in recur and
#                       [i - 1, j + 1] not in recur and
#                       j not in column):
#             if i > 1:
#                 diagonal = 0
#                 for k in range(2, i + 1):
#                     if ([i - k, j - k] in recur) or ([i - k, j + k] in recur):
#                         diagonal = 1
#                         break
#                 if diagonal:
#                     continue
#             recur.append([i, j])
#             column.append(j)
#             find_solutions(recur, lst, column, i + 1, n)
#             column.pop()
#             recur.pop()

#     return lst

def find_solutions(n):
    """
    - For each possible solution, we take one position, remove all positions
    where another queen can't be in, and if the number of remaining positions
    is less than the number of queens expected, we discard that solution.
    If not, we take the remaining positions, and for each one, do the same
    process.
    """
    tiles = [[i, j] for i in range(n) for j in range(n)]
    solutions = []
    k = 0
    while k < len(tiles):
        print(tiles)
        solution = [tiles[k]]
        print("Solving for {}".format(tiles[k]))
        board = [[i, j] for i in range(n) for j in range(n)]
        for i in range(1, n):
            curr = solution[-1]
            print("\t- Eliminating for {}".format(curr))
            x, y = curr
            for j in range(n):
                if curr != [x, j] and [x, j] in board:
                    board.remove([x, j])
                if curr != [j, y] and [j, y] in board:
                    board.remove([j, y])
            while x >= 0 and y >= 0:
                if curr != [x, y] and [x, y] in board:
                    board.remove([x, y])
                x -= 1
                y -= 1
            x, y = curr
            while x < n and y < n:
                if curr != [x, y] and [x, y] in board:
                    board.remove([x, y])
                x += 1
                y += 1
            x, y = curr
            while x >= 0 and y < n:
                if curr != [x, y] and [x, y] in board:
                    board.remove([x, y])
                x -= 1
                y += 1
            x, y = curr
            while x < n and y >= 0:
                if curr != [x, y] and [x, y] in board:
                    board.remove([x, y])
                x += 1
                y -= 1
            print("\t Current Solution: {}".format(solution))
            print("\t - Remaining: {}".format(board))
            if len(board) < n:
                print("\t - Less than n")
                print("\t {}".format(board))
                break
            solution.append(board[i])
        if len(solution) == n:
            if sorted(solution) not in solutions:
                print("\t\t - Inserted solution: {}".format(solution))
                solutions.append(sorted(solution))
            # for tile in solution:
            #     if tile in tiles:
            #         print("Removing tile: {}".format(tile))
            #         tiles.remove(tile)
        k += 1

    return solutions
            





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
