reds = 12
blues = 14
greens = 13
id_store = []

with open("aocd2.txt", "r") as aocd2:
    for line in aocd2:
        if line[6] == ":":
            game_id = int(line[5])
            new_line = line[8::]
            new_line = new_line.strip()
            balls = new_line.split(";")

        elif line[7] == ":":
            game_id = int(line[5:7])
            new_line = line[9::]
            new_line = new_line.strip()
            balls = new_line.split(";")

        elif line[8] == ":":
            game_id = int(line[5:8])
            new_line = line[10::]
            new_line = new_line.strip()
            balls = new_line.split(";")

        else:
            pass

        okay = True
        for game in balls:
            roundb = game.strip()
            roundb = roundb.split(" ")
            for eh in range(0, len(roundb), 2):
                print(roundb[eh], roundb[eh+1])
                if (roundb[eh+1] == "red") or (roundb[eh+1] == "red,"):
                    if (reds - int(roundb[eh])) < 0:
                        okay = False
                        

                elif (roundb[eh+1] == "green") or (roundb[eh+1] == "green,"):
                    if (greens - int(roundb[eh])) < 0:
                        okay = False
                        

                elif (roundb[eh+1] == "blue") or (roundb[eh+1] == "blue,"):
                    if (blues - int(roundb[eh])) < 0:
                        okay = False
                        

                else:
                    pass
                if not okay:
                    break
            if not okay:
                    break
        
        if okay:
            id_store.append(game_id)
            print(game_id)
        
total = 0
for i in id_store:
    total += i
print(total)