power_thingy = []

with open("aocd2.txt", "r") as aocd2:
    for line in aocd2:
        if line[6] == ":":
            new_line = line[8::]
            new_line = new_line.strip()
            balls = new_line.split(";")

        elif line[7] == ":":
            new_line = line[9::]
            new_line = new_line.strip()
            balls = new_line.split(";")

        elif line[8] == ":":
            new_line = line[10::]
            new_line = new_line.strip()
            balls = new_line.split(";")

        okay = True
        red = 0
        blue = 0
        green = 0
        for game in balls:            
            roundb = game.strip()
            roundb = roundb.split(" ")
            for eh in range(0, len(roundb), 2):
                print(roundb[eh], roundb[eh+1])
                if (roundb[eh+1] == "red") or (roundb[eh+1] == "red,"):
                    if int(roundb[eh]) > red:
                        red = int(roundb[eh])
                        

                elif (roundb[eh+1] == "green") or (roundb[eh+1] == "green,"):
                    if int(roundb[eh]) > green:
                        green = int(roundb[eh])
                        

                elif (roundb[eh+1] == "blue") or (roundb[eh+1] == "blue,"):
                    if int(roundb[eh]) > blue:
                        blue = int(roundb[eh])

        power_thingy.append((red*blue*green))
        print(f"red {red}, blue {blue}, green {green}")
        
total = 0
for i in power_thingy:
    total+= i
print(total)