def factorial(n):

    number = 1
    for integer in range(1, n + 1):
        number *= integer

    return number

string = str(factorial(100))

number = 0
for letter_index in range(len(string)):
    number += int(string[letter_index])
    
print(number)