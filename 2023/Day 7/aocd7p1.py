cardsnbids = []
order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

with open("aocd7.txt", "r") as aocd7:
    for line in aocd7:
        a, b = line.strip().split()
        cardsnbids.append((a, int(b)))

fiveofakind = []
fourofakind = []
fullhouse = []
threeofakind = []
twopair = []
onepair = []
highcard = []

for erm in cardsnbids:
    card = erm[0]
    s = set(card)
    repeats = {}
    if len(s) == 5:
        highcard.append(erm)
    elif len(s) == 4:
        onepair.append(erm)
    elif len(s) == 3:
        for i in card:
            if i not in repeats:
                repeats[i] = 1
            else:
                repeats[i] += 1
        if set(repeats.values()) == {1, 2}:
            twopair.append(erm)
        else:
            threeofakind.append(erm)
    elif len(s) == 2:
        for i in card:
            if i not in repeats:
                repeats[i] = 1
            else:
                repeats[i] += 1
        for x in repeats:
            if repeats[x] == 2 or repeats[x] == 3:
                fullhouse.append(erm)
            else:
                fourofakind.append(erm)
            break
    elif len(s) == 1:
        fiveofakind.append(erm)

def sort1(oh):
    ah = oh[0]
    return order.index(ah[0])
def sort2(oh):
    ah = oh[0]
    return order.index(ah[1])
def sort3(oh):
    ah = oh[0]
    return order.index(ah[2])
def sort4(oh):
    ah = oh[0]
    return order.index(ah[3])
def sort5(oh):
    ah = oh[0]
    return order.index(ah[4])

final = []
def ahah(oh):
    oh.sort(key=sort5)
    oh.sort(key=sort4)
    oh.sort(key=sort3)
    oh.sort(key=sort2)
    oh.sort(key=sort1)
    final.extend(oh)

ahah(fiveofakind)
ahah(fourofakind)
ahah(fullhouse)
ahah(threeofakind)
ahah(twopair)
ahah(onepair)
ahah(highcard)

rank = len(final)
total = 0
for x in final:
    total+= x[1]*rank
    rank-=1



print(total)