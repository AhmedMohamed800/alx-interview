#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """create scal tringle"""
    if n < 1:
        return []
    pascal_array = [[1]]
    for i in range(1, n):
        last_row = pascal_array[i - 1]
        new_array = []
        for j in range(0, len(last_row) + 1):
            if j == 0 or j == len(last_row):
                new_array.append(1)
            else:
                new_array.append(last_row[j - 1] + last_row[j])
        pascal_array.append(new_array)

    return pascal_array
