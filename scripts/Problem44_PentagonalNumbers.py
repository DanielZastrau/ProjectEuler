"""
https://projecteuler.net/problem=44
"""

import time
import math

def next_num(n):
    return n*(3*n - 1) // 2

def check_pentagonal(num):
    check1 = math.sqrt(24*num + 1)
    check2 = (check1 + 1) / 6
    if (check1%6 == 5) and (check2%1 == 0):
        return True
    
    return False

def check_nums(Penta_nums):
    cur = Penta_nums[-1]

    for num in Penta_nums[:-1]:
        sum_ = cur + num
        diff = cur - num

        if check_pentagonal(sum_) and check_pentagonal(diff):
            return cur, num

    return False, False

def main():
    Penta_nums = []
    n = 1
    while True:
        Penta_nums.append(next_num(n))
        n += 1

        P_k, P_j = check_nums(Penta_nums)
        if P_k:
            return abs(P_k - P_j)

print(main())