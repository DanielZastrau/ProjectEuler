"""https://projecteuler.net/problem=1
Sometime 2021

limit=        1 000                    233 168          0.2ms
limit=    1 000 000            233 333 166 668        117.3ms
limit=1 000 000 000    233 333 333 166 666 668    121 295.0ms
"""
import argparse
import math
import itertools as it
import time

if __name__=="__main__":

    t = time.time()
    print(sum([i for i in range(1, 10**9) if i % 3 == 0 or i % 5 == 0]))
    print(time.time() - t)