#!/usr/bin/python3
"""
0-island_perimeter.py
"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    def dfs(i, j):
        if i < 0 or j < 0 or i >= len(grid):
            return 1
        if j >= len(grid[0]) or grid[i][j] == 0:
            return 1
        if grid[i][j] == -1:
            return 0

        grid[i][j] = -1
        return dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)

    for i in range(len(grid)):
        for j in range(i):
            if grid[i][j] == 1:
                return dfs(i, j)

    return 0
