with open("4.txt") as file_obj:
    passports = [line.replace("\n", " ") for line in file_obj.read().split("\n\n")]

valid_count = 0

NULL_RANGE = range(0)

UNIT_RANGE = {
    "cm": range(150, 194),
    "in": range(59, 77), 
}

def validate_height(height):
    height_num, height_unit = int(height[:-2]), height[-2:]
    return height_num in UNIT_RANGE.get(height_unit, NULL_RANGE)

EYES = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

FIELD_RULES = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: len(x) > 2 and validate_height(x),
    "hcl": lambda x: len(x) == 7 and x[0] == "#" and all(char.isalnum() for char in x[1:]),
    "ecl": lambda x: x in EYES,
    "pid": lambda x: len(x) == 9 and x.isdigit(),
}
ALL_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

for passport in passports:
    this_passport_fields = set()
    pairs = passport.split(" ")
    for pair in pairs:
        field, value = pair.split(":")
        rule = FIELD_RULES.get(field)
        if rule and not rule(value):
            break
        this_passport_fields.add(field)

    if ALL_FIELDS.issubset(this_passport_fields):
        valid_count += 1

print(valid_count)
