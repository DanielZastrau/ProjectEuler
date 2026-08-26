"""https://projecteuler.net/problem=187
Aug 26

17 427 258    3.911s    correct
"""

import argparse
import time
import math
import itertools as it
import operator as op
import functools as ft
from typing import Iterator

def main(limit: int = 10**8):

    #! Generate the primes up to limit // 2, because we need only those
    limit_sq = math.isqrt(limit) + 1
    numbers: list[bool] = [True] * ((limit // 2) + 1)

    slice_len = (len(numbers) - 4 + 2 - 1) // 2
    numbers[4::2] = [False] * slice_len

    for n in range(3, limit_sq):
        if numbers[n]:
            # only checking the odd multiples, because even multiples are already covered by 2
            # starting at the square, because previous multiples are covered by previous primes
            start = n**2
            step = 2*n
            slice_len = (len(numbers) - start + step - 1) // step
            numbers[n**2::2*n] = [False] * slice_len
    primes: list[int] = [index for index in range(2, len(numbers)) if numbers[index]]

    print(time.time() - t, len(primes))

    #! Two pointer approach
    composites = 0
    left = 0
    right = len(primes) - 1

    while left <= right:
        if primes[left] * primes[right] < limit:
            # The product is under the limit, meaning primes[left] multiplied 
            # by any prime between left and right is a valid semiprime.
            composites += (right - left + 1)
            left += 1
        else:
            right -= 1

    print(time.time() - t)

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=10**8)
    args = parser.parse_args()

    t = time.time()
    main(limit=args.limit)
    print(time.time() - t)