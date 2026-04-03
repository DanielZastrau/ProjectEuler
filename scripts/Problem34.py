def factorial_inner(n):
    if n == 0: return 1
    if n == 1: return 1
    return factorial_inner(n - 1) * n

def factorial_outer():
    d = {}
    for n in range(0, 10):
        d[n] = factorial_inner(n)
    return d

def make_list(n):
    return [int(x) for x in str(n)]

def sum_of_digit_fact(n, d):
    return sum([d[x] for x in make_list(n)])

N = []
d = factorial_outer()
for n in range(10, 10 ** 5):
    if n == sum_of_digit_fact(n, d): N.append(n)

print(sum(N))