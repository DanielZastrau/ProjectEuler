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

def binomial(n: int, m: int) -> int:
    return math.factorial(n) // (math.factorial(n - m) * math.factorial(m))

def n_digit_bouncy_numbers(digital_places: int) -> int:
    first_summand: int = 9 * 10**(digital_places - 1)
    second_summand: int = ((digital_places + 18) * binomial(digital_places + 8, 8) // 9)

    return first_summand - second_summand + 10

def main(limit: int = 10**100):
    """https://oeis.org/A152054"""

    digital_places = int(math.log10(limit))
    amount_non_bouncy_numbers = 0
    for number_digits in range(1, digital_places + 1):
        amount_n_digit_bouncy_numbers = n_digit_bouncy_numbers(number_digits)
        n_digit_numbers = 10**number_digits - 10**(number_digits - 1)
        amount_non_bouncy_numbers += n_digit_numbers - amount_n_digit_bouncy_numbers
    print(amount_non_bouncy_numbers)

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