"""https://projecteuler.net/problem=179
Aug 26

771 019    283.170    wrong
771 018    226.106    wrong
986 262    212.627    right,  but takes too long by a factor of 4
986 262    175.932    right,  but takes too long by a factor of 3    instead of storing lists of the actual divisors I just store the count    lists.append > int += 1
986 262    114.977    right,  but takes too long by a factor of 2    the inner for / while loop got replaced by an itertools.count
986 262     11.335    right,                                         took out the print
"""

import argparse
import sys
import os
import time
import math 
import itertools as it

def main(searchspace: int = 10**7):

    #! index is offset by 1, i.e., number 1 is at index 0
    divisors = [1] + [2 for _ in range(2, searchspace + 1)]

    for n in range(2, searchspace // 2 + 10 + 2):
        for nn in it.count(start=2*n, step=n):
            if nn > searchspace:
                break

            divisors[nn - 1] += 1

    amount = 0
    for i in range(len(divisors) - 1):
        if divisors[i] == divisors[i + 1]:
            amount += 1

    print(amount)

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--searchspace', type=int, default=10**7)
    args = parser.parse_args()

    t = time.time()
    main(searchspace = args.searchspace)
    print(time.time() - t)