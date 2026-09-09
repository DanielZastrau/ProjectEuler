"""https://projecteuler.net/problem=46
"""

import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op

from typing import Iterator

import commons

def expression(prime: int, j: int) -> int:
    return prime + 2 * j**2

def find_j(prime: int, num: int) -> int:
    for j in range(math.isqrt(num)):
        if expression(prime, j) >= num:
            return j
    return j

def conjecture(num: int, primes: list[int]):
    for prime in primes:
        if prime > num:
            return False
        if expression(prime, find_j(prime, num)) == num:
            return True
    return False

def main():
    primes = commons.eratosthenes(limit=10000)

    for n in range(3, 10000, 2):
        if not commons.isprime(n) and not conjecture(n, primes):
            print(n)
            break

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    t = time.time()
    main()
    print(time.time() - t)