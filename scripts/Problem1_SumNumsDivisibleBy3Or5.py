"""https://projecteuler.net/problem=1"""
import argparse
import math
import itertools as it
import time

def sum_nums_divisible_by(n: int):

    p = (limit - 1) // n
    
    return n * (p * (p + 1)) // 2


if __name__=="__main__":

    t = time.time()
    print(sum([i for i in range(1, 10**3) if i % 3 == 0 or i % 5 == 0]))
    print(time.time() - t)