"""https://projecteuler.net/problem=84"""

if __name__=="__main__":
    from time import time, sleep
    from random import shuffle, choice

    class Player:
        
        def __init__(self):
            self.pos = 0

        def update_pos(self, step):
            self.pos = (self.pos + step) % 40

    t = time()

    iterations = 10**5
    sides = 4
    player = Player()
    Pos = [0]*40
    CC = [i for i in range(0, 16)]; shuffle(CC)
    CC_index = 0
    CH = [i for i in range(0, 16)]; shuffle(CH)
    CH_index = 0
    Dice_sums = [ i + j for i in range(1, sides +1) for j in range(1, sides +1)]; shuffle(Dice_sums)

    for _ in range(iterations):
        step = choice(Dice_sums)
        player.update_pos(step)
        
        # handle Go to Jail
        if player.pos == 30:
            player.pos = 10

        # handle the CC cards
        elif player.pos in [2, 17, 33]:
            card = CC[CC_index]
            CC_index += 1
            CC_index %= 16

            if card == 0:
                player.pos = 0
            elif card == 1:
                player.pos = 10

        # handle the CH cards
        elif player.pos in [7, 22, 36]:
            card = CH[CH_index]
            CH_index += 1
            CH_index %= 16

            if card == 0:
                player.pos = 0
            elif card == 1:
                player.pos = 10
            elif card == 2:
                player.pos = 11
            elif card == 3:
                player.pos = 24
            elif card == 4:
                player.pos = 39
            elif card == 5:
                player.pos = 5
            elif card == 6 or card == 7:
                while player.pos not in [5, 15, 25, 35]:
                    player.pos += 1
                    if player.pos > 39:
                        player.pos %= 40
            elif card == 8:
                while player.pos not in [12, 28]:
                    player.pos += 1
                    if player.pos > 39:
                        player.pos %= 40
            elif card == 9:
                player.pos -= 3

        Pos[player.pos] += 1


    Pos = [ e/iterations for e in Pos ]
    Tmp = Pos.copy()
    for _ in range(3):
        m = max(Tmp); Tmp.remove(m)
        print(Pos.index(m))
    
    print(time() -t)