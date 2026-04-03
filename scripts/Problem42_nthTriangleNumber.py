with open('p042_words.txt', 'r') as file:
    for line in file:
        Words = [elem.strip('"') for elem in line.split(',')]
        m = max([len(elem) for elem in Words])

        Num_values = dict()

        Letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
        for index, letter in enumerate(Letters):
            Num_values[letter] = index + 1

        Tr_nums = [1]
        limit = m * Num_values['z']
        n = 2
        while Tr_nums[-1] < limit:
            Tr_nums.append(int((1/2)*n*(n+1)))
            n += 1
        print(Tr_nums)

        c = 0
        for word in Words:
            num_value = 0
            for letter in word:
                num_value += Num_values[letter.lower()]
            
            if num_value in Tr_nums:
                c += 1
        print(c)