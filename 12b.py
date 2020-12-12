with open("12.txt") as file_obj:
    lines = [line.strip() for line in file_obj.readlines()]

DIRECTIONS = "NESW"

DIRECTION_TO_CHANGE = {
    "N": ("N", 1),
    "E": ("E", 1),
    "S": ("N", -1),
    "W": ("E", -1)
}

def rotate_waypoint(waypoint, direction, angle):
    north, east = waypoint["N"], waypoint["E"]
    turns = angle // 90
    if direction == "L":
        for _ in range(turns):
            north, east = east, -north
    else:
        for _ in range(turns):
            north, east = -east, north
    return {"N": north, "E": east}


class Ship:
    def __init__(self):
        self.waypoint = {"N": 1, "E": 10}
        self.ship = {"N": 0, "E": 0}

    def process(self, instruction):
        command, distance = instruction[0], int(instruction[1:])
        if command in DIRECTIONS:
            direction, mult = DIRECTION_TO_CHANGE[command]
            self.waypoint[direction] += (mult * distance)
        elif command == "F":
            for direction in self.ship:
                self.ship[direction] += (distance * self.waypoint[direction])
        else:
            self.waypoint = rotate_waypoint(self.waypoint, command, distance)
    
    def manhattan(self):
        return abs(self.ship["N"]) + abs(self.ship["E"])

ship = Ship()
for line in lines:
    ship.process(line)
print(ship.manhattan())
