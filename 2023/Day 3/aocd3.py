import re

total = 0

with open("aocd3.txt", "r") as aocd3:
    
    grid = []
    for oomph in aocd3:
        grid.append(oomph)

    for rownum, line in enumerate(grid):
        matches1 = re.findall(r'[!@#$%^&*()_+=/?<>~`]+[0-9]+', line)
        matches2 = re.findall(r'[0-9]+[!@#$%^&*()_+=/?<>~`]+', line)
        for match1 in matches1:
            total+=int(match1[1::])
        for match2 in matches2:
            total+=int(match2[0:-1])    
        
        coordinatesuh = []
        coordinateseh = []
        coordinatesic = []
        for uh in re.finditer(r'[.][0-9]+[.]', line):
            coordinatesuh.append(uh.span())
        for eh in re.finditer(r'^[0-9]+[.]', line):
            coordinateseh.append(eh.span())
        for ic in re.finditer(r'$[.][0-9]+', line):
            coordinatesic.append(ic.span())
        
        tracker = []
        for er, coorduh in enumerate(coordinatesuh):
            if rownum != (len(grid) - 1):
                woosh = grid[rownum + 1][(coorduh[0]):(coorduh[1])]
                if re.search('[!@#$%^&*()_+=/?<>~`]+', woosh) is not None:
                    if er not in tracker:
                        tracker.append(er)
                        total+=int(grid[rownum][(coorduh[0]+1):(coorduh[1] - 1)])
                        #print(grid[rownum][(coorduh[0]+1):(coorduh[1] - 1)])
            if rownum != 0:
                woosh = grid[rownum - 1][(coorduh[0]):(coorduh[1])]
                if re.search('[!@#$%^&*()_+=/?<>~`]+', woosh) is not None:
                    if er not in tracker:
                        tracker.append(er)
                        total+=int(grid[rownum][(coorduh[0]+1):(coorduh[1] - 1)])
                        #print(grid[rownum][(coorduh[0]+1):(coorduh[1] - 1)])

        tracker = []
        for er, coordeh in enumerate(coordinateseh):
            if rownum != (len(grid) - 1):
                woosh = grid[rownum + 1][(coordeh[0]):(coordeh[1])]
                if re.search('[!@#$%^&*()_+=/?<>~`]+', woosh) is not None:
                    if er not in tracker:
                        tracker.append(er)
                        total+=int(grid[rownum][(coordeh[0]):(coordeh[1] - 1)])
            if rownum != 0:
                woosh = grid[rownum - 1][(coordeh[0]):(coordeh[1])]
                if re.search('[!@#$%^&*()_+=/?<>~`]+', woosh) is not None:
                    if er not in tracker:
                        tracker.append(er)
                        total+=int(grid[rownum][(coordeh[0]):(coordeh[1] - 1)])

        tracker = []
        for er, coordic in enumerate(coordinatesic):
            if rownum != (len(grid) - 1):
                woosh = grid[rownum + 1][(coordic[0]):(coordic[1])]
                if re.search('[!@#$%^&*()_+=/?<>~`]+', woosh) is not None:
                    if er not in tracker:
                        tracker.append(er)
                        total+=int(grid[rownum][(coordic[0]+1):(coordic[1])])
            if rownum != 0:
                woosh = grid[rownum - 1][(coordic[0]):(coordic[1])]
                if re.search('[!@#$%^&*()_+=/?<>~`]+', woosh) is not None:
                    if er not in tracker:
                        tracker.append(er)
                        total+=int(grid[rownum][(coordic[0]+1):(coordic[1])])
print(total)


            


'''
symbol = 0
with open ("aocd3.txt", "r") as aocd3:
    
    for eh, row in enumerate(grid):
        number_found = False
        for count, char in enumerate(row):
            if char.isnumeric():
                if count != 0:
                    if not row[count - 1].isnumeric():
                        number = int(char)
                        number_found = True
                        if row[count + 1].isnumeric():
                            number = number*10 + int(row[count+1])
                            if row[count + 2].isnumeric():
                                number = number*10 + int(row[count+2])
            if number_found:
                if eh == 0:
                    if len(str(number)) == 1:
                        # edge cases
                        if count != (len(row) - 1:)
                        if (not row[count + 1].isnumeric()) and (row[count + 1] != "."):
                            symbol += number
                        elif (not grid[eh+1][count].isnumeric() and grid[eh+1][count] != ".") or (not grid[eh+1][count+1].isnumeric() and grid[eh+1][count+1] != "."):
                            symbol += number
                        if count != 0:


                    elif len(str(number)) == 2:
                        if (not row[count + 2].isnumeric()) and (row[count + 2] != "."):
                            symbol += number
                        elif (not grid[eh+1][count].isnumeric() and grid[eh+1][count] != ".") or (not grid[eh+1][count+1].isnumeric() and grid[eh+1][count+1] != ".") or (not grid[eh+1][count+2].isnumeric() and grid[eh+1][count+2] != "."):
                            symbol += number

                    elif len(str(number)) == 3:
                        if (not row[count + 3].isnumeric()) and (row[count + 3] != "."):
                            symbol += number
                        elif (not grid[eh+1][count].isnumeric() and grid[eh+1][count] != ".") or (not grid[eh+1][count+1].isnumeric() and grid[eh+1][count+1] != ".") or (not grid[eh+1][count+2].isnumeric() and grid[eh+1][count+2] != ".") or (not grid[eh+1][count+3].isnumeric() and grid[eh+1][count+3] != "."):
                            symbol += number 

                    else


                number_found = False
                    '''