"""https://projecteuler.net/problem=88"""

if __name__=="__main__":
    from time import time, sleep
    from math import prod, sqrt, ceil

    def factorization(n, curr):
        if n == 1:
            return []
        elif n < curr:
            return []
        else:
            Factorizations = list()
            Factorizations.append([n])
            for m in range(curr, ceil(sqrt(n)) +1):
                if n%m == 0:
                    tmp = factorization(n//m, m)
                    for entry in tmp:
                        Factorizations.append([m] + entry)
            return Factorizations

    def sum_(entry, depth):
        return depth - len(entry) + sum(entry)

    t = time()

    lower_limit = 2
    upper_limit = 12000

    F = list()
    F.append([0]); F.append([1])
    for n in range(2, 24_001):
        F.append(factorization(n, 2))

    s = 0
    for depth in range(lower_limit, upper_limit +1):
        for n in range(depth, 2*depth +1):
            b = 0

            Factorizations = F[n]
            for entry in Factorizations:
                if sum_(entry, depth) == prod(entry) == n:
                    s += n

                    b = 1
                    break

            if b:
                break
    print(s)

    print(time() - t)