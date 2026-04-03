import numpy as np
import math
import time

def term(a, b, p):
    return p ** 2 - 2 * p * a - 2 * p * b + 2 * a * b

maximum_sol = 0
maximum_p = 0
for p in range(1001):
    Sol = np.zeros(p, dtype=np.bool)
    for a in range(1, p):
        b = 1
        while term(a, b, p) > 0:
            b += 1
        if term(a, b, p) == 0:
            Sol[a] = 1
            Sol[b] = 1

    x = len(Sol[Sol != 0]) // 2
    if x > maximum_sol:
        maximum_sol = x
        maximum_p = p

print(maximum_p, maximum_sol)