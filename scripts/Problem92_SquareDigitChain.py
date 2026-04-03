"""https://projecteuler.net/problem=92"""

from time import time, sleep
from math import ceil, log
from Package import binary_search

if __name__=="__main__":
    t = time()

    L89 = list()    # numbers arriving at 89
    L1 = list()    # numbers arriving at 1

    c = 0
    for n in range(1, 10**7):
        next_ = n
        while True:
            tmp = 0
            for elem in str(next_):
                tmp += int(elem)**2
            next_ = tmp

            if next_ == 1:
                L1.append(n)
                break
            elif next_ == 89:
                c += 1
                L89.append(n)
                break
            elif binary_search(next_, L1):
                L1.append(n)
                break
            elif binary_search(next_, L89):
                L89.append(n)
                c += 1
                break
    print(c)

    print(time() - t)