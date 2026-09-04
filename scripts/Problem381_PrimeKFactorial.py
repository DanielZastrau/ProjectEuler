"""https://projecteuler.net/problem=381
Sep 2026"""

import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op

from typing import Iterator

import commons

@ft.cache
def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)

def expression(p: int) -> int:
    return sum([factorial(p - i) for i in range(5, 0, -1)]) % p

def main (limit: int):

    primes = commons.eratosthenes(limit=limit)[2:]
    print('precomputed primes', len(primes), time.time() - t)

    s = 0
    for p in primes:
        s += expression(p)
    print(s)

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=10**8)
    args = parser.parse_args()

    t = time.time()
    main(limit=args.limit)
    print(time.time() - t)