import time
import numpy as np

L = np.arange(10, dtype=int)

Perm = []
for i1 in L:
    perm1 = [i1]
    L1 = L[L != i1]
    for i2 in L1:
        perm2 = perm1 + [i2]
        L2 = L1[L1 != i2]
        for i3 in L2:
            perm3 = perm2 + [i3]
            L3 = L2[L2 != i3]
            for i4 in L3:
                perm4 = perm3 + [i4]
                L4 = L3[L3 != i4]
                for i5 in L4:
                    perm5 = perm4 + [i5]
                    L5 = L4[L4 != i5]
                    for i6 in L5:
                        perm6 = perm5 + [i6]
                        L6 = L5[L5 != i6]
                        for i7 in L6:
                            perm7 = perm6 + [i7]
                            L7 = L6[L6 != i7]
                            for i8 in L7:
                                perm8 = perm7 + [i8]
                                L8 = L7[L7 != i8]
                                for i9 in L8:
                                    perm9 = perm8 + [i9]
                                    L9 = L8[L8 != i9]
                                    for i10 in L9:
                                        perm10 = perm9 + [i10]
                                        Perm.append(perm10)
            
print(Perm[999999:1000002])