import time

L = [0, 1, 1]
x = 1
i = 2

while x < 10**999:
    x = L[i] + L[i - 1]
    L.append(x)
    i = i + 1

print(i)
