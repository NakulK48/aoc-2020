with open("3.txt") as file_obj:
    GRID = [line.strip() for line in file_obj.readlines()]

MAX_X = len(GRID[0])
MAX_Y = len(GRID)

X_STEP = 3
Y_STEP = 1

trees = x = y = 0

while y < MAX_Y:
    cell = GRID[y][x]
    if cell == "#":
        trees += 1
    x = (x + X_STEP) % MAX_X
    y += Y_STEP

print(trees)
