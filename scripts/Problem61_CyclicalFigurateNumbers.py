"""
https://projecteuler.net/problem=61
"""

from time import sleep

def backtracking(Nums, Keys, Curr):

    if len(Curr) == 6 and Curr[0][:2] == Curr[-1][-2:]:
        print(Curr)
        print(Keys)
        print(sum([ int(elem) for elem in Curr ]))
        sleep(1)

    if Curr:
        for key, value in Nums.items():
            if key not in Keys:
                for num in value:
                    if Curr[-1][-2:] == num[:2]:
                        backtracking(Nums, Keys + [key], Curr + [num])

    else:
        for num3 in Nums['3']:
            backtracking(Nums, ['3'], [num3])

def generate_nums(order):
    n, num = 1, 0
    Out = list()
    while num < 10**4:

        if order == 3:
            num = tr_num(n)
        elif order == 4:
            num = sq_num(n)
        elif order == 5:
            num = pent_num(n)
        elif order == 6:
            num = hex_num(n)
        elif order == 7:
            num = hept_num(n)
        else:
            num = oct_num(n)

        if num > 999:
            Out.append(str(num))

        n += 1

    return Out[:-1]

def tr_num(n):
    return (n*(n+1)) // 2

def sq_num(n):
    return n**2

def pent_num(n):
    return (n*(3*n - 1)) // 2

def hex_num(n):
    return n*(2*n - 1)

def hept_num(n):
    return n*(5*n - 3) // 2

def oct_num(n):
    return n*(3*n - 2)

if __name__=="__main__":
    Nums = dict()
    for order in [3, 4, 5, 6, 7, 8]:
        Nums[str(order)] = generate_nums(order)

    for order, nums in Nums.items():
        print(f'order: {order} | count: {len(nums)} ')
        print(f'nums: {nums} ')

    backtracking(Nums, [], [])
    print('\n')