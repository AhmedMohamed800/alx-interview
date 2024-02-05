#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens on an NxN chessboard.
"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)
except ValueError:
    print("N must be a number")
    exit(1)

