#!/usr/bin/python3
"""
Contains:
    Functions
    =========
    minOperations - Assuming we have one character in a file
    and we can perform two operation: copy all, and paste, the
    function returns the minimum number of operations it would take
    to reach a given number of characters
"""


def minOperations(n: int) -> int:
    """
    Assuming we have one character in a file
    and we can perform two operation: copy all, and paste, the
    function returns the minimum number of operations it would take
    to reach a given number of characters
    """
    if n < 1:
        return 0
    prime_factors = {}
    for i in range(2, n + 1):
        while n % i == 0:
            if i in prime_factors:
                prime_factors[i] += 1
            else:
                prime_factors[i] = 1
            n /= i
        if n <= 1:
            break
    return (sum([key * val for key, val in prime_factors.items()]))
