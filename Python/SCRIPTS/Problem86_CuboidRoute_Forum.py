from heapq import heappop, heappush
from math import gcd

# generate primitive pythagorean triples
# then the non primitive ones
# Number of options for the two smaller sides y and z within triple: zy//2 - max(zy-x-1,0)

Lgen=1000
h=[]
for u in range(2,Lgen//2):
    for v in range(1,u):
        if (u+v)%2 and gcd(u,v)==1:
            a=u*u-v*v; b=2*u*v
            for k in range(1,2+2*Lgen//min(a,b)):
                if b <= 2*a: heappush(h,[k*a,k*b])
                if a <= 2*b: heappush(h,[k*b,k*a])

SUM=0 
while SUM < 1_000_000:
    P = heappop(h)
    SUM += P[1]//2 - max(P[1]-P[0]-1,0)
print(P[0],SUM)