with open("24.txt") as file_obj:
    lines = [line.strip() for line in file_obj.readlines()]

def get_destinations(x, y, z):
    return {
        "ne": (x + 1, y, z - 1),
        "nw": (x, y + 1, z - 1),
        "e": (x + 1, y - 1, z),
        "w": (x - 1, y + 1, z),
        "se": (x, y - 1, z + 1),
        "sw": (x - 1, y, z + 1),
    }

def move(x, y, z, direction):
    destinations = get_destinations(x, y, z)
    return destinations[direction]

def parse_line(line):
    index = 0
    x = y = z = 0
    while index < len(line):
        if line[index] in "ew":
            direction = line[index]
            index += 1
        else:
            direction = line[index:index+2]
            index += 2
        x, y, z = move(x, y, z, direction)
    return (x, y, z)

black = set()

for line in lines:
    destination = parse_line(line)
    if destination in black:
        black.remove(destination)
    else:
        black.add(destination)

TURNS = 100

def becomes_black(node):
    currently_black = (node in black)
    adjacent = get_destinations(*node).values()
    black_adjacent = sum(1 for adj in adjacent if adj in black)
    if currently_black:
        return black_adjacent in (1, 2)
    else:
        return black_adjacent == 2


for _ in range(TURNS):
    new_black = set()
    nodes_to_consider = set()
    for node in black:
        nodes_to_consider.add(node)
        destinations = get_destinations(*node)
        nodes_to_consider |= set(destinations.values())
    
    for node in nodes_to_consider:
        if becomes_black(node):
            new_black.add(node)

    black = new_black

print(len(black))
