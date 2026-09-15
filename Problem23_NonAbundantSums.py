"""https://projecteuler.net/problem=23
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

    n = 28124
    divisor_sums: list[int] = [0 for _ in range(30000)]
    abundant_numbers: list[int] = []
    non_abundant_numbers: list[bool] = [True for _ in range(30000)]

    for n in range(1, 30000):
        for nn in range(2 * n, 30000, n):
            divisor_sums[nn] += n

    for n in range(1, 30000):
        if divisor_sums[n] > n:
            abundant_numbers.append(n)

    for index in range(len(abundant_numbers)):
        n1 = abundant_numbers[index]

        for jindex in range(index, len(abundant_numbers)):
            total = n1 + abundant_numbers[jindex]

            if total < 30000:
                non_abundant_numbers[total] = False
            else:
                break

    s = 0
    for n in range(1, 28124):
        if non_abundant_numbers[n]:
            s += n
    print(s)

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    t = time.time()
    main()
    print(time.time() - t)