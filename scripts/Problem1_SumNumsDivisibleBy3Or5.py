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

    limit = 10**9

    s3 = sum_nums_divisible_by(3)
    s5 = sum_nums_divisible_by(5)
    s15 = sum_nums_divisible_by(15)
    print(s3 + s5 - s15)

    print(time.time() - t)