with open("4.txt") as file_obj:
    passports = [line.replace("\n", " ") for line in file_obj.read().split("\n\n")]

valid_count = 0
ALL_FIELDS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

for passport in passports:
    this_passport_fields = set()
    pairs = passport.split(" ")
    for pair in pairs:
        field, _ = pair.split(":")
        this_passport_fields.add(field)

    if ALL_FIELDS.issubset(this_passport_fields):
        valid_count += 1
    
print(valid_count)