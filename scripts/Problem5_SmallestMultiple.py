"""https://projecteuler.net/problem=5"""

if __name__=="__main__":
    from time import time, sleep
    from Constants import primes_up_to_10to
    from math import log10, floor

    t = time()

    limit = 10**6
    Primes = primes_up_to_10to(int(log10(limit)))
    res = 1
    for prime in Primes:
        res *= prime**(floor(log10(limit) / log10(prime)))
        
    print(time() - t)
    print(res)