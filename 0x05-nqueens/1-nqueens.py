#!/usr/bin/python3
"""
N-queens problem
"""
import sys


def copy_2d_board(board):
    return [[*tile] for tile in board]


def remove_opposing(curr, board, n):
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


def find_solutions(board, solution, curr, i, n, solutions):
    """Find solutions"""
    # print("\n\n\n")
    # print(board, solution, curr, i, n, solutions)
    # print("\n\n\n")
    if i == n - 1:
        solution.append(curr)
        if sorted(solution) not in solutions:
            solutions.append(sorted(solution))
        return
    remove_opposing(curr, board, n)
    if len(board) < n - i:
        return
    solution.append(curr)
    board.remove(curr)
    for tile in board:
        new_board = copy_2d_board(board)
        new_solution = copy_2d_board(solution)
        find_solutions(new_board, new_solution, tile, i + 1, n, solutions)
    return


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
    solutions = []
    first_col = [[0, i] for i in range(n)]
    for tile in first_col:
        board = [[i, j] for i in range(n) for j in range(n)]
        find_solutions(board, [], tile, 0, n, solutions)
    for solution in solutions:
        print(solution)


main()