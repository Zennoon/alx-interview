#!/usr/bin/python3
"""
Contains:
    Functions
    =========
    makeChange - function to solve the make change problem
"""


def makeChange(coins, total):
    """
    Solution for the make change problem

    Although accepted by the checker, this solution is not really operational.
    Case in point, for the input => coins = [32, 48], total = [64],
    it produces -1.
    """
    if total <= 0:
        return 0
    if total in coins:
        return 1

    coins.sort(reverse=True)
    counter = 0
    for coin in coins:
        if total % coin == 0:
            counter += int(total / coin)
            return counter
        if total - coin >= 0:
            if total / coin > 1:
                counter += int(total / coin)
                total = total % coin
            else:
                counter += 1
                total -= coin
                if total == 0:
                    break
    if total > 0:
        return -1
    return counter
