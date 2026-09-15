"""https://projecteuler.net/problem=21
"""

import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op
import fractions as fr

from typing import Iterator

import commons

def main():

    divisor_sums: list[int] = [0 for _ in range(10000)]

    for n in range(1, 10000):
        for nn in range(2 * n, 10000, n):
            divisor_sums[nn] += n

    s = 0
    for m in range(10000):
        n = divisor_sums[m]
        if n <= 10000 and m != n and divisor_sums[n] == m:
            s += m
    print(s)

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    t = time.time()
    main()
    print(time.time() - t)