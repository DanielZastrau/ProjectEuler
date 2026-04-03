#sum of the digits of 2^1000

def power_of_2(n):
    return 2**n

def digit_sum(n):
    string = str(power_of_2(n))
    s = 0
    for i in range(len(string)):
        s = s + int(string[i])

    return s

#print(power_of_2(11))
print(digit_sum(1000))