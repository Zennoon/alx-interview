#!/usr/bin/python3
"""
Contains:
    isWinner - determines the winner of the prime game
"""


def find_primes(num):
    """Find the prime numbers less than or equal to n
    using the sieve of Eratosthenes"""
    candidates = [i for i in range(2, num + 1)]
    i = 0
    while i < len(candidates):
        focal = candidates[i]
        j = 2
        while (focal * j <= candidates[-1]):
            if ((focal * j) >= focal ** 2 and (focal * j) in candidates):
                candidates.remove(focal * j)
            j += 1
        i += 1
    return candidates


def isWinner(x, nums):
    """Determines the collective winner of  x rounds of prime game"""
    if x is None or nums is None or x == 0 or nums == []:
        return None
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
