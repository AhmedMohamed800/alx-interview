#!/usr/bin/python3
"""making_change module"""


def min_great_than_zero(coins, total):
    """min_great_than_zero"""
    min = total - coins[0]
    for coin in coins:
        coin = total - coin
        if min > coin and coin > 0:
            min = coin
    return min


def search(steps, coins, total):
    """DFS"""
    if total < 0:
        return -1
    if total == 0:
        return steps

    shortest = min_great_than_zero(coins, total)
    steps += 1
    return search(steps, coins, shortest)


def makeChange(coins, total):
    """
    return the fewest number of coins needed to meet a given amount total.
    """
    return search(-1, coins, total)
