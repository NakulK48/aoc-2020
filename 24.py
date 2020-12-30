with open("24.txt") as file_obj:
    lines = [line.strip() for line in file_obj.readlines()]

def move(x, y, z, direction):
    destination = {
        "ne": (x + 1, y, z - 1),
        "nw": (x, y + 1, z - 1),
        "e": (x + 1, y - 1, z),
        "w": (x - 1, y + 1, z),
        "se": (x, y - 1, z + 1),
        "sw": (x - 1, y, z + 1),
    }
    return destination[direction]

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

flipped = set()

for line in lines:
    destination = parse_line(line)
    if destination in flipped:
        flipped.remove(destination)
    else:
        flipped.add(destination)

print(len(flipped))
