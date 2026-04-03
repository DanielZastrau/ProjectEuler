import math

proper_Divisors = [[], [1]]

for n in range(2, 10000):
    D = [1]
    for d in range(2, int(math.sqrt(n)) + 1):
        if n % d == 0:
            D.append(d)
            y = int(n / d)
            if y != d:
                D.append(y)

    proper_Divisors.append(D)

Sum_pD = []
for number in proper_Divisors:
    sum_ = 0
    for divisor in number:
        sum_ += divisor
    
    Sum_pD.append(sum_)


A_numbers = []
for a in range(len(Sum_pD)):
    b = Sum_pD[a]
    if b >= 10000:
        continue
    
    number = Sum_pD[b]

    if number == a and a != b:
        if a < b: tupel = (a, b)
        else: tupel = (b, a)

        if not tupel in A_numbers: A_numbers.append(tupel)

sum_AN = 0
for tupel in A_numbers:
    sum_AN += tupel[0] + tupel[1]

print(sum_AN)