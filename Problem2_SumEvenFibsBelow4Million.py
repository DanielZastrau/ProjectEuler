"""https://projecteuler.net/problem=2"""
import time

def naive_solution(limit: int):

    x = 1
    y = 1
    total = 0
    while y < limit:
        x, y = y, x + y

        if y % 2 == 0:
            total += y
    print(total)

def standard_solution():
    even1 = 0
    even2 = 2
    sum_ = 0
    while even2 < 4 * 10**6:
        sum_ += even2

        tmp = even2
        even2 = 4*even2 + even1
        even1 = tmp
    print(sum_)

if __name__=="__main__":
    
    t = time.time()
    naive_solution(limit=10**200)
    print(time.time() - t)