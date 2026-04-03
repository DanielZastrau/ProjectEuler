"""
https://projecteuler.net/problem=62
"""

from Constants import cubes_up_to_1Trillion
from time import sleep, time

def are_permutations(num, cube):
    L1 = sorted(list(str(num)))
    L2 = sorted(list(str(cube)))
    return L1 == L2

def backtracking(Cubes, Curr):
    if Curr:
        if len(Curr) == 5:
            bool_ = 1
            for cube in Cubes:
                if cube not in Curr:
                    bool__ = 1

                    for num in Curr:
                        if not are_permutations(num, cube):
                            bool__ = 0
                    if bool__:
                        bool_ = 0

            if bool_:
                return min(Curr)

        elif len(Curr) < 5:
            for cube in Cubes:
                if cube not in Curr:
                    bool_ = 1

                    for num in Curr:
                        if not are_permutations(num, cube):
                            bool_ = 0
                    if bool_:
                        res = backtracking(Cubes, Curr + [cube])

                        if res is not None:
                            return res

    else:
        for cube in Cubes:
            res = backtracking(Cubes, [cube])

            if res is not None:
                return res

if __name__ == "__main__":
    t = time()
    Cubes = cubes_up_to_1Trillion()

    Cubes12 = list()

    for cube in Cubes:
        if 10**11 <= cube:
            Cubes12.append(cube)

    print(backtracking(Cubes12, []))
    print(time() - t)