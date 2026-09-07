"""https://projecteuler.net/problem=78"""

if __name__=="__main__":
    from time import time, sleep
    from math import sqrt, floor, ceil

    t = time()

    curr_10 = 0
    Partition_count = [1]

    n = 1
    while True:
        Partition_count.append(0)

        lower_limit = floor(-(sqrt(24*n + 1) - 1)/6)
        upper_limit = ceil((sqrt(24*n + 1) + 1)/6)

        for k in range(lower_limit -1, upper_limit +1):
            if k == 0:
                continue
            value = int(n - k*(3*k -1)/2)
            if value < 0:
                continue
            Partition_count[n] += (-1)**((k + 1)%2) * Partition_count[value]

        if Partition_count[-1] % 10**6 == 0:
            print(n)
            break

        n += 1

    print(time() - t)