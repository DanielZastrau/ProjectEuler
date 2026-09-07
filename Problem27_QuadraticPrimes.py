import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op

from typing import Iterator

import commons


def quadratic(t: tuple[int, int], x: int) -> int:
    return x**2 + t[0]*x + t[1]

def largest_product(C: Iterator[tuple[int, int]]) -> int:
    max_n = 0
    max_t = (-1, -1)
    for t in C:
        x = 0
        while commons.isprime(quadratic(t, x)):
            x += 1
        if x > max_n:
            max_n = x
            max_t = t

    return max_t[0] * max_t[1]

def main():
        
    n = 1000
    nums = [x for x in range (-n + 1, n)]
    primes = commons.eratosthenes(limit=n)
    pairs = it.product(nums, primes)
    print(largest_product(pairs))

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    t = time.time()
    main()
    print(time.time() - t)