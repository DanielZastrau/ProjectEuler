"""https://projecteuler.net/problem=74"""

from time import time, sleep
from math import floor, log10, factorial

class Marked:

    def __init__(self):
        self.mark = False
        self.chain = 0

if __name__=="__main__":
    t = time()

    Factorials = [ factorial(x) for x in range(10)]

    N = [ Marked() for _ in range(3 * 10**6) ]
    N[0].mark = True
    N[1].mark = True
    N[2].mark = True

    for n in range(3, 10**6):    # range(3, 10**6)    # [69, 78, 540]
        if N[n].mark is False:
            L = [n]

            while True:
                curr = L[-1]

                D = [ curr//10**i % 10 for i in range( floor( log10(curr)), -1, -1) ]
                new = sum([ Factorials[x] for x in D ])

                if N[new].mark is True:
                    length = N[new].chain
                    for i in range(1, len(L) + 1):
                        elem = L[-i]
                        if elem >= 10**6:
                            continue

                        N[elem].mark = True
                        N[elem].chain = length + i
                    break

                if new in L:
                    index = L.index(new)
                    length = len(L)
                    for i in range(index):
                        elem = L[i]
                        if elem >= 10**6:
                            continue

                        N[elem].mark = True
                        N[elem].chain = length - i
                    for i in range(index, length):
                        elem = L[i]
                        if elem >= 10**6:
                            continue

                        N[elem].mark = True
                        N[elem].chain = length - i
                    break
                else:
                    L.append(new)

    c = 0
    for obj in N:
        if obj.chain == 60:
            c+= 1

    print(c)
    print(time() - t)