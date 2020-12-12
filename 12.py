with open("12.txt") as file_obj:
    lines = [line.strip() for line in file_obj.readlines()]

DIRECTIONS = "NESW"
DIRECTION_TO_INDEX = {direction: index for index, direction in enumerate(DIRECTIONS)}

DIRECTION_TO_CHANGE = {
    "N": ("N", 1),
    "E": ("E", 1),
    "S": ("N", -1),
    "W": ("E", -1)
}

def turn(original, direction, distance):
    multiplier = (1 if direction == "R" else -1)
    index = DIRECTION_TO_INDEX[original]
    index += (distance // 90) * multiplier
    return DIRECTIONS[index % 4]

class Ship:
    def __init__(self):
        self.direction = "E"
        self.distances = {"N": 0, "E": 0}

    def process(self, instruction):
        command, distance = instruction[0], int(instruction[1:])
        if command in "LR":
            self.direction = turn(self.direction, command, distance)
            return
        direction = self.direction if command == "F" else command
        new_direction, mult = DIRECTION_TO_CHANGE[direction]
        self.distances[new_direction] += (mult * distance)
    
    def manhattan(self):
        return abs(self.distances["N"]) + abs(self.distances["E"])

ship = Ship()
for line in lines:
    ship.process(line)
print(ship.manhattan())
