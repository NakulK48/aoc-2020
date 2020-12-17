with open("17.txt") as file_obj:
    lines = [line.strip() for line in file_obj.readlines()]

ITERATIONS = 6

SIDE_LENGTH = 21
MIDDLE = 11
THIRD = 7

def build_cube(side_length):
    return [
        [
            [[0 for _ in range(side_length)] for __ in range(side_length)]
            for ___ in range(side_length)
        ]
        for ____ in range(side_length) 
    ]

cube = build_cube(SIDE_LENGTH)

for x, line in enumerate(lines):
    for y, value in enumerate(line):
        if value == "#":
            cube[MIDDLE][MIDDLE][x + THIRD][y + THIRD] = 1


def iterate_cell(cube, x, y, z, w):
    active_neighbours = 0
    original = cube[x][y][z][w]
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                for m in range(w-1, w+2):
                    if (i, j, k, m) == (x, y, z, w):
                        continue
                    try:
                        neighbour = cube[i][j][k][m]
                    except IndexError:
                        continue
                    if neighbour:
                        active_neighbours += 1
    if original:
        return (1 if active_neighbours in (2, 3) else 0)
    return (1 if active_neighbours == 3 else 0)



for iteration in range(ITERATIONS):
    print("ITERATION", iteration+1)
    new_cube = build_cube(SIDE_LENGTH)
    total_active = 0
    for x in range(SIDE_LENGTH):
        for y in range(SIDE_LENGTH):
            for z in range(SIDE_LENGTH):
                for w in range(SIDE_LENGTH):
                    new_cell = iterate_cell(cube, x, y, z, w)
                    total_active += new_cell
                    new_cube[x][y][z][w] = new_cell
    cube = new_cube

print(total_active)