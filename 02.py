with open("2.txt") as file_obj:
    lines = file_obj.readlines()

valid = 0

for line in lines:
    rule, password = line.split(": ")
    counts, letter = rule.split(" ")
    lowest, highest = [int(x) for x in counts.split("-")]
    count = password.count(letter)
    if lowest <= count <= highest:
        valid += 1

print(valid)