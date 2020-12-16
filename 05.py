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

max_id = 0

with open("5.txt") as file_obj:
    passes = [line.strip() for line in file_obj.readlines()]

for pass_str in passes:
    pass_id = parse_pass(pass_str)
    max_id = max(max_id, pass_id)

print(max_id)