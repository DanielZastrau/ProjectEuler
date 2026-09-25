"""https://projecteuler.net/problem=134
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

precomputed_starts: dict[int, list[int]] = {1 : [10, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                                            2 : [5, -1, 1, -1, 2, -1, 3, -1, 4, -1],
                                            3 : [10, 7, 4, 1, 8, 5, 2, 9, 6, 3],
                                            4 : [5, -1, 3, -1, 1, -1, 4, -1, 2, -1],
                                            5 : [2, -1, -1, -1, -1, 1, -1, -1, -1, -1],
                                            6 : [5, -1, 2, -1, 4, -1, 1, -1, 3, -1],
                                            7 : [10, 3, 6, 9, 2, 5, 8, 1, 4, 7],
                                            8 : [5, -1, 4, -1, 3, -1, 2, -1, 1, -1],
                                            9 : [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]}

precomputed_intervals: dict[int, list[int]] = {1 : [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
                                               2 : [5, -1, 5, -1, 5, -1, 5, -1, 5, -1],
                                               3 : [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
                                               4 : [5, -1, 5, -1, 5, -1, 5, -1, 5, -1],
                                               5 : [2, -1, -1, -1, -1, 2, -1, -1, -1, -1],
                                               6 : [5, -1, 5, -1, 5, -1, 5, -1, 5, -1],
                                               7 : [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
                                               8 : [5, -1, 5, -1, 5, -1, 5, -1, 5, -1],
                                               9 : [10, 10, 10, 10, 10, 10, 10, 10, 10, 10],}

def smallest_multiple(p1: int, p2: int) -> int:

    # length of the first prime
    l = int(math.log10(p1)) + 1
    modulator = 10**l

    start = precomputed_starts[p2 % 10][p1 % 10] * p2   # the first multiple, which shares the last digit
    step = precomputed_intervals[p2 % 10][p1 % 10] * p2    # step to the next such multiple

    for multiple in it.count(start, step):
        if multiple % modulator == p1:
            return multiple
    return -1

def main(limit: int):

    # [2:] cuts off the primes 2 and 3, which we are not considering here
    primes = commons.eratosthenes(limit=limit)[2:]
    print(len(primes))

    # checks the provided example for correctness
    assert smallest_multiple(19, 23) == 1219

    s = 0
    for index in range(len(primes)):
        if time.time() - t > 60:
            break

        # print(index)
        for jindex in range(index + 1, len(primes)):
            s += smallest_multiple(primes[index], primes[jindex])
    print(s)

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=10**6)
    args = parser.parse_args()

    t = time.time()
    main(limit=args.limit)
    print(time.time() - t)