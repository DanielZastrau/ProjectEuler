"""https://projecteuler.net/problem=2"""

if __name__=="__main__":
    from time import time, sleep
    
    t = time()

    even1 = 0
    even2 = 2
    sum_ = 0
    while even2 < 4 * 10**6:
        sum_ += even2

        tmp = even2
        even2 = 4*even2 + even1
        even1 = tmp
    print(sum_)

    print(time() - t)