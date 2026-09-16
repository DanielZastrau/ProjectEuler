"""https://projecteuler.net/problem=191
Sep 26

limit=26 with dfs 45s
limit=30 with dfs 823s

what would I tag this problem as?
  -  combinatorics"""

import argparse
import time
import math
import itertools as it
import functools as ft
import operator as op
import fractions as fr
import heapq

from typing import Iterator

import commons

@ft.cache
def recursion_dfs(rest: int, l_count: int, consec_a_count: int) -> int:
    global count

    if l_count == 2 or consec_a_count == 3:
        return 0

    if rest == 0:
        return 1

    return (
        recursion_dfs(rest=rest - 1, l_count=l_count, consec_a_count=0) +
        recursion_dfs(rest=rest - 1, l_count=l_count, consec_a_count=consec_a_count + 1) +
        recursion_dfs(rest=rest - 1, l_count=l_count + 1, consec_a_count=0)
    )

def main(limit: int):

    # total=func(30,0,0)
    # print ("Total: %d"%total)

    global count

    print(recursion_dfs(limit, 0, 0))
    print(recursion_dfs.cache_info())

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=30)
    args = parser.parse_args()

    t = time.time()
    main(limit=args.limit)
    print(time.time() - t)