# Part 1
maxcal = 0
with open("aocd1.txt", "r") as aocd1:
    each_total = 0
    for line in aocd1:
        if line == "\n":
            if each_total > maxcal:
                maxcal = each_total
            each_total = 0
        else:
            each_total += int(line.strip())

print(maxcal)

# Part 2
calories = []
with open("aocd1.txt", "r") as aocd1:
    each_total = 0
    for line in aocd1:
        if line == "\n":
            calories.append(each_total)
            each_total = 0
        else:
            each_total += int(line.strip())

calories.sort(reverse=True)
print(calories[0]+calories[1]+calories[2])
