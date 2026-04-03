def cycle_length(n):
    R = []
    r = 1
    for c in range(0, n):
        x = r % n
        if x == 0:
            return 0
        elif x != 0:
            for i in range( len(R)):
                if R[i] == x: return len(R) - i
            R.append(x)
            r = x * 10
    return 0

m = 0
for n in range(1, 1000):
    l = cycle_length(n)
    if l > m:
        m = n

print(m)
