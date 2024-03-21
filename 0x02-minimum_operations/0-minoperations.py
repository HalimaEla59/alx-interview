#!/usr/bin/python3
""" minOperations(n) function"""


def minOperations(n):
    """
    calculates the fewest number of operations needed
    to result in exactly n H characters in the file
    """
    if n < 2:
        return 0
    counter = 0
    i = 2
    while i <= n:
        # checking if i devides n
        if n % i == 0:
            # total even-divisions is the number of operations
            counter += i
            n = n / i
            i -= 1
        # increment i until we get n % i = 0
        i += 1
    return counter
