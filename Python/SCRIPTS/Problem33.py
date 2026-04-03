import math

def make_list(n):
    D = []
    for digit in str(n):
        D.append(int(digit))
    return D

def common_digit(s1, s2):
    for digit in s1:
        if digit in s2:
            return digit
    return None

def multiple_of_10(n):
    if n % 10 == 0: return True
    else: return False

def largest_common_divisor(n1, n2):
    D = []
    for i in range(1, int(math.sqrt(n2)) + 1):
        if n1 % i == 0 and n2 % i == 0:
            D.append(i)

    if D == []: return None
    else: return max(D) 

N = []
for numerator in range(10,100):
    for denominator in range(numerator + 1, 100):
        if multiple_of_10(numerator) and multiple_of_10(denominator): continue
        N1 = make_list(numerator)
        N2 = make_list(denominator)
        v = common_digit(N1, N2)
        if v != None:
            N1.remove(v)
            N2.remove(v)
            if N2[0] != 0 and numerator / denominator == N1[0] / N2[0]:
                N.append((numerator, denominator))

P = [1, 1]
for numerator, denominator in N:
    P = [P[0] * numerator, P[1] * denominator]
    print(P)

x = largest_common_divisor(P[0], P[1])
while x != None:
    P = [P[0] // x, P[1] // x]
    x = largest_common_divisor(P[0], P[1])
    if x == 1: 
        print(P)
        break
print(P)