#product of a pythagorean triplet that sums up to 1000
PT = []
PT1000 = []

for integer1 in range(1, 1000):
    if integer1 < 1000 - integer1: limit1 = integer1
    else: limit1 = 1000 - integer1

    for integer2 in range(1, limit1 + 1):
        if integer2 < 1000 - integer1 - integer2: limit2 = integer2
        else: limit2 = 1000 - integer1 - integer2
        for integer3 in range(1, limit2 + 1):

            if ((integer3 * integer3) + (integer2 * integer2)) == (integer1 * integer1):
                PT.append((integer3, integer2, integer1))

for triplet in PT:
    if triplet[0] + triplet[1] + triplet[2] == 1000:
        PT1000.append(triplet)

triplet = PT1000[0]
print(((triplet[0] * triplet[0]) + (triplet[1] * triplet[1])) == (triplet[2] * triplet[2]))
print(triplet[0] + triplet[1] + triplet[2])
print(triplet[0] * triplet[1] * triplet[2])