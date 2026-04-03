from math import log as ln
from time import time

def ecart(x):    # signed step between x and IN, set of integers
    return(x-int(x+0.5)) 

n = 123
eps = ln(1+1/n) / ln(2)
f = lambda q: (ln(n+1) + q*ln(10)) / ln(2)

#(N is valid) iff (2^N=123... tail of q digits)  iff (0<ecart(f(q))<eps)
ef25 = ecart(f(25))    # 1st valid is q=25,N=90
t = ln(10)/ln(2)    # slope of function f

d87 = ecart(87*t)
d59 = -ecart(59*t)
d146 = d87-d59
print(d87,d59,d146)

def suivant(i, x, N):
    if x < eps-d87:
        return(i+1, x+d87, N+289)
    if x < d59:
        return(i+1, x+d146, N+485)
    return(i+1, x-d59, N+196)

start=time()

i, x, N = 1, ef25, 90
for _ in range(678909):
	#print(i,x,N);
	i,x,N=suivant(i,x,N)
    
print(i,N, ' in ' ,str(int(1000*(time()-start))),' ms')