"""https://projecteuler.net/problem=187
Aug 26

17 427 258    14.366s    correct
"""

import argparse
import time
import math
import itertools as it
import operator as op
import functools as ft
from typing import Iterator

def main(limit: int = 10**8):

    limit_sq = math.isqrt(limit) + 1

    # Offset by 2, i.e., value 2 is at index 0
    numbers: list[bool] = [True] + [n % 2 == 1 for n in range(3, (limit + 1) // 2)]

    for n in range(3, limit_sq):
        if numbers[n - 2]:

            #! only checking the odd multiples, because even multiples are already covered by 2
            #! starting at the square, because previous multiples are covered by previous primes
            nn = n**2
            while nn < limit // 2:
                numbers[nn - 2] = False
                nn += 2*n

    primes: list[int] = [index + 2 for index in range(len(numbers)) if numbers[index]]
    print(time.time() - t, len(primes))

    composites = 0
    for i in range(len(primes)):
        for j in range(i, len(primes)):

            if primes[i] * primes[j] < limit:
                composites += 1
            else:
                break
    print(composites)

    print(time.time() - t)

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=10**8)
    args = parser.parse_args()

    t = time.time()
    main(limit=args.limit)
    print(time.time() - t)