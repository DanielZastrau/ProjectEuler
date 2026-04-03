import numpy as np

n = 1001
M = np.zeros((n,n), dtype=int)
i = (n - 1) // 2
j = (n - 1) // 2
M[i][j] = 1
x = 2

b1 = True
b2 = True
l = 1

for c0 in range(n-1):
    for c1 in range(2):
        for c2 in range(l):
            if b1 and b2: # taking steps to the right
                j += 1

            if b1 and not b2: # taking steps down
                i += 1

            if not b1 and b2: # taking steps to the left
                j -= 1

            if not b1 and not b2: # taking steps up
                i -= 1

            M[i][j] = x
            x += 1

        if b1 and b2: # taking steps to the right
            b2 = False

        elif b1 and not b2: # taking steps down
            b1 = False
            b2 = True

        elif not b1 and b2: # taking steps to the left
            b1 = False
            b2 = False

        elif not b1 and not b2: # taking steps up
            b1 = True
            b2 = True
    l += 1
    
for c in range(l - 1):
    j += 1
    M[i][j] = x
    x += 1

s = 0
for i in range(n):
    s += M[i][i]
    if i != n - 1 - i: 
        s += M[i][n - 1 - i]
print(s)

for row in M:
    print(row)