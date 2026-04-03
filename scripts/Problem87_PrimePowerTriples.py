"""https://projecteuler.net/problem=87"""

if __name__=="__main__":
    from time import time, sleep
    from Constants import primes_up_to_10to

    t = time()

    Primes = primes_up_to_10to(4)
    limit = 50 * 10**6 + 1

    Squares = list(filter(lambda x: x < limit, map(lambda x: x**2, Primes)))
    Cubes = list(filter(lambda x: x < limit, map(lambda x: x**3, Primes)))
    Tessarects = list(filter(lambda x: x < limit, map(lambda x: x**4, Primes)))

    S = set()
    for prime_sq in Squares:
        for prime_cu in Cubes:
            for prime_tess in Tessarects:
                e = prime_sq + prime_cu + prime_tess
                if e < limit:
                    S.add(e)
    print(len(S))

    print(time() - t)