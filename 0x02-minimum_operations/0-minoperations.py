#!/usr/bin/python3

"""Calculates the fewest number of operations"""


import math


def minOperations(n):
    """calculates the fewest number of operations"""
    if not isinstance(n, int) or n < 2:
        return 0

    count = 0
    for i in range(2, int(math.sqrt(n))+1):
        while n % i == 0:
            count += i
            n //= i
    if n > 1:
        count += n
    return count
