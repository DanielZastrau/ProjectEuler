import math

def digitsum(n: int):
    return sum([n // 10**power % 10 for power in range(int(math.log10(n)) + 1)])