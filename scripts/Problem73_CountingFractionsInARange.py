"""https://projecteuler.net/problem=73"""

from time import time, sleep
from Constants import primes_up_to_10to
from Package import prime_factors_up_to_1Million
from math import ceil

class Fraction:

    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator
        self.reduced = self.reduced()

    def reduced(self):
        global Primes

        for prime in Primes:
            if prime > self.num or prime > self.den:
                break
            if self.num % prime and self.den % prime:
                return False
        return True


if __name__=="__main__":
    t = time()

    Primes = primes_up_to_10to(6)
    Primes = [ prime for prime in Primes if prime < 12_000 ]

    Candidates = [ set() for _ in range(12_001) ]
    for prime in Primes:
        L = set()
        i = 1
        check = i*prime
        while check < 12_001:
            Candidates[check].update(L)
            L.add(check)

            i += 1
            check = i*prime

    Coprimes = []
    for i, e in enumerate(Candidates):
        # if i != 10:
            # continue
        if i == 0 or i == 1:
            Coprimes.append([])
            continue

        # print(e)

        x = ceil(i/3 + 0.000000001)
        y = ceil(i/2)
        L = list(range(x, y))
        # print(L)
        for candidate in e:
            if x <= candidate < y:
                L.remove(candidate)

        Coprimes.append(L)
        # if L != list():
            # print(L[0], L[-1], i)
            # sleep(2)

    c = 0
    for elem in Coprimes:
        c += len(elem)

    print(c)
    print(time() - t)