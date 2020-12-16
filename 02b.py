with open("2.txt") as file_obj:
    lines = file_obj.readlines()

valid = 0

for line in lines:
    rule, password = line.split(": ")
    counts, letter = rule.split(" ")
    lowest, highest = [int(x) for x in counts.split("-")]
    first_match = (password[lowest-1] == letter)
    second_match = (password[highest-1] == letter)
    if first_match != second_match:
        valid += 1

print(valid)