"""https://projecteuler.net/problem=69"""

from Constants import primes_up_to_1Million
from time import time

if __name__=="__main__":
    t = time()

    Primes = primes_up_to_1Million()

    stop = 10**6 + 1

    i = 0
    res = 1
    while res * Primes[i] < stop:
        res *= Primes[i]
        i += 1

    print(res)
    print(time() - t)