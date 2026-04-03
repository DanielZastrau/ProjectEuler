"""https://projecteuler.net/problem=72"""

from time import time, sleep
from Constants import primes_up_to_1Million

def phi(i, e):
    num = i
    for prime in e:
        num //= prime
    
    res = 1
    for prime in e:
        res *= prime - 1

    if num == 1:
        return res
    else:
        return num * res

if __name__=="__main__":
    t = time()

    d = 10**6

    Primes = primes_up_to_1Million()

    Prime_factors = [ list() for _ in range(d + 1) ]
    for prime in Primes:
        i = 1
        while i*prime < d + 1:
            Prime_factors[i*prime].append(prime)
            i += 1

    s = 0
    for i, e in enumerate(Prime_factors):
        if i == 0 or i == 1:
            continue
        else:
            s += phi(i, e)
    print(s)

    print(time() - t)