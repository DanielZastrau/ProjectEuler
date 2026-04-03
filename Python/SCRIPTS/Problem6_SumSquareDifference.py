"""https://projecteuler.net/problem=6"""

if __name__=="__main__":
    from time import time

    t = time()

    limit = 1_000_000_000_000_000_000_000_000
    sq_sum = (limit*(limit + 1) // 2)**2
    sum_sq = (limit * (2*limit +1) * (limit +1)) / 6
    print(sq_sum - sum_sq)

    print(time() - t)