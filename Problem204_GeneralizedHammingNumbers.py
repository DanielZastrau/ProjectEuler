"""https://projecteuler.net/problem=204
Sep 26"""

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

def count(limit: int, primes: list[int]) -> int:

    def dp(num: int, start: int):
        total = 1

        for i in range(start, len(primes)):
            val = num * primes[i]
            if val > limit:
                break
            total += dp(val, i)

        return total
    return dp(1, 0)

def main(prime_limit: int, limit: int):
    print(count(limit, commons.eratosthenes(limit=prime_limit)))

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=10**9)
    parser.add_argument('--prime-limit', type=int, default=100)
    args = parser.parse_args()

    t = time.time()
    main(args.prime_limit, args.limit)
    print(time.time() - t)