#!/usr/bin/python3
"""N quens"""
import sys


def print_board(board, n):
    """Print allocaed posiions to quen"""
    b = []

    for i in range(n):
        for j in range(n):
            if j == board[i]:
                b.append([i, j])
    print(b)


def is_position_safe(board, i, j, r):
    """Checks if position is safe fo queen"""
    return board[i] in (j, j - i + r, i - r + j)


def safe_positions(board, row, n):
    """Find all saf positions where queen can be allocated"""
    if row == n:
        print_board(board, n)

    else:
        for j in range(n):
            allowed = True
            for i in range(row):
                if is_position_safe(board, i, j, row):
                    allowed = False
            if allowed:
                board[row] = j
                safe_positions(board, row + 1, n)


def create_board(size):
    """Generates board"""
    return [0 * size for i in range(size)]


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except BaseException:
    print("N must be a number")
    exit(1)

if (n < 4):
    print("N must be at least 4")
    exit(1)

board = create_board(int(n))
row = 0
safe_positions(board, row, int(n))