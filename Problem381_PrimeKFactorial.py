"""https://projecteuler.net/problem=381
Sep 2026 ~ 4 hours"""

import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op

from typing import Iterator

import commons

def modular_inverse(n: int, p: int) -> int:
    """Modified extended Euler algorithm"""
    t, new_t = 0, 1
    r, new_r = p, n

    while new_r != 0:
        q = r // new_r
        t, new_t = new_t, t - q * new_t
        r, new_r = new_r, r - q * new_r

    if r > 1:
        return -1
    if t < 0:
        t = t + p

    return t

def expression(p: int) -> int:

        mod_inv1 = modular_inverse(p - 2, p)
        mod_inv2 = modular_inverse(p - 3, p)
        mod_inv3 = modular_inverse(p - 4, p)
        return (mod_inv1 * ( 1 + mod_inv2 * (1 + mod_inv3))) % p

def main(limit: int):

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