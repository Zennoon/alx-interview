#!/usr/bin/python3
"""
Contains:
    isWinner - determines the winner of the prime game
"""


def find_primes(num):
    """Find the prime numbers less than or equal to n
    using the sieve of Eratosthenes"""
    prime = []
    sieve = [True for i in range(num + 1)]
    for i in range(2, num + 1):
        if (sieve[i]):
            prime.append(i)
            j = 2
            while i * j <= num:
                sieve[i * j] = False
                j += 1
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
