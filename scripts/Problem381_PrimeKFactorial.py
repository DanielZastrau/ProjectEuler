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

@ft.cache
def folding_modulo_factorial(n: int, modulo: int) -> int:

    if n == 0:
        return 1
    if n == 1 or n == 2:
        return 2
    
    if n % 2 == 0:
        nums = [m for m in range(1, n + 1)]
        l = n
    else:
        nums = [1] + [m for m in range(1, n + 1)]
        l = n + 1

    I = l // 2
    for _ in range(I):
        nums = [(nums[i] * nums[l - 1 - i]) % modulo for i in range(l//2)]
        l //= 2
        if l % 2 == 1:
            nums = [1] + nums
            l += 1

    return nums[0]

def expression_with_folding(p: int) -> int:
    return (sum([folding_modulo_factorial(p - i, p) for i in range(5 , 0, -1)])) % p

def main(limit: int, which: int):

    primes = commons.eratosthenes(limit=limit)[2:]
    print('precomputed primes', len(primes), time.time() - t)

    s = 0
    for p in primes:
        print(p)
        if which == 0:
            s += expression(p)
        else:    # which == 1:
            s += expression_with_folding(p)
    print(s)

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=10**8)
    parser.add_argument('--which', type=int, default=0, choices=[0, 1])
    args = parser.parse_args()

    t = time.time()
    main(limit=args.limit, which=args.which)
    print(time.time() - t)