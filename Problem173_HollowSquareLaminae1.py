"""https://projecteuler.net/problem=173
Sep 26"""

import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op

from typing import Iterator

import commons

def main(limit: int):

    count = 0
    last_start_even = 2
    last_start_odd = 1
    for n in range(3, limit):
        if 2 * n + 2 * (n - 2) > limit:
            break

        parity = n % 2
        if parity == 0:
            start = last_start_even
        else:
            start = last_start_odd

        for m in range(start, n, 2):

            if n**2 - m**2 <= limit:
                count += (n - m) // 2

                if parity == 0:
                    last_start_even = m
                else:
                    last_start_odd = m

                break

    print(count)

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=10**6)
    args = parser.parse_args()

    t = time.time()
    main(limit=args.limit)
    print(time.time() - t)