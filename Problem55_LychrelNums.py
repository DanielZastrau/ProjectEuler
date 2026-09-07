"""
https://projecteuler.net/problem=55
"""

def reverse(num):
    return int( ''.join( reversed( [ elem for elem in str(num) ] )))

def palindrome(num):
    string = str(num)

    for index in range(len(string) // 2):
        if string[index] != string[-(index + 1)]:
            return False
    return True

def lychrel(num):
    for iteration in range(50):
        num = num + reverse(num)

        if palindrome(num):
            return False
    return True

def main():
    c = 0
    for num in range(10**4):
        if lychrel(num):
            c += 1
    return c

print(main())