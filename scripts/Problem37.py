import math

def is_prime(n):
    if n == 1: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def trunc_left(n):
    if len(str(n)) == 1: return is_prime(n)
    elif is_prime(n):
        return trunc_left(int(str(n)[1:]))
    else:
        return False

def trunc_right(n):
    if len(str(n)) == 1: return is_prime(n)
    elif is_prime(n):
        return trunc_right(int(str(n)[:-1]))
    else:
        return False

n = 10
P = []
while len(P) < 11:
    n += 1
    if is_prime(n):
        if trunc_left(n) and trunc_right(n):
            P = P + [n]

print(sum(P))