import math

def help():
    return 'prime', 'cross_sum', 'reverse', 'palindrome', 'primes_up_to', 'binary_search', 'permutations_of',\
            'product', 'sum_'

def product(L:list) -> int:

    assert isinstance(L, list), 'L must be a list'

    p = 1
    for e in L:
        p *= e

    return p

def prime(num):
    if num == 0 or num == 1:
        return False
    elif num == 2:
        return True

    for i in range(2, int(math.sqrt(num)) + 1):
        if num%i == 0:
            return False
    return True

def primes_up_to(n):
    # prime numbers less than N in O(N)
    MAX_SIZE = n + 1

    # isPrime[] : isPrime[i] is true if number is prime
    # prime[] : stores all prime number less than N
    # SPF[] that store smallest prime factor of number
    #   [for ex : smallest prime factor of '8' and '16' is '2' so we put SPF[8] = 2 , SPF[16] = 2 ]
    isprime = [True] * MAX_SIZE
    Primes = []
    SPF = [None] * (MAX_SIZE)
    
    isprime[0] = isprime[1] = False
 
    # Fill rest of the entries
    for i in range(2, n):
     
        if isprime[i] == True:
            Primes.append(i)
 
            SPF[i] = i    # A prime number is its own smallest prime factor
         
        # Remove all multiples of i*prime[j] which are not prime by making
        # isprime[i * prime[j]] = false and put smallest prime factor of i*Prime[j]
        # as prime[j] [ for exp :let i = 5 , j = 0 , prime[j] = 2 [ i*prime[j] = 10 ]
        # so smallest prime factor of '10' is '2' that is prime[j] ] this loop run only one
        # time for number which are not prime
        j = 0
        length = len(Primes)
        cur = Primes[j]
        prod = i * cur
        while prod < n \
                and cur <= SPF[i]:
         
            isprime[prod] = False
 
            # put smallest prime factor of i*prime[j]
            SPF[prod] = cur
             
            j += 1
            if j < length:
                cur = Primes[j]
                prod = i * cur
            else:
                break

    return Primes

def cross_sum(num):
    return sum([ int(elem) for elem in str(num) ])

def reverse(num):
    return int( ''.join( reversed( [ elem for elem in str(num) ] )))

def palindrome(num):
    string = str(num)

    for index in range(len(string) // 2):
        if string[index] != string[-(index + 1)]:
            return False
    return True

def binary_search(elem, L):
    if L == []:
        return False

    lo = 0
    hi = len(L)
    index = hi // 2

    exp = 1
    while 2**exp < hi:
        exp += 1
    iter_ = exp

    for iteration in range(iter_ + 1):
        if elem == L[index]:
            return True
        elif elem < L[index]:
            hi = index
            index = lo + ((hi - lo) // 2)
        elif elem > L[index]:
            lo = index
            index = lo + ((hi - lo) // 2)
    return False

def permutations_of(obj):
    if isinstance(obj, str):
        L = list(obj)
    elif isinstance(obj, list):
        L = obj
    elif isinstance(obj, int):
        L = list(str(obj))

    if len(L) == 1:
        return L

    Out = list()
    for index in range(len(L)):
        elem = L[index]
        Perms = permutations_of([ L[i] for i in range(len(L)) if i != index ])

        for permutation in Perms:
            Out.append(elem + permutation)
    return Out

def are_permutations_of_each_other(n1, n2):
    s1 = str(n1)
    s2 = str(n2)
    
    Buckets1 = [0]*10
    Buckets2 = [0]*10

    for elem in s1:
        Buckets1[int(elem)] += 1
    for elem in s2:
        Buckets2[int(elem)] += 1
    
    if Buckets1 == Buckets2:
        return True
    return False

def unique_prime_factors(n):
    Primes = primes_up_to(n+1)

    L = list()
    for prime_ in Primes:
        if n%prime_ == 0:
            L.append(prime_)
    return L

def prime_factors_up_to_1Million():
    from Constants import primes_up_to_1Million

    Primes = primes_up_to_1Million()

    Prime_factors = [ list() for _ in range(10**6 + 1) ]
    length = len(Prime_factors)
    for prime in Primes:
        i = 1
        while i*prime < length:
            Prime_factors[i*prime].append(prime)
            i += 1
    return Prime_factors

if __name__=="__main__":
    from time import time

    t = time()

    L = list()
    for i in range(10_000):
        L.append(i)
        sum(L)

    print('sum', time() - t)