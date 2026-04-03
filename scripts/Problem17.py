def count1(n):
    return Count[str(n)]

def count2(n):
    return Count[str(n)[0] + '0'] + Count[str(n)[1]]

def count3(n):
    return Count[str(n)[0]] + Count['100']

def inner_letter_count(n):
    print(n)
    if 0 <= n and n < 21: return count1(n)

    elif 20 < n and n < 100: 
        if str(n)[1:] == '0': return count1(n)
        else: return count2(n)

    elif 99 < n and n < 1000:
        if str(n)[1:] == '00': return count3(n)
        elif str(n)[2:] == '0': return count3(n) + 3 + count1(int(str(n)[1:]))
        else: 
            x = int(str(n)[1:])
            #print(x)

            if 0 < x and x < 21: return count3(n) + 3 + count1(x)
            elif 20 < x and x < 100: return count3(n) + 3 + count2(x)

    elif n == 1000: return Count['1'] + Count['1000']

def outer_letter_count(u):
    count = 0
    for n in range(1, u + 1):
        count = count + inner_letter_count(n)
    
    return count

Count = {'1': 3, '2': 3, '3': 5, '4': 4, '5': 4, '6': 3, '7': 5, '8': 5, '9': 4, '10': 3,
        '11': 6, '12': 6, '13': 8, '14': 8, '15': 7, '16': 7, '17': 9, '18': 8, '19': 8, '20': 6,
        '30': 6, '40': 5, '50': 5, '60': 5, '70': 7, '80': 6, '90': 6, '100': 7, '1000' : 8,
    }

# for u in range(1, 100):
#     print(str(u)+ ': ' + str(inner_letter_count(u)) + ',   ' + str(outer_letter_count(u)))

print(outer_letter_count(1000))
# print(outer_letter_count(5))
# print(inner_letter_count(342))
# print(inner_letter_count(115))