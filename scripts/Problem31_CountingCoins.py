cents = 200
denominations = [200, 100, 50, 20, 10, 5, 2, 1]
counts = {200 : "", 100 : "", 50 : "", 20 : "", 10 : "", 5 : "", 2 : "", 1: ""}

def count_combs(total, i, comb, add):
    if add:
        comb.append(add)
    if total == 0 or (i+1) == len(denominations):
        if (i+1) == len(denominations) and total > 0:
            comb.append( (total, denominations[i]) )
            i += 1
        while i < len(denominations):
            comb.append( (0, denominations[i]) )
            i += 1
        print (" ".join("%d %s" % (n,counts[c]) for (n,c) in comb))
        return 1
    cur = denominations[i]
    return sum(count_combs(total-x*cur, i+1, comb[:], (x,cur)) for x in range(0, int(total/cur)+1))

print(count_combs(cents, 0, [], None))