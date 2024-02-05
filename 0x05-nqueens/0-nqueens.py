#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing
N non-attacking queens on an NxN chessboard.
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


def is_valid_state(state, n):
    """check if the state is valid"""
    # check state
    return len(state) == n


def get_candidates(state, n):
    """generate candidates for solving"""
    if not state:
        return range(n)

    # find the next position in the state
    position = len(state)
    candidates = set(range(n))

    # prune down candidates that place the queen
    for row, col in enumerate(state):
        candidates.discard(col)
        dist = position - row

        candidates.discard(col+dist)
        candidates.discard(col-dist)
    return candidates


def search(state, solutions, n):
    """search through candidates"""
    if is_valid_state(state, n):
        convert_to_2d_array(state)
        solutions.append(state.copy())
        return

    for candidate in get_candidates(state, n):
        state.append(candidate)
        search(state, solutions, n)
        state.pop()


def convert_to_2d_array(state):
    """convert an array to a 2d array"""
    for i in range(len(state)):
        temp = state[i]
        state[i] = [i, temp]


def solveNQueen(n):
    """solve the question"""
    solutions = []
    state = []
    search(state, solutions, n)
    return solutions


for solution in solveNQueen(n):
    print(solution)
