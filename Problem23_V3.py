import time

n = 28124
abundantNumbers = []
arr = [x for x in range(1, n)]

x = time.time()

for number in range(1, n):
    if type(number / 2) == int and (number / 2) in abundantNumbers:
        abundantNumbers.append(number)

    else:
        sum0 = 0
        for divisor in range(1, int((number/2) + 1)):
            if number % divisor == 0:
                sum0 += divisor
        if sum0 > number:
            abundantNumbers.append(number)


sum2 = 0
for number in arr:
    
    b = 0
    for i in range(len(abundantNumbers)):
        for j in range(i, len(abundantNumbers)):
            
            sum1 = abundantNumbers[i] + abundantNumbers[j]            
            if sum1 == number:
                b = 1
                break
        if b == 1:
            break
    if b == 0:
        sum2 += number

y = time.time()

print(y - x)
print(sum2)
# print (arr)
# print(abundantNumbers)