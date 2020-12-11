from copy import deepcopy

with open("11.txt") as file_obj:
    grid = [list(line.strip()) for line in file_obj.readlines()]

ROWS = len(grid)
COLS = len(grid[0])

def iterate_seat(old_grid, row, col):
    current = old_grid[row][col]
    if current == ".":
        return (".", False)
    num_populated = 0

    start_row = max(0, row-1)
    end_row = min(ROWS, row+2)
    start_col = max(0, col-1)
    end_col = min(COLS, col+2)

    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if (row == r and col == c):
                continue
            if old_grid[r][c] == "#":
                num_populated += 1

    if current == "L" and num_populated == 0:
        return ("#", True)
    if current == "#" and num_populated >= 4:
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
