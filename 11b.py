from copy import deepcopy
from itertools import permutations

with open("11.txt") as file_obj:
    grid = [list(line.strip()) for line in file_obj.readlines()]

ROWS = len(grid)
COLS = len(grid[0])

MAX_DIST = ROWS + COLS  # It's less than this, but just to loop neatly

GRADIENTS = [
    (-1, -1), (-1, 0), (-1, 1), (0, 1),
    (1, 1), (1, 0), (1, -1), (0, -1)
]

def iterate_seat(old_grid, row, col):
    current = old_grid[row][col]
    if current == ".":
        return (".", False)
    num_populated = 0

    for row_grad, col_grad in GRADIENTS:
        for distance in range(1, MAX_DIST):
            new_row = row + (row_grad * distance)
            new_col = col + (col_grad * distance)

            if not ((0 <= new_row < ROWS) and (0 <= new_col < COLS)):
                break
            target = old_grid[new_row][new_col]
            if target == "L":
                break
            if target == "#":
                num_populated += 1
                break

    if current == "L" and num_populated == 0:
        return ("#", True)
    if current == "#" and num_populated >= 5:
        return ("L", True)
    return (current, False)


iteration = 0
while True:
    iteration += 1
    new_grid = [[None for col in range(COLS)] for row in range(ROWS)]
    changed = False
    for row in range(ROWS):
        for col in range(COLS):
            new_seat, changed_here = iterate_seat(grid, row, col)
            changed = (changed or changed_here)
            new_grid[row][col] = new_seat

    if not changed:
        break

    grid = new_grid

def num_occupied(row):
    return row.count("#")

result = sum(num_occupied(row) for row in grid)
print("Iterations:", iteration)
print(result)
