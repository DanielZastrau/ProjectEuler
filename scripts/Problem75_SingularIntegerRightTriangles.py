"""https://projecteuler.net/problem=75"""

from time import time, sleep
from Constants import primes_up_to_10to
from math import gcd

if __name__=="__main__":
    t = time()

    limit = int(1.5 * 10**6 + 1)

    L = [ 0 for _ in range(limit) ]
    Pythagorean_triples = set()

    for m in range(1, 2_000):
        for n in range(1, m):
            if m%2==0 or n%2==0:
                if gcd(m, n) == 1:
                    a = m**2 - n**2
                    b = 2*m*n
                    c = m**2 + n**2
                    if a + b + c < limit:
                        Pythagorean_triples.add((a, b, c))

    Non_primitives = set()
    for a, b, c in Pythagorean_triples:
        i = 2
        d = a + b + c
        while i * d < limit:
            Non_primitives.add((i*a, i*b, i*c))
            i += 1
    Pythagorean_triples.update(Non_primitives)

    for a, b, c in Pythagorean_triples:
        L[a + b + c] += 1
    L = list(filter(lambda x: x==1, L))
    print(len(L))


    print(time() - t)