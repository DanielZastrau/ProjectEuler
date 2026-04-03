import numpy as np
import math
import time

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def pandigitals():
    L = np.arange(10, dtype=int)
    L = L[1:]
    Pans = []

    for c in range(9):
        if c == 0:
            L0 = L[:1]
            for i1 in L0:
                Pans.append(i1)
        if c == 1:
            L0 = L[:2]
            for i1 in L0:
                s1 = str(i1)
                L1 = L0[L0 != i1]
                for i2 in L1:
                    Pans.append(int(s1 + str(i2)))
        if c == 2:
            L0 = L[:3]
            for i1 in L0:
                s1 = str(i1)
                L1 = L0[L0 != i1]
                for i2 in L1:
                    s2 = s1 + str(i2)
                    L2 = L1[L1 != i2]
                    for i3 in L2:
                        Pans.append(int(s2 + str(i3)))
        if c == 3:
            L0 = L[:4]
            for i1 in L0:
                s1 = str(i1)
                L1 = L0[L0 != i1]
                for i2 in L1:
                    s2 = s1 + str(i2)
                    L2 = L1[L1 != i2]
                    for i3 in L2:
                        s3 = s2 + str(i3)
                        L3 = L2[L2 != i3]
                        for i4 in L3:
                            Pans.append(int(s3 + str(i4)))
        if c == 4:
            L0 = L[:5]
            for i1 in L0:
                s1 = str(i1)
                L1 = L0[L0 != i1]
                for i2 in L1:
                    s2 = s1 + str(i2)
                    L2 = L1[L1 != i2]
                    for i3 in L2:
                        s3 = s2 + str(i3)
                        L3 = L2[L2 != i3]
                        for i4 in L3:
                            s4 = s3 + str(i4)
                            L4 = L3[L3 != i4]
                            for i5 in L4:
                                Pans.append(int(s4 + str(i5)))
        if c == 5:
            L0 = L[:6]
            for i1 in L0:
                s1 = str(i1)
                L1 = L0[L0 != i1]
                for i2 in L1:
                    s2 = s1 + str(i2)
                    L2 = L1[L1 != i2]
                    for i3 in L2:
                        s3 = s2 + str(i3)
                        L3 = L2[L2 != i3]
                        for i4 in L3:
                            s4 = s3 + str(i4)
                            L4 = L3[L3 != i4]
                            for i5 in L4:
                                s5 = s4 + str(i5)
                                L5 = L4[L4 != i5]
                                for i6 in L5:
                                    Pans.append(int(s5 + str(i6)))
        if c == 6:
            L0 = L[:7]
            for i1 in L0:
                s1 = str(i1)
                L1 = L0[L0 != i1]
                for i2 in L1:
                    s2 = s1 + str(i2)
                    L2 = L1[L1 != i2]
                    for i3 in L2:
                        s3 = s2 + str(i3)
                        L3 = L2[L2 != i3]
                        for i4 in L3:
                            s4 = s3 + str(i4)
                            L4 = L3[L3 != i4]
                            for i5 in L4:
                                s5 = s4 + str(i5)
                                L5 = L4[L4 != i5]
                                for i6 in L5:
                                    s6 = s5 + str(i6)
                                    L6 = L5[L5 != i6]
                                    for i7 in L6:
                                        Pans.append(int(s6 + str(i7)))
        if c == 7:
            L0 = L[:8]
            for i1 in L0:
                s1 = str(i1)
                L1 = L0[L0 != i1]
                for i2 in L1:
                    s2 = s1 + str(i2)
                    L2 = L1[L1 != i2]
                    for i3 in L2:
                        s3 = s2 + str(i3)
                        L3 = L2[L2 != i3]
                        for i4 in L3:
                            s4 = s3 + str(i4)
                            L4 = L3[L3 != i4]
                            for i5 in L4:
                                s5 = s4 + str(i5)
                                L5 = L4[L4 != i5]
                                for i6 in L5:
                                    s6 = s5 + str(i6)
                                    L6 = L5[L5 != i6]
                                    for i7 in L6:
                                        s7 = s6 + str(i7)
                                        L7 = L6[L6 != i7]
                                        for i8 in L7:
                                            Pans.append(int(s7 + str(i8)))
        if c == 8:
            for i1 in L:
                s1 = str(i1)
                L1 = L[L != i1]
                for i2 in L1:
                    s2 = s1 + str(i2)
                    L2 = L1[L1 != i2]
                    for i3 in L2:
                        s3 = s2 + str(i3)
                        L3 = L2[L2 != i3]
                        for i4 in L3:
                            s4 = s3 + str(i4)
                            L4 = L3[L3 != i4]
                            for i5 in L4:
                                s5 = s4 + str(i5)
                                L5 = L4[L4 != i5]
                                for i6 in L5:
                                    s6 = s5 + str(i6)
                                    L6 = L5[L5 != i6]
                                    for i7 in L6:
                                        s7 = s6 + str(i7)
                                        L7 = L6[L6 != i7]
                                        for i8 in L7:
                                            s8 = s7 + str(i8)
                                            L8 = L7[L7 != i8]
                                            for i9 in L8:
                                                Pans.append(int(s8 + str(i9)))
    return Pans

def largest_pandigital_prime_below(n):
    m = 0
    for pandigital in pandigitals():
        if is_prime(pandigital):
            if pandigital > m:
                m = pandigital
    return m

n = 10 ** 10
print(largest_pandigital_prime_below(n))