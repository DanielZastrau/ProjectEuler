import math

def binary_of(n):
    s = ''
    x = n
    h = math.floor(math.log2(n))
    y = 2 ** h
    while h != -1:
        if y <= x:
            x -= y
            s = s + '1'
            h -= 1
            y = 2 ** h

        elif y > x:
            s = s + '0'
            h -= 1
            y = 2 ** h

    return s

def palindrome(s):
    if len(s) == 0: return True
    elif len(s) == 1: return True
    elif s[0] == s[-1]: return palindrome(s[1:-1])
    elif s[0] != s[-1]: return False

def sum_of_palindromes_less_than(n):
    P = []
    for i in range(1, n):
        if palindrome(str(i)) and palindrome(binary_of(i)):
            P.append(i)

    return sum(P)

n = 10 ** 6
#print(palindrome(99))
#print(palindrome(1100011))
print(sum_of_palindromes_less_than(n))