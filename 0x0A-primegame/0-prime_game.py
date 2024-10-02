#!/usr/bin/python3
"""
Contains:
    isWinner - determines the winner of the prime game
"""


def find_primes(n):
    """Return list of prime numbers between 1 and n inclusive
       Args:
        n (int): upper boundary of range. lower boundary is always 1
    """
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):
    """Determines the collective winner of  x rounds of prime game"""
    score = {
        "Maria": 0,
        "Ben": 0
    }
    for i in range(x):
        num = nums[i]
        primes = find_primes(num)
        score['Maria' if len(primes) % 2 else 'Ben'] += 1
    return ("Maria" if score["Maria"] > score["Ben"]
            else ("Ben" if score["Ben"] > score["Maria"] else None))
