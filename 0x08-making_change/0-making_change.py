#!/usr/bin/python3
"""
Contains:
    Functions
    =========
    makeChange - function to solve the make change problem
"""


def makeChange(coins, total):
    """Function to solve the make change problem"""
    if total <= 0:
        return 0
    coins.sort()
    all_nums = {i: total+1 for i in range(total + 1)}
    all_nums[0] = 0
    for i in range(1, len(all_nums)):
        for coin in coins:
            if i - coin < 0:
                break
            else:
                all_nums[i] = min(all_nums[i], 1 + all_nums[i - coin])
    if all_nums[total] > total:
        return -1
    return all_nums[total]
