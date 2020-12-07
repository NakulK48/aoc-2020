from collections import defaultdict, deque

contained = defaultdict(list)

def parse_descriptor(descriptor):
    first_space_index = descriptor.find(" ")
    quantity = int(descriptor[:first_space_index])
    colour = descriptor[first_space_index+1:].replace(" bags", "").replace(" bag", "")
    return (quantity, colour)

def parse_line(line):
    outer, inner_str = line.strip().strip(".").split(" contain ")
    outer_colour = outer.replace(" bags", "")
    if inner_str == "no other bags":
        return
    inner_list = inner_str.split(", ")
    for descriptor in inner_list:
        parsed = parse_descriptor(descriptor)
        contained[outer_colour].append(parsed)

with open("7.txt") as file_obj:
    lines = file_obj.readlines()

for line in lines:
    parse_line(line)

total = 0

def recurse(colour, quantity):
    global total
    total += quantity
    for sub_quantity, sub_colour in contained[colour]:
        recurse(sub_colour, quantity * sub_quantity)

recurse("shiny gold", 1)
print(total - 1)  # exclude the enclosing bag
