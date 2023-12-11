# Part 1
total = 0

def exp_val_finder(sequence):
    if set(sequence) == {0}:
        return 0
    else:
        a = []
        for x in range(1, len(sequence)):
            a.append(sequence[x] - sequence[x - 1])
        return sequence[-1] + exp_val_finder(a)

with open("aocd9.txt", "r") as aocd9:
    for line in aocd9:
        seq = line.split(" ")
        s = []
        for num in seq:
            s.append(int(num))
        total += exp_val_finder(s)

print(total)


# Part 2
total = 0

def exp_val_finder(sequence):
    if set(sequence) == {0}:
        return 0
    else:
        a = []
        for x in range(1, len(sequence)):
            a.append(sequence[x] - sequence[x - 1])
        return sequence[0] - exp_val_finder(a)

with open("aocd9.txt", "r") as aocd9:
    for line in aocd9:
        seq = line.split(" ")
        s = []
        for num in seq:
            s.append(int(num))
        total += exp_val_finder(s)

print(total)