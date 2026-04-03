"""
https://projecteuler/problem=54
"""

def consec(player):
    Cards = []
    for key, value in player['values'].items():
        Cards.extend([ key for i in range(value) ])
    Cards = sorted(Cards)

    if 14 != Cards[-1]:
        if Cards[1] == Cards[0] + 1 and Cards[2] == Cards[0] + 2 \
                and Cards[3] == Cards[0] + 3 and Cards[4] == Cards[0] + 4:
            return True
    elif 14 == Cards[-1]:
        if Cards[1] == Cards[0] + 1 and Cards[2] == Cards[0] + 2 \
                and Cards[3] == Cards[0] + 3 and Cards[0] == 2:
            return True
    return False

def count(player):
    d = dict()
    for elem in [ elem[0] for elem in player ]:
        if elem in d.keys():
            d[elem] += 1
        else:
            d[elem] = 1
    return d


def royal_flush(player):
    if len(player['suits'].keys()) == 1 and player['values'].keys() == [10, 11, 12, 13, 14]:
            return True
    return False

def straight_flush(player):
    if len( player['suits'].keys() ) == 1 and len( player['values'].keys() ) == 5:
        if consec(player):
            return True
    return False

def four_kind(player):
    if 4 in player['values'].values():
        return True
    return False

def full_house(player):
    tmp = player['values'].values()
    if 3 in tmp and 2 in tmp:
        return True
    return False

def flush(player):
    if len( player['suits'].keys() ) == 1:
        return True
    return False

def straight(player):
    if consec(player):
        return True
    return False

def three_kind(player):
    if 3 in player['values'].values():
        return True
    return False

def two_pairs(player):
    c = 0
    for value in player['values'].values():
        if value == 2:
            c += 1

    if c == 2:
        return True
    return False

def one_pair(player):
    if 2 in player['values'].values():
        return True
    return False


def highest_rank(player):
    if royal_flush(player):
        return 9

    elif straight_flush(player):
        return 8

    elif four_kind(player):
        return 7

    elif full_house(player):
        return 6

    elif flush(player):
        return 5

    elif straight(player):
        return 4

    elif three_kind(player):
        return 3

    elif two_pairs(player):
        return 2

    elif one_pair(player):
        return 1

    else:
        return 0

def compare_rank(rank, player1, player2):
    print(player1)
    print(player2)

    if rank == 9:
        print('you need to think of something here for royal flush')

    elif rank == 8:    # straight flush
        Cards1 = list( player1['values'].keys() )
        Cards2 = list( player2['values'].keys() )

        if Cards1[0] == 2 and Cards1[-1] == 14:
            min1 = 1
        else: min1 = Cards1[0]

        if Cards2[0] == 2 and Cards2[-1] == 14:
            min1 = 1
        else: min1 = Cards2[0]

        if min1 > min2:
            return 1
        elif min1 < min2:
            return -1
        else:
            return 0

    elif rank == 7:    # four of a kind
        for key, value in player1['values'].items():
            if value == 4:
                card1 = key

        for key, value in player2['values'].items():
            if value == 4:
                card2 = key

        if card1 > card2:
            return 1
        elif card1 < card2:
            return -1
        else:
            return 0

    elif rank == 6:    # full house
        for key, value in player1['values'].items():
            if value == 3:
                card1 = key
        
        for key, value in player2['values'].items():
            if value == 3:
                card2 = key

        if card1 > card2:
            return 1
        elif card1 < card2:
            return -1
        else:
            for key, value in player1['values'].items():
                if value == 2:
                    card1 = key
            
            for key, value in player2['values'].items():
                if value == 2:
                    card2 = key

            if card1 > card2:
                return 1
            elif card1 < card2:
                return -1
            else:
                return 0

    elif rank == 5:    # flush
        return compare_rank(0, player1, player2)

    elif rank == 4:    # straight
        Cards1 = player1['values'].keys()
        if 14 in Cards1 and 2 in Cards1:
            card1 = 1
        else:
            card1 = min(Cards1)

        Cards2 = player2['values'].keys()
        if 14 in Cards2 and 2 in Cards2:
            card2 = 1
        else:
            card2 = min(Cards2)

        if card1 > card2:
            return 1
        elif card1 < card2:
            return -1
        else:
            return 0

    elif rank == 3:    # three of a kind
        for key, value in player1['values'].items():
            if value == 3:
                card1 = key
        
        for key, value in player2['values'].items():
            if vlaue == 3:
                card2 = key

        if card1 > card2:
            return 1
        elif card1 < card2:
            return -1
        else:
            return 0        

    elif rank == 2:    # two pairs
        max1 = 0
        for key, value in player1['values'].items():
            if value == 2 and key > max1:
                max1 = key
        
        max2 = 0
        for key, value in player2['values'].items():
            if value == 2 and key > max2:
                max2 = key

        if max1 > max2:
            return 1
        elif max1 < max2:
            return -1
        else:
            max1_ = 0
            for key, value in player1['values'].items():
                if value == 2 and key > max1_ and key != max1:
                    max1_ = key

            max2_ = 0
            for key, value in player2['values'].items():
                if value == 2 and key > max2_ and key != max2:
                    max2_ = key

            if max1_ > max2_:
                return 1
            elif max1_ < max2_:
                return -1
            else:
                return 0

    elif rank == 1:    # one pair
        for key, value in player1['values'].items():
            if value == 2:
                max1 = key
            
        for key, value in player2['values'].items():
            if value == 2:
                max2 = key

        if max1 > max2:
            return 1
        elif max1 < max2:
            return -1
        else:
            return 0

    else:              # high card
        Cards1 = []
        for key, value in player1['values'].items():
            Cards1.extend([ key for i in range(value) ])
        Cards1 = sorted(Cards1)

        Cards2 = []
        for key, value in player2['values'].items():
            Cards2.extend([ key for i in range(value) ])
        Cards2 = sorted(Cards2)

        for i in range(5):
            highest_card1 = max(Cards1[:5 - i])
            highest_card2 = max(Cards2[:5 - i])

            if highest_card1 > highest_card2:
                return 1
            elif highest_card1 < highest_card2:
                return -1
            else:
                continue
        return 0


def preprocessing(player):
    Out = {
        'values':{},
        'suits':{},
        'cards':player
    }

    v_dict = {
        '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
        'T':10, 'J':11, 'Q':12, 'K':13, 'A':14
    }

    for value in [ elem[0] for elem in player ]:
        num_value = v_dict[value]

        if num_value in Out['values'].keys():
            Out['values'][num_value] += 1
        else:
            Out['values'][num_value] = 1

    for suit in [ elem[1] for elem in player ]:
        
        if suit in Out['suits'].keys():
            Out['suits'][suit] += 1
        else:
            Out['suits'][suit] = 1

    return Out


def main():
    with open('p054_poker.txt', 'r') as file:
        Games = []

        for line in file:
            clean_line = line.strip().split(' ')

            player1 = clean_line[:5]
            player2 = clean_line[5:]
            Games.append([player1, player2])

    win = 0
    for game in Games:
        player1 = game[0]
        player2 = game[1]

        player1 = preprocessing(player1)
        player2 = preprocessing(player2)

        h1 = highest_rank(player1)
        h2 = highest_rank(player2)

        if h1 > h2:
            win += 1
        elif h1 == h2:
            res = compare_rank(h1, player1, player2)
            if res == 1:
                win += 1
            elif res == 0:
                res = compare_rank(0, player1, player2)
                if res == 1:
                    win += 1

    return win

print(main())