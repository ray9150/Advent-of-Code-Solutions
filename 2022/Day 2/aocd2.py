# Part 1
total = 0
with open("aocd2.txt", "r") as aocd2:
    for line in aocd2:
        them, you = line.strip().split(" ")

        if them == "A":
            if you == "X":
                total += 4
            elif you == "Y":
                total += 8
            elif you == "Z":
                total += 3

        elif them == "B":
            if you == "X":
                total += 1
            elif you == "Y":
                total += 5
            elif you == "Z":
                total += 9
                
        elif them == "C":
            if you == "X":
                total += 7
            elif you == "Y":
                total += 2
            elif you == "Z":
                total += 6

print(total)

# Part 2
total = 0
with open("aocd2.txt", "r") as aocd2:
    for line in aocd2:
        them, you = line.strip().split(" ")

        if them == "A":
            if you == "X":
                total += 3
            elif you == "Y":
                total += 4
            elif you == "Z":
                total += 8

        elif them == "B":
            if you == "X":
                total += 1
            elif you == "Y":
                total += 5
            elif you == "Z":
                total += 9
                
        elif them == "C":
            if you == "X":
                total += 2
            elif you == "Y":
                total += 6
            elif you == "Z":
                total += 7

print(total)