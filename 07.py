from collections import defaultdict, deque

containers = defaultdict(set)

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
        _, inner_colour = parse_descriptor(descriptor)
        containers[inner_colour].add(outer_colour)

with open("7.txt") as file_obj:
    lines = file_obj.readlines()

for line in lines:
    parse_line(line)

seen = set()
to_explore = deque()
to_explore.append("shiny gold")

while to_explore:
    colour = to_explore.popleft()
    seen.add(colour)
    for container in containers[colour]:
        to_explore.append(container)

seen.remove("shiny gold")
print(len(seen))
