#!/usr/bin/python3
"""Minimum operations"""


def minOperations(n: int) -> int:
    """Calculates the fewest number of operations needed to \
    result in exactly n H characters in the file"""
    if n < 2:
        return 0

    ops = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            ops += factor
            n //= factor
        factor += 1

    return ops
