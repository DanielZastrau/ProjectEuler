"""
https://projecteuler.net/problem=62
"""

"""
taken from the forum
"""

from Constants import cubes_up_to_1Trillion
from time import time, sleep

def fingerprint(num):
    string = str(num)
    Buckets = [0]*10
    for elem in string:
        Buckets[int(elem)] += 1
    return str(Buckets)


if __name__=="__main__":
    t = time()

    Cubes = cubes_up_to_1Trillion()
    d = dict()

    for cube in Cubes:
        fp = fingerprint(cube)

        if fp in d.keys():
            d[fp][0] += 1
        else:
            d[fp] = [1, cube]

    for key, value in d.items():
        if value[0] == 5:
            print(value[1])
    print(time() - t)