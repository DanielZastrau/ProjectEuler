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

def count_increasing_numbers_below(total_count: int, remaining_digits: list[int],
                                  remaining_places: int):
    """The assumption is simply that limit is of the form 10**x.
    I.e. it poses a number of digits."""

    for n in remaining_digits:
        total_count += 1
        remaining_places -= 1

        if remaining_places > 0:
            total_count = count_increasing_numbers_below(total_count=total_count,
                                                          remaining_digits=list(range(n, 10)),
                                                          remaining_places=remaining_places)

    return total_count


def count_decreasing_numbers_below(total_count: int, remaining_digits: list[int],
                                  remaining_places: int):
    """The assumption is simply that limit is of the form 10**x.
    I.e. it poses a number of digits."""

    for n in remaining_digits:
        total_count += 1
        remaining_places -= 1

        if remaining_places > 0:
            total_count = count_decreasing_numbers_below(total_count=total_count,
                                                            remaining_digits=list(range(n, -1, -1)),
                                                            remaining_places=remaining_places)

    return total_count

def main(limit: int = 10**100):

    digital_places = int(math.log10(limit))
    count_of_increasing_numbers = count_increasing_numbers_below(total_count=0,
                                                                remaining_places=digital_places,
                                                                remaining_digits=list(range(1, 10)))
    count_of_decreasing_numbers = count_decreasing_numbers_below(total_count=0,
                                                                 remaining_places=digital_places,
                                                                 remaining_digits=list(range(9, 0, -1)))
    # both count constant digits like 1111111.... or 99999999.... these we have to substract
    total_count = count_of_increasing_numbers + count_of_decreasing_numbers - 9
    print(total_count)

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
        print(n)
        d = digits(n)
        if (isincreasing(d) or isdecreasing(d)):
            count += 1
    print(count)

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=10**100)
    args = parser.parse_args()

    t = time.time()
    main(limit=args.limit)
    print(time.time() - t)