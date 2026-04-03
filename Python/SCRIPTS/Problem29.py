A = [a for a in range(2, 101)]
B = [b for b in range(2, 101)]
C = []

for a in A:
    for b in B:
        C.append(a ** b)

D = []

for n in C:
    if n not in D:
        D.append(n)

print(len(D))