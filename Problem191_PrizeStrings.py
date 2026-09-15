"""https://projecteuler.net/problem=191
Sep 26

limit=26 with dfs 58s

Want to try something akin to the tiling problem. I.e. how many ways are there to tile a block
of 3 or more a's into a string of lenght 30. And the same for the l's."""

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

def recursion_dfs(count: int, curr_str: str, depth: int, limit: int,
                  l_count: int, consec_a_count: int) -> int:

    if l_count == 2:
        return count

    if consec_a_count == 3:
        return count

    if depth == limit:
        return count + 1

    count = recursion_dfs(count=count, curr_str=curr_str + 'o', depth=depth + 1, limit=limit,
                            l_count=l_count, consec_a_count=0)
    count = recursion_dfs(count=count, curr_str=curr_str + 'a', depth=depth + 1, limit=limit,
                            l_count=l_count, consec_a_count=consec_a_count + 1)
    count = recursion_dfs(count=count, curr_str=curr_str + 'l', depth=depth + 1, limit=limit,
                            l_count=l_count + 1, consec_a_count=0)
    
    return count

def main(limit: int):

    print(recursion_dfs(0, '', 0, limit, 0, 0))

if __name__=='__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--limit', type=int, default=30)
    args = parser.parse_args()

    t = time.time()
    main(limit=args.limit)
    print(time.time() - t)