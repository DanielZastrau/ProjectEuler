"""https://projecteuler.net/problem=31
"""

import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op
import fractions as fr
import heapq

from typing import Iterator

import commons

def dp(target: int, coins: list[int]) -> int:

    ways = [0] * (target + 1)
    ways[0] = 1

    for coin in coins:
        for amount in range(coin, target + 1):
            ways[amount] += ways[amount - coin]

    return ways[target]

def main():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    target = 200
    print(dp(target, coins))

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    t = time.time()
    main()
    print(time.time() - t)