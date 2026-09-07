"""https://projecteuler.net/problem=124
Aug 26

21 417    0.087s    right
"""

import argparse
import sys
import os
import time
import math 
import itertools as it

def main(searchspace: int = 10**5, kth: int = 0):

    # offset by one, value 1 is at index 0
    distinct_prime_factors = [[1] for _ in range(1, searchspace + 1)]

    for n in range(2, searchspace + 1):
        if len(distinct_prime_factors[n - 1]) != 1:
            continue

        distinct_prime_factors[n - 1].append(n)
        for nn in it.count(start=2*n, step=n):
            if nn > searchspace:
                break

            distinct_prime_factors[nn - 1].append(n)

    sorted_zipped = sorted(zip(range(1, searchspace + 1), map(lambda x: math.prod(x) ,distinct_prime_factors)), key=lambda x: x[1])
    print(sorted_zipped[kth - 1])
            


if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--searchspace', type=int, default=10**5)
    parser.add_argument('--kth', type=int, default=0)
    args = parser.parse_args()

    t = time.time()

    main(searchspace=args.searchspace, kth=args.kth)

    print(time.time() - t)