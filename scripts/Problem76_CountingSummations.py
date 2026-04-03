"""https://projecteuler.net/problem=76"""

if __name__=="__main__":
    from time import time, sleep
    from math import sqrt, floor, ceil

    t = time()

    limit = 100

    Partition_count = [0]*(limit+1)
    Partition_count[0] += 1
    for n in range(1, limit + 1):
        lower_limit = floor(-(sqrt(24*n + 1) - 1)/6)
        upper_limit = ceil((sqrt(24*n + 1) + 1)/6)
        # print(lower_limit, upper_limit)

        for k in range(lower_limit -1, upper_limit +1):
            if k == 0:
                continue
            # print('k | ', k)
            value = int(n - k*(3*k -1)/2)
            # print('value || ', value)
            if value < 0:
                continue
            Partition_count[n] += (-1)**(k + 1) * Partition_count[value]
    for n in range(limit+1):
        print(n, ' : ', Partition_count[n] -1)

    print(time() - t)