from math import lcm

# Part 1
with open("aocd8.txt", "r") as aocd8:
    directions = aocd8.readline().strip()
    aocd8.readline()
    nodes = {}
    for line in aocd8:
        temp = line.strip()
        source = temp[0:3] ; temp = temp[7:15]
        left, right = temp.split(",") ; right = right[1::]
        nodes[source] = (left,right)
        
deb = {"L": 0, "R": 1} ; found = False ; start = "AAA" 
d_pointer = 0 ; counter = 0
while not found:
    counter += 1
    next = nodes[start][deb[directions[d_pointer]]]
    if next == "ZZZ":
        found = True
    else:
        start = next
        if d_pointer == len(directions) - 1:
            d_pointer = 0
        else:
            d_pointer += 1

print(counter)

# Part 2
starts = []
with open("aocd8.txt", "r") as aocd8:
    directions = aocd8.readline().strip()
    aocd8.readline()
    nodes = {}
    for line in aocd8:
        temp = line.strip()
        source = temp[0:3] ; temp = temp[7:15]
        left, right = temp.split(",") ; right = right[1::]
        nodes[source] = (left,right)
        if source[2] == "A":
            starts.append(source)
        
deb = {"L": 0, "R": 1}

ends = []

for start in starts:
    found = False ; d_pointer = 0 ; counter = 0

    while not found:
        counter += 1
        next = nodes[start][deb[directions[d_pointer]]]
        if next[2] == "Z":
            found = True
            ends.append(counter)
        else:
            start = next
            if d_pointer == len(directions) - 1:
                d_pointer = 0
            else:
                d_pointer += 1

uhh = 1
for x in range(len(ends)):
    uhh = lcm(uhh, ends[x])
print(uhh)