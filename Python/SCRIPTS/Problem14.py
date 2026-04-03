import time

def inner_collatz(number):
    if number % 2 == 0: return number / 2
    elif number % 2 == 1: return (number * 3) + 1

def outer_collatz(number):
    sequence_length = 1
    while not number == 1:
        number = int(inner_collatz(number))
        if number < len(SL): return sequence_length + SL[number]
        sequence_length = sequence_length + 1
    return sequence_length

max_sl = float('-inf')
max_int = 0
SL = [0,1]
for integer in range(2,1000000):
    sl = outer_collatz(integer)
    SL.append(sl)
    if sl > max_sl: 
        max_sl = sl
        max_int = integer

print(max_int)