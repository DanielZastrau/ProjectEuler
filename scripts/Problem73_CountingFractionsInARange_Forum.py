from math import gcd
print(sum(1 for d in range(1,12001) for n in range(d//3+1,(d+1)//2) if gcd(d,n)==1))