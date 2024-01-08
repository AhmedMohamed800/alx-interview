#!/usr/bin/python3
"""canUnlockAll function"""


def canUnlockAll(boxes):
    """see if all boxes can be opened or not"""
    keys = {0}
    stack = [boxes[0]]
    while stack:
        pop = stack.pop()
        for index in pop:
            if index in keys or index >= len(boxes):
                continue
            stack.append(boxes[index])
            keys.add(index)
    return len(keys) == len(boxes)
