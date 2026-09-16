"""https://projecteuler.net/problem=24
"""

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

def integer_of(perm: tuple[int, ...]) -> int:

    n = 0
    length = len(perm)
    for power in range(length -1, -1, -1):
        n += perm[length - power - 1] * 10**power
    return n

def main():
    print(sorted(map(integer_of, it.permutations(range(10))))[999999])

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    t = time.time()
    main()
    print(time.time() - t)