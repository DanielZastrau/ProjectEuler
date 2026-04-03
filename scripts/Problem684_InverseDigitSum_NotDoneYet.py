"""https://projecteuler.net/problem=684"""

from Constants import fibs_up_to_10to21
from time import time, sleep

def s(n):
    global Mod

    rest = n

    curr_pow = 1
    out = 0
    while rest > 9:
        out += 9*curr_pow
        out %= Mod

        curr_pow *= 10
        curr_pow %= Mod

        rest -= 9

    out += rest*curr_pow
    out %= Mod

    return out

def S(limit):
    global Mod
    
    i = limit // 9
    j = limit % 9
    # print(f'limit, i, j | {limit}, {i}, {j} ')

    num = 5

    a = i // 10
    b = i % 10
    for _ in range(a):
        num *= 10**10 % Mod
    num *= 10**b % Mod
    # print(f'limit, num | {limit}, {num} ')

    # print(f'limit, i, i-1 | {limit}, {i}, {i-1} ')
    for exp in range(1, i - 1):
        # print('exp: ', exp)
        a = (i-exp) // 10
        b = (i-exp) % 10
        # print('a, b: ', a, b)
        n = 9
        for _ in range(a):
            n *= 10**10 % Mod
        n *= 10**b % Mod

        num += n
    # print(f'limit, num | {limit}, {num} ')
    
    num += 94
    num %= Mod
    # print(f'limit, num | {limit}, {num} ')

    res = num - i*9
    res %= Mod

    for n in range(limit, limit - j, -1):
        num = s(n)

        res += num
        res %= Mod

    return res

if __name__=="__main__":
    t = time()

    Fibs = fibs_up_to_10to21()
    # limit = Fibs[90]        # 2 880 067 194 370 816 120

    Mod = 1_000_000_007

    sum_ = 0
    for i in range(90, 1, -1):
        print(Fibs[i])
        sum_ += S(Fibs[i])
        sum_ %= Mod

    print(sum_)
    print(time() - t, '\n')