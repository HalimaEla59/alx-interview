#!/usr/bin/python3
"""
Maria and Ben are playing a game.
Given a set of consecutive integers starting from 1 up to and including n,
they take turns choosing a prime number from the set and removing that
number and its multiples from the set. The player that cannot make
a move loses the game.

They play x rounds of the game,
where n may be different for each round.
Assuming Maria always goes first and both players play optimally,
determine who the winner of each game is.
"""


def primeNumbers(n):
    """
    Return:
        list of prime numbers between 1 and n inclusive
    """
    primeNlist = []
    filtered = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filtered[prime]):
            primeNlist.append(prime)
            for i in range(prime, n + 1, prime):
                filtered[i] = False
    return primeNlist


def isWinner(x, nums):
    """
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        primeNlist = primeNumbers(nums[i])
        if len(primeNlist) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
