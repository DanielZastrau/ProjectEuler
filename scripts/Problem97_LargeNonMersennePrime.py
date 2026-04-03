"""https://projecteuler.net/problem=97"""

from time import time, sleep

if __name__=="__main__":
    t = time()

    const = 10**10

    p = 1
    for _ in range(7830457):    # 7830457
        p *= 2
        if p > const:
            p -= const

    s = 0
    for _ in range(28433):    # 28433
        s += p
    s += 1

    print(str(s)[-10:])
    print(time() - t)