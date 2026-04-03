"""https://projecteuler.net/problem=3"""

from time import time, sleep
from Constants import primes_up_to_10to

if __name__=="__main__":
    t = time()

    Primes = primes_up_to_10to(6)
    # n = 600_851_475_143
    n = 201_799_977_802
    m = n
    max_ = 0
    sqroot = n ** 0.5

    for prime in Primes:
        if prime > sqroot:
            break
        elif n%prime == 0:
            max_ = prime
            n //= prime
            while n%prime == 0:
                n //= prime
            sqroot = n**0.5

    if n != 1:
        print(n)
    else:
        print(max_)

    print(time() - t)