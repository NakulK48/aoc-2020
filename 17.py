with open("17.txt") as file_obj:
    lines = [line.strip() for line in file_obj.readlines()]

ITERATIONS = 6

initial_side_length = len(lines)

XY_LENGTH = initial_side_length + (ITERATIONS * 2)
Z_LENGTH =  1 + (ITERATIONS * 2)

XY_START = ITERATIONS
Z_START = Z_LENGTH // 2

def build_cube():
    return [
        [
            [0 for _ in range(Z_LENGTH)]
            for __ in range(XY_LENGTH)
        ]
        for ___ in range(XY_LENGTH) 
    ]

cube = build_cube()

for x, line in enumerate(lines):
    for y, value in enumerate(line):
        if value == "#":
            cube[x + XY_START][y + XY_START][Z_START] = 1

def iterate_cell(cube, x, y, z):
    active_neighbours = 0
    original = cube[x][y][z]
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                if (i, j, k) == (x, y, z):
                    continue
                try:
                    neighbour = cube[i][j][k]
                except IndexError:
                    continue
                if neighbour:
                    active_neighbours += 1
    if original:
        return (1 if active_neighbours in (2, 3) else 0)
    return (1 if active_neighbours == 3 else 0)

ITERATIONS = 6

for iteration in range(ITERATIONS):
    print("ITERATION", iteration+1)
    new_cube = build_cube()
    total_active = 0
    for x in range(XY_LENGTH):
        for y in range(XY_LENGTH):
            for z in range(Z_LENGTH):
                new_cell = iterate_cell(cube, x, y, z)
                total_active += new_cell
                new_cube[x][y][z] = new_cell
    cube = new_cube

print(total_active)
