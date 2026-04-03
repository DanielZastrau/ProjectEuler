"""
https://projecteuler.net/problem=46
"""

import math

def prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num%i == 0: return False

    return True

def conjecture(num):
    Primes = []
    for i in range(2, num):
        if prime(i):
            Primes.append(i)
    # print(f'{num}: {Primes}')
    
    for prime_ in Primes:
        # print(f'num - prime_: {num - prime_}')
        # print(f'(num - prime_) / 2: {(num - prime_) / 2}')
        if math.sqrt((num - prime_) / 2)%1 == 0:
            return True
    
    return False

def main():
    next_ = 3
    
    while True:
        next_ = next_ + 2
        if not prime(next_) and not conjecture(next_):
            return next_

print(main())
