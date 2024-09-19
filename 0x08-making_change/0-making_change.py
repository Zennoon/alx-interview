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
    """
    if total <= 0:
        return 0
    if total in coins:
        return 1

    coins.sort(reverse=True)
    counter = 0
    for i in coins:
        if total % i == 0:
            counter += int(total / i)
            return counter
        if total - i >= 0:
            if total / i > 1:
                counter += int(total / i)
                total = total % i
            else:
                counter += 1
                total -= i
                if total == 0:
                    break
    if total > 0:
        return -1
    return counter
