"""https://projecteuler.net/problem=68"""

from time import time, sleep

def make(L):
    global Avail_nums

    if len(L) == 10:
        Avail_nums.append(L)
    else:
        for i in range(1, 10):
            if i not in L:
                make(L + [i])

if __name__=="__main__":
    t = time()
    
    Avail_nums = list()
    make([10])

    Sol_sets = list()
    for nums in Avail_nums:
        O = nums[:5]
        I = nums[5:]

        L1 = [O[0], I[0], I[1]]
        L2 = [O[1], I[1], I[2]]
        L3 = [O[2], I[2], I[3]]
        L4 = [O[3], I[3], I[4]]
        L5 = [O[4], I[4], I[0]]

        sum1 = sum(L1)
        sum2 = sum(L2)
        sum3 = sum(L3)
        sum4 = sum(L4)
        sum5 = sum(L5)

        if sum1 == sum2 == sum3 == sum4 == sum5:
            Sol_sets.append([L1, L2, L3, L4, L5])

    Sol_nums = list()
    for list_ in Sol_sets:

        O = [elem[0] for elem in list_]
        for i, e in enumerate(O):
            if e == min(O):
                index = i

        string = str()
        for i in range(5):
            for elem in list_[index]:
                string += str(elem)

            index = (index + 1)%5
        
        Sol_nums.append(int(string))

    print(max(Sol_nums))
    print(time() - t)