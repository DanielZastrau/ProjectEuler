import numpy as np

def equal(n):
    string = str(n)
    s = 0
    for digit in string:
        s += int(digit)**5

    if s == n:
        return True
    else:
        return False

def equals_up_to(n):
    A = np.zeros(n, dtype= np.bool)
    for i in range(10, n):
        if equal(i):
            A[i] = 1

    return A

def sum_of_equals(A):
    s = 0
    for n, i in enumerate(A):
        if i == 1:
            s += n

    return s

n = 10 ** 6
A = equals_up_to(n)
print(A)
print( sum_of_equals(A))