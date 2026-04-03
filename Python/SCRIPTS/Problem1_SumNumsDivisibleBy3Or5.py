"""https://projecteuler.net/problem=1"""

if __name__=="__main__":
    from time import time, sleep

    def sum_nums_divisible_by(n):
        global limit

        p = (limit - 1) // n
        
        return n * (p * (p + 1)) // 2

    t = time()

    limit = 10**9

    s3 = sum_nums_divisible_by(3)
    s5 = sum_nums_divisible_by(5)
    s15 = sum_nums_divisible_by(15)
    print(s3 + s5 - s15)

    print(time() - t)