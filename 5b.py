def parse_section(part):
    upper, decrease, code = part
    lower = 0

    for letter in code:
        new_divider = (lower + upper) // 2
        if letter == decrease:
            upper = new_divider
        else:
            lower = new_divider
    
    return lower

def parse_pass(pass_str):

    parts = [
        (128, "F", pass_str[:7]),
        (8, "L", pass_str[7:]),
    ]

    col, row = [parse_section(part) for part in parts]
    
    return (col * 8) + row

pass_ids = []

with open("5.txt") as file_obj:
    passes = [line.strip() for line in file_obj.readlines()]

for pass_str in passes:
    pass_id = parse_pass(pass_str)
    pass_ids.append(pass_id)

pass_ids.sort()

prev = pass_ids[0] - 1

for pass_id in pass_ids:
    if prev != (pass_id - 1):
        print(pass_id - 1)
    prev = pass_id