"""https://projecteuler.net/problem=76"""

from time import time, sleep

if __name__=="__main__":
    t = time()

    limit = 100
    ways = [0 for _ in range(limit + 1)]
    ways[0] = 1

    for i in range(1, limit):
        for j in range(i, limit + 1):
            ways[j] += ways[j - i]
    print(ways[100])

    print(time() - t)