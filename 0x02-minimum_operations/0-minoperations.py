#!/usr/bin/python3
"""
0-minoperations
"""


def minOperations(n):
    """Min operations"""
    if n <= 0:
        return 0
    minOp = n
    for i in range(1, round(n / 2)):
        if n % i == 0:
            minOp = min(round(n / i) + i, minOp)
    return minOp
