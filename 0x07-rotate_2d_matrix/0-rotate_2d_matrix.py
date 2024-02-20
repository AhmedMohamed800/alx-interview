#!/usr/bin/python3
"""rotate_2d_matrix module"""


def rotate_2d_matrix(matrix):
    """rotate_2d_matrix function"""
    list_len = len(matrix)
    move_one_column_left = 1
    sub = list_len - 1

    for list in matrix:
        list.reverse()

    for i in range(list_len - 1):
        for y in range(list_len - move_one_column_left):
            temp = matrix[y+sub][i+sub]
            matrix[y][i], matrix[y+sub][i+sub] = temp, matrix[y][i]
            sub -= 1
        move_one_column_left += 1
        sub = list_len - (i + 1) - 1
