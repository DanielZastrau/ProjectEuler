"""https://projecteuler.net/problem=113
Sep 26"""

import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op

from typing import Iterator

import commons

def main3(limit: int = 10**100):
    """https://oeis.org/A152054"""
    pass

def amount_increasing_numbers(total_count: int, remaining_digits: range,
                              remaining_places: int) -> int:

    for n in remaining_digits:
        total_count += 1

        if remaining_places - 1 > 0:
            total_count = amount_increasing_numbers(total_count=total_count,
                                                    remaining_digits=range(n, 10),
                                                    remaining_places=remaining_places - 1)

    return total_count

def amount_decreasing_numbers(total_count: int, remaining_digits: range,
                              remaining_places: int) -> int:
    for n in remaining_digits:
        total_count += 1

        if remaining_places - 1 > 0:
            total_count = amount_decreasing_numbers(total_count=total_count,
                                                    remaining_digits=range(n, -1, -1),
                                                    remaining_places=remaining_places - 1)
    return total_count

def amount_inc_and_dec(total_count: int, remaining_digits: range,
                       remaining_places: int) -> int:
    for n in remaining_digits:
        total_count += 1

        if remaining_places - 1 > 0:
            total_count = amount_inc_and_dec(total_count=total_count,
                                             remaining_digits=range(n, n + 1),
                                             remaining_places=remaining_places - 1)
    return total_count

def main(limit: int = 10**100):
    """10**24 takes 41 seconds"""
    
    digital_places = int(math.log10(limit))
    amount1 = amount_increasing_numbers(total_count=0,
                                        remaining_digits=range(1, 10),
                                        remaining_places=digital_places)
    amount2 = amount_decreasing_numbers(total_count=0,
                                        remaining_digits=range(9, 0, -1),
                                        remaining_places=digital_places)
    amount3 = amount_inc_and_dec(total_count=0, remaining_digits=range(1, 10),
                                 remaining_places=digital_places)
    print(amount1 + amount2 - amount3)


def main_naive(limit: int):
    """unsuprisingly this works correctly, but is way too slow"""

    def digits(n: int):
        d: list[int] = []
        q, r = n, 0
        while q > 0:
            q, r = q // 10, q % 10
            d.append(r)
        return d[::-1]

    def isincreasing(d: list[int]):
        for i in range(len(d) - 1):
            if not (d[i] <= d[i + 1]):
                return False
        return True

    def isdecreasing(d: list[int]):
        for i in range(len(d) -1):
            if not (d[i] >= d[i + 1]):
                return False
        return True
    
    count = 0
    for n in range(1, limit):
        d = digits(n)
        if (isincreasing(d) or isdecreasing(d)):
            count += 1
    print(count)

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--which', type=int, default=0)
    parser.add_argument('--limit', type=int, default=10**100)
    args = parser.parse_args()

    t = time.time()
    if args.which == 0:
        main(limit=args.limit)
    elif args.which == 1:
        main_naive(limit=args.limit)
    print(time.time() - t)