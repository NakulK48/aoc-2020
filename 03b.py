with open("3.txt") as file_obj:
    GRID = [line.strip() for line in file_obj.readlines()]

MAX_X = len(GRID[0])
MAX_Y = len(GRID)

STEP_PAIRS = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]

total = 1

for x_step, y_step in STEP_PAIRS:
    trees = x = y = 0

    while y < MAX_Y:
        cell = GRID[y][x]
        if cell == "#":
            trees += 1
        x = (x + x_step) % MAX_X
        y += y_step

    print(trees)
    total *= trees

print()
print(total)
