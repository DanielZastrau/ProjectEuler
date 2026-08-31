"""https://projecteuler.net/problem=6

naive solution
limit=    100    25164150         0ms
limit=  1_000    xxxxxxxx         0ms
limit= 10**6                    143ms
limit= 10**9                166 986ms
"""
import time

def naive_solution(limit: int = 100):

    sumofsquares: int = 0
    squareofsum: int = 0

    for i in range(1, limit + 1):
        sumofsquares += i**2
        squareofsum += i

    print(squareofsum**2 - sumofsquares)

def standard_solution():

    limit = 1_000_000_000_000_000_000_000_000
    sq_sum = (limit*(limit + 1) // 2)**2
    sum_sq = (limit * (2*limit +1) * (limit +1)) / 6
    print(sq_sum - sum_sq)


if __name__=='__main__':
    t = time.time()
    naive_solution(10**9)
    print(time.time() - t)