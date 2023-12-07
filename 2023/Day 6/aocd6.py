# Part 1
aocd6 = open("aocd6.txt", "r")
time = aocd6.readline()[13::].strip().split("     ")
distance = aocd6.readline()[12::].strip().split("   ")
aocd6.close()
er = 1
for et in range(len(time)):
    ways = 0
    for hold in range(int(time[et]) + 1):
        d = hold*(int(time[et]) - hold)
        if d > int(distance[et]):
            ways+=1
    er*=ways
print(er)


# Part 2
aocd6 = open("aocd6.txt", "r")
time = "".join(aocd6.readline()[13::].strip().split("     "))
distance = "".join(aocd6.readline()[12::].strip().split("   "))
aocd6.close()
ways = 0
for hold in range(int(time) + 1):
    d = hold*(int(time) - hold)
    if d > int(distance):
        ways+=1
print(ways)
