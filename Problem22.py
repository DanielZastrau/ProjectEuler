with open('p022_names.txt', 'r') as file:
    for line in file:
        Names_V1 = line.split(',')
        Names_V2 = list(map(lambda name: name[1:-1], Names_V1))
        Names_V3 = sorted(Names_V2)

alphabeticalValue = [None] + 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
nameScores = []
nameScore_0 = 0
sOuter = 0

for indexOuter in range(len(Names_V3)):
    name = Names_V3[indexOuter]
    s = 0

    for letter in name:
        for index in range(len(alphabeticalValue)):
            if alphabeticalValue[index] == letter:
                s = s + index

    s = s * (indexOuter + 1)
    sOuter = sOuter + s

print(sOuter)