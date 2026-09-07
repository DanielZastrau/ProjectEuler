"""https://projecteuler.net/problem=125
Aug 26

limit=      1 000     11            4 164    0.000633    correct
limit=100 000 000    168    2 916 867 073    0.4405      wrong
limit=100 000 000    159    2 897 741 832    0.437       wrong    fixed the looping index for the end
limit=100 000 000    168    2 906 969 179    0.4199      correct    apparently, just iterating over square chains can yield the same palindrome twice
"""

import argparse
import time
import math
import itertools as it
import operator as op
import functools as ft
from typing import Iterator

def is_palindrome(n: int) -> bool:

    s = str(n)
    return s == s[::-1]

def main(limit: int):

    squares: list[int] = [n**2 for n in range(1, math.isqrt(limit) + 1)]

    amount = 0
    palindromes: set[int] = set()

    for chain_length in it.count(start=2, step=1):

        if sum(squares[:chain_length]) > limit:
            break

        for start in range(len(squares) - chain_length + 1):
            n = sum(squares[start : start + chain_length])

            if n >= limit:
                break

            if is_palindrome(n):
                amount += 1
                palindromes.add(n)

    print(amount, sum(list(palindromes)))

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=10**8)
    args = parser.parse_args()

    t = time.time()
    main(limit=args.limit)
    print(time.time() - t)