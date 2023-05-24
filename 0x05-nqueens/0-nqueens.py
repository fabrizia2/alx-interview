#!/usr/bin/python3
"""N Queens"""

import sys


def is_safe(board, row, col, N):
    """Check if the current position is attacked by any other queen
    in the previous rows"""
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check upper diagonal on the left side
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check upper diagonal on the right side
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(N):
    """Create an empty board"""
    board = [['.' for _ in range(N)] for _ in range(N)]

    def backtrack(row):
        """Base case: If all queens are placed, print the solution"""
        if row == N:
            print_solution(board)
            return

        # Try placing the queen in each column of the current row
        for col in range(N):
            if is_safe(board, row, col, N):
                # Place the queen
                board[row][col] = 'Q'
                # Recur for the next row
                backtrack(row + 1)
                # Remove the queen (backtrack)
                board[row][col] = '.'

    def print_solution(board):
        """Print the board configuration"""
        for row in board:
            print(' '.join(row))
        print()

    backtrack(0)


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
