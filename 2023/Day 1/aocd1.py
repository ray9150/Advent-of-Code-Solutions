# Part 1
'''with open("aocd1.txt", "r") as aocd1:
    total = 0
    for line in aocd1:
        number_found = False
        first_num = 0
        last_num = 0
        for count, character in enumerate(line):
            if character.isnumeric():
                last_num = int(character)
                if not number_found:
                    first_num = int(character)
                    number_found  = True
            
        calibration_val = (first_num*10) + last_num
        print(calibration_val) # for double-checking
        total += calibration_val

print(total)
'''


# Part 2
total = 0

with open("aocd1.txt", "r") as aocd1:
    for line in aocd1:
        number_found = False
        first_num = 0
        last_num = 0
        for count, character in enumerate(line):
            if character.isnumeric():
                last_num = int(character)
                if not number_found:
                    first_num = int(character)
                    number_found  = True

            else:
                digit_to_add = 0
                word_found = False

                if line[count:count+3] == "one":
                    digit_to_add = 1
                    word_found = True
                elif line[count:count+3] == "two":
                    digit_to_add = 2
                    word_found = True
                elif line[count:count+3] == "six":
                    digit_to_add = 6
                    word_found = True
                
                if line[count:count+4] == "four":
                    digit_to_add = 4
                    word_found = True
                elif line[count:count+4] == "five":
                    digit_to_add = 5
                    word_found = True
                elif line[count:count+4] == "nine":
                    digit_to_add = 9
                    word_found = True
                elif line[count:count+4] == "zero":
                    digit_to_add = 0
                    word_found = True

                if line[count:count+5] == "three":
                    digit_to_add = 3
                    word_found = True
                elif line[count:count+5] == "seven":
                    digit_to_add = 7
                    word_found = True
                elif line[count:count+5] == "eight":
                    digit_to_add = 8
                    word_found = True
                
                if word_found:
                    last_num = digit_to_add
                    if not number_found:
                        first_num = digit_to_add
                        number_found  = True

        calibration_val = (first_num*10) + last_num
        print(calibration_val)
        total += calibration_val

print(total)
