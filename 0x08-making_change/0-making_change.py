#!/usr/bin/python3
"""making_change module"""


def makeChange(coins, total):
    """
    return the fewest number of coins needed to meet a given amount total.
    """
    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for j in range(0, len(coins)):
            if coins[j] <= i:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)
    return -1 if dp[total] > total else dp[total]
