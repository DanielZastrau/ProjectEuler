"""https://projecteuler.net/problem=85"""

if __name__=="__main__":
    from time import time, sleep
    from math import ceil

    t = time()

    closest = 0
    area = 0

    for i in range(1, 100):
        for j in range(i, 100):
            factor1 = i*(i+1)//2
            factor2 = j*(j+1)//2
            s = factor1 * factor2

            if abs(s - 2_000_000) < abs(closest - 2_000_000):
                closest = s
                area = i * j
    print(closest)
    print(area)

    print(time() -t)