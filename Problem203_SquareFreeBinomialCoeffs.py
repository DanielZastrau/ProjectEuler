"""https://projecteuler.net/problem=203
Aug 26

34029210557338    13s    correct
"""

import argparse
import time
import math
import itertools as it
import operator as op
import functools as ft
from typing import Iterator

from PrimeSieves import eratosthenes

def main(rows: int = 51):

    uniques: set[int] = set([1])
    for total in range(rows):
        for take in range(1, total):
            uniques.add(math.comb(total, take))


    maximum = max(uniques)
    print(maximum)
    print(len(list(uniques)))
    print(time.time() - t)

    primes = eratosthenes(limit=math.isqrt(maximum) + 1)
    print(time.time() - t)

    square_free_numbers: list[int] = []
    for n in uniques:

        divisor = False
        for prime in primes:
            if n % prime**2 == 0:
                divisor = True
                break

        if not divisor:
            square_free_numbers.append(n)

    print(sum(square_free_numbers))

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--rows', type=int, default=51)
    args = parser.parse_args()

    t = time.time()
    main(rows=args.rows)
    print(time.time() - t)