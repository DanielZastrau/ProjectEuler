"""https://projecteuler.net/problem=9
"""

import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op

from typing import Iterator

import Commons

def main():
    PT: list[tuple[int, ...]] = []
    PT1000: list[tuple[int, ...]] = []

    for integer1 in range(1, 1000):

        if integer1 < 1000 - integer1:
            limit1 = integer1
        else:
            limit1 = 1000 - integer1

        for integer2 in range(1, limit1 + 1):

            if integer2 < 1000 - integer1 - integer2:
                limit2 = integer2
            else:
                limit2 = 1000 - integer1 - integer2

            for integer3 in range(1, limit2 + 1):

                if ((integer3**2) + (integer2**2)) == (integer1**2):
                    PT.append((integer3, integer2, integer1))

    for triplet in PT:
        if triplet[0] + triplet[1] + triplet[2] == 1000:
            PT1000.append(triplet)

    triplet = PT1000[0]
    print(((triplet[0]**2) + (triplet[1]**2)) == (triplet[2]**2))
    print(triplet[0] + triplet[1] + triplet[2])
    print(triplet)

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    t = time.time()
    main()
    print(time.time() - t)