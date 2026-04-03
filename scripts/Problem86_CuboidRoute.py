"""https://projecteuler.net/problem=86"""

if __name__=="__main__":
    from time import time, sleep
    from math import sqrt, isclose, gcd

    t = time()

    limit = 1_818

    Pythagorean_triples = set()

    for m in range(1, limit):
        for n in range(1, m):
            if m%2==0 or n%2==0:
                if gcd(m, n) == 1:
                    a = m**2 - n**2
                    b = 2*m*n
                    c = m**2 + n**2
                    if a + b < limit*3:
                        Pythagorean_triples.add((a, b, c))

    Non_primitives = set()
    for a, b, c in Pythagorean_triples:
        i = 2
        d = a + b
        while i * d < limit*3:
            Non_primitives.add((i*a, i*b, i*c))
            i += 1
    Pythagorean_triples.update(Non_primitives)

    Cuboids = set()
    for d, e, f in Pythagorean_triples:
        if d < limit:
            a = d
            for c in range(1, min(e//2 +1, limit)):
                b = e - c
                if b < limit:
                    sq1 = (max(a, b), min(a, b))
                    sq2 = (max(b, c), min(b, c))
                    sq3 = (max(a, c), min(a, c))
                    cuboid = [sq1, sq2, sq3]; cuboid.sort(reverse=True, key=lambda x: x[0])
                    cuboid = tuple(cuboid)
                    Cuboids.add(cuboid)

        if e < limit:
            b = e
            for c in range(1, min(d//2 +1, limit)):
                a = d - c
                if a < limit:
                    sq1 = (max(a, b), min(a, b))
                    sq2 = (max(b, c), min(b, c))
                    sq3 = (max(a, c), min(a, c))
                    cuboid = [sq1, sq2, sq3]; cuboid.sort(reverse=True, key=lambda x: x[0])
                    cuboid = tuple(cuboid)
                    Cuboids.add(cuboid)

    tmp = set()
    for cuboid in Cuboids:
        a, b = cuboid[0]
        c = cuboid[1][1]

        line1 = a**2 + (b + c)**2
        line2 = (a + c)**2 + b**2
        min_ = min(line1, line2)

        if sqrt(min_)%1 == 0:
            tmp.add(cuboid)
    Cuboids = tmp
    print(len(Cuboids))

    print(time() - t)