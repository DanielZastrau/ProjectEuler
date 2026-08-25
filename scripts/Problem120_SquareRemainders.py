"""https://projecteuler.net/problem=120
Aug 26

333 082 500    3.812s    correct
"""

import argparse
import time
import math
import itertools as it
import operator as op
import functools as ft
from typing import Iterator

def find_chain(a: int, modulo: int) -> tuple[int, list[int]]:

    chain: list[int] = []

    n = a % modulo
    chain.append(n)
    while True:
        n = (n * a) % modulo

        if n in chain:
            return len(chain), chain

        chain.append(n)

def main():

    s = 0
    for a in range(3, 1001):

        a_minus_one = a - 1
        a_plus_one = a + 1
        a_sq = a**2

        l1, chain1 = find_chain(a_minus_one, a_sq)
        l2, chain2 = find_chain(a_plus_one, a_sq)

        #! smallest common multiple
        smc = (l1 * l2) // math.gcd(l1, l2)

        maximum = 0
        for _, e1, e2 in zip(range(smc), it.cycle(chain1), it.cycle(chain2)):

            v = (e1 + e2) % a_sq

            if v > maximum:
                maximum = v
        s += maximum

    print(s)


if __name__=='__main__':

    t = time.time()
    main()
    print(time.time() - t)