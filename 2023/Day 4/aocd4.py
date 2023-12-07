'''total = 0
with open("aocd4.txt", "r") as aocd4:
    for row in aocd4:
        score = 0
        line = row[10::]
        winning, own = line.split("|")
        winning = winning.split(" ")
        for x, num in enumerate(winning):
            if num == "":
                winning.pop(x)

        own = own.split(" ")
        for y, numm in enumerate(own):
            if numm == "":
                own.pop(y)
            if y == len(own) - 1:
                own[y] = own[y][0:-1]
            
        for eh in own:
            if eh in winning:
                score+=1
        if score != 0:
            score-=1
            total += (2**(score))
    print(total)'''

total = 0
multiplier = {}
with open("aocd4.txt", "r") as aocd4:
    for index, row in enumerate(aocd4):
        erm = 0
        score = 0
        line = row[10::]
        winning, own = line.split("|")
        winning = winning.split(" ")
        for x, num in enumerate(winning):
            if num == "":
                winning.pop(x)

        own = own.split(" ")
        for y, numm in enumerate(own):
            if numm == "":
                own.pop(y)
            if y == len(own) - 1:
                own[y] = own[y][0:-1]
        
        for eh in own:
            if eh in winning:
                score+=1
            
        if score == 0:
            break

        if index in multiplier:
            total += (score*multiplier[index]) + 1
        else:
            total+= score

        for x in range(1, (score + 1)):
            temp = index + x
            if index != 0:
                ehe = multiplier[index]
            else:
                ehe = 1

            if temp not in multiplier:
                multiplier[temp] = ehe
            else:
                multiplier[temp] += ehe

print(total)



       



