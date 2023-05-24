#!/usr/bin/python3
"""N Queens"""

import sys


def is_safe(board, row, col, N):
    """Check if the current position is attacked by any other queen
    # in the previous rows"""
    for i in range(row):
        if board[i] == col:
            return False
        if board[i] + i == row + col:
            return False
        if board[i] - i == col - row:
            return False
    return True


def solve_nqueens(N):
    """Create an empty board"""
    board = [-1] * N
    solutions = []

    def backtrack(row):
        """Base case: If all queens are placed, add the solution"""
        if row == N:
            solutions.append(board[:])
            return

        # Try placing the queen in each column of the current row
        for col in range(N):
            if is_safe(board, row, col, N):
                # Place the queen
                board[row] = col
                # Recur for the next row
                backtrack(row + 1)
                # Remove the queen (backtrack)
                board[row] = -1

    backtrack(0)

    # Print the solutions
    for solution in solutions:
        print_solution(solution)


def print_solution(board):
    """Print the board configuration"""
    print('[', end='')
    for i in range(len(board)):
        print('[{}, {}]'.format(i, board[i]), end='')
        if i < len(board) - 1:
            print(', ', end='')
    print(']')


if __name__ == '__main__':
    # Check the command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N)
