"""https://projecteuler.net/problem=145
Aug 26

limit=0 000 001 000    000 120    000.000290s
limit=0 000 010 000    000 720    000.00235s
limit=0 000 100 000    000 720    000.00218s
limit=0 001 000 000    018 720    000.198s
limit=0 010 000 000    068 720    002.287s
limit=0 100 000 000    608 720    021.749s
limit=1 000 000 000    608 720    021.554s    correct answer
"""

import argparse
import time
import math
import itertools as it
import operator as op
import functools as ft
from typing import Iterator

def main(limit: int = 10**9):

    evens = set('02468')

    search_ranges = [
        (10, 100),               # Length 2
        (100, 1000),             # Length 3
        (1000, 10000),           # Length 4
        (100000, 1000000),       # Length 6
        (1000000, 10000000),     # Length 7
        (10000000, 100000000)    # Length 8
    ]

    search_ranges = [(start, stop) for start, stop in search_ranges if stop <= limit]
    
    amount = 0
    for start, stop in search_ranges:
        for n in range(start, stop):

            #! Drop numbers with trailing zeroes
            if n % 10 == 0:
                continue

            #! Drop numbers where the leading and trailing digit have the same parity. Roughly a 50% reduction
            if (n // start) % 2 == (n % 10) % 2:
                continue

            #! Lazy evaluation of the sum digits
            s = str(n)
            total = n + int(s[::-1])
            if evens.isdisjoint(str(total)):
                amount += 1

    print(amount)


if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=10**9)
    args = parser.parse_args()

    t = time.time()

    main(limit=args.limit)

    print(time.time() - t)
