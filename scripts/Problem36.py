import math

def binary_of(n: int):
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

def palindrome(s: str) -> bool:
    return s == s[::-1]

def sum_of_palindromes_less_than(n: int):
    palindromes: list[int] = []
    for i in range(1, n):
        if palindrome(str(i)) and palindrome(binary_of(i)):
            palindromes.append(i)

    return sum(palindromes)

n = 10 ** 6
#print(palindrome(99))
#print(palindrome(1100011))
print(sum_of_palindromes_less_than(n))