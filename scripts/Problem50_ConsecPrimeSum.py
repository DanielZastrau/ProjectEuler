"""
https://projecteuler.net/problem=50
"""
# takes ?:??

import math
from time import sleep
from Package import prime

def main(order):
    max_ = 0
    max_c = 0

    Primes = []
    for num in range(2, 10**order):
        if prime(num):
            Primes.append(num)

    for start_index in range(len(Primes)):
        for window_length in range(1, len(Primes) - start_index):
            window = Primes[start_index: start_index + window_length]
            sum_ = sum(window)

            if sum_ > 10**order:
                break

            if not prime(sum_):
                continue

            if window_length > max_c:
                max_ = sum_
                max_c = window_length

    return max_, max_c

print(main(6))
