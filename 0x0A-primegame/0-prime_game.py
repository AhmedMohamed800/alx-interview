#!/usr/bin/python3
"""0-prime_game.py"""

def get_primes(n):
    """Return list of prime numbers between 1 and n inclusive"""
    primes = []
    sieve = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (sieve[prime]):
            primes.append(prime)
            for i in range(prime, n + 1, prime):
                sieve[i] = False
    return primes


def isWinner(x, nums):
    """DET if Ben will win the game or Maria"""
    if x is None or nums is None or x == 0 or nums == []:
        return None
    
    Maria = 0
    Ben = 0

    for i in range(x):
        primes = get_primes(nums[i])
        if len(primes) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None