"""https://projecteuler.net/problem=231
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


def main(n: int, k: int):

    prime_factors = commons.prime_factorization_sieve(limit=n + 1)

    # these are two distinct set of numbers
    numerator_nums = [n - i for i in range(k)]
    denominator_nums = [i for i in range(1, max(k, n - k) + 1)]
    print(numerator_nums, denominator_nums)

    numerator_factors: list[int] = []
    for i in numerator_nums:
        numerator_factors.extend(prime_factors[i])

    denominator_factors: list[int] = []
    for i in denominator_nums:
        denominator_factors.extend(prime_factors[i])

    for factor in denominator_factors:
        if factor in numerator_factors:
            numerator_factors.remove(factor)

    print(sum(numerator_factors))

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--n', type=int, default=20 * 10**6)
    parser.add_argument('--k', type=int, default=15 * 10**6)
    args = parser.parse_args()

    t = time.time()
    main(n=args.n, k=args.k)
    print(time.time() - t)