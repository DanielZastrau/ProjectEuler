"""https://projecteuler.net
Aug 26
"""

import argparse
import time
import math
import itertools as it
import operator as op
import functools as ft
from typing import Iterator

import Commons

def main(limit: int):

    digitpowersum_n: list[int] = []
    for digitsum in range(2, 99999):

        for power in range(1, 10):

            if digitsum**power < 10:
                continue

            if Commons.digitsum(digitsum**power) == digitsum:
                out = [digitsum, digitsum**power, time.time() - t]
                names = ['digitsum', 'n', 'elapsed time']
                print(*list(zip(names, out)))
                print()

                digitpowersum_n.append(digitsum**power)

        if len(digitpowersum_n) == 2*limit:
            break

    print(sorted(digitpowersum_n))
    print(sorted(digitpowersum_n)[29])

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=30)
    args = parser.parse_args()

    t = time.time()
    main(limit=args.limit)
    print(time.time() - t)