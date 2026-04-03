"""https://projecteuler.net/problem=92"""

from time import time

t = time()

sd_list = [0]*568

def sdc(n: int ) -> int:
    """The result of square digit chain"""
    while True:
        n = sum([i**2 for i in map(int, str(n))])
        if (n == 89) or (n == 1):
            return 89 if n == 89 else 1

for n in range(1, 568):
    sd_list[n] = sdc(n)

cnt_89 = 0
for n in range(1, 10_000_000):
    n_idx = sum([i**2 for i in map(int, str(n))])
    if sd_list[n_idx] == 89:
        cnt_89 += 1

print(cnt_89)
print(time() - t)