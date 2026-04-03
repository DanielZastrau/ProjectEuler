"""https://projecteuler.net/problem=719"""

from time import time, sleep

def generate_windows(Curr, L):
    start = L[0]
    for i in range(1, len(L)):
        end = L[i]
        if end == L[-1]:
            yield Curr + [[start, end]]
        else:
            generate_windows(Curr + [[start, end]], [ elem for elem in L if elem >= end])

def number_splitting(sq, n, windows):
    for window in windows:
        L = list()
        for i in window:
            L.append( int( str(sq)[i[0]: i[1]]))
        if sum(L) == n:
            return True
    return False

if __name__=="__main__":
    t = time()

    Squares = list()
    for i in range(0, 10**6 + 1):
        Squares.append(i**2)

    for square in Squares[:10]:
        L = list(str(square))
        print(L)

    print(time() - t)