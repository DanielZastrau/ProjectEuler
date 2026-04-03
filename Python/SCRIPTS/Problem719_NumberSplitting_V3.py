"""https://projecteuler.net/problem=719"""

from time import time, sleep
from math import ceil, log

def generate_windows(Curr, L, length, windows):
    start = L[0]
    for i in range(1, len(L)):
        end = L[i]
        if end - start > length:
            break
        elif end == L[-1]:
            windows.append(Curr + [[start, end]])
        else:
            generate_windows(Curr + [[start, end]], [ elem for elem in L if elem >= end], length, windows)

def number_splitting(sq, n, windows):
    string = str(sq)
    for window in windows:
        L = list()
        for i in window:
            L.append( int( string[i[0]: i[1]]))
        if sum(L) == n:
            return True
    return False

def recursive(string, i, length, curr):
    if string == str():
        if sum(curr) == i:
            return 0

    for j in range(1, len(string) + 1):
        if j > length:
            break
        res = recursive(string[j:], i, length, curr + [int(string[:j])])

        if res == 0:
            return 0

if __name__=="__main__":
    t = time()

    s = 0
    for i in range(1, 10**6 + 1):
        if time() - t > 60:
            print(i)
            break

        sq = i**2
        res = recursive(str(sq), i, len(str(i)), [])
        
        if res == 0:
            s += sq

    print(s)
    print(time() - t)