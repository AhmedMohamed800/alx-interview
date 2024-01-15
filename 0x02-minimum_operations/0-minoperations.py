#!/usr/bin/python3
"""
0-minoperations
"""


def minOperations(n):
    """minOperations1"""
    current_position = 1
    starting_point = 0
    step_counter = 0
    while current_position < n:
        remainder = n - current_position

        if remainder % current_position == 0:
            starting_point = current_position
            current_position += starting_point
            step_counter += 2
        else:
            current_position += starting_point
            step_counter += 1
    return step_counter
