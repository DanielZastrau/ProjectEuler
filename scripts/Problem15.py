import math

def bin(k, n):
    number1 = 1
    for integer in range(n, 0, -1):
        number1 = number1 * integer
    #print(number1)

    number2 = 1
    for integer in range(k, 0, -1):
        number2 = number2 * integer
    #print(number2)

    number3 = 1
    for integer in range(n - k, 0, -1):
        number3 = number3 * integer
    #print(number3)

    return int(number1 / (number2 * number3))

print(bin(1, 2))
print(bin(2, 4))
print(bin(3, 6))
print(bin(4, 8))
print(bin(5, 10))
print(bin(6, 12))
print(bin(7, 14))
print(bin(8, 16))
print(bin(9, 18))
print(bin(10, 20))
print(bin(11, 22))
print(bin(12, 24))
print(bin(13, 26))
print(bin(14, 28))
print(bin(15, 30))
print(bin(16, 32))
print(bin(17, 34))
print(bin(18, 36))
print(bin(19, 38))
print(bin(20, 40))
