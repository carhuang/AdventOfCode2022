"""
Day 14: Regolith Reservoir
"""

# read the input
with open('./input.txt', 'r') as f:
    lines = f.readlines()

# plot the cave map
rows, cols = 800, 1000
cave_map = [[0 for _ in range(cols)] for _ in range(rows)]
# track the boundaries of the rocks
rows_min, rows_max = 10000, -1
cols_min, cols_max = 10000, -1
# 0 is air, 1 is rock, -1 is sand
for line in lines:
    prev_x, prev_y = -1, -1
    coords = line.strip().split(" -> ")
    for coord in coords:
        coord = coord.split(",")
        x, y = int(coord[0]), int(coord[1])
        if prev_x == -1 and prev_y == -1:
            prev_x, prev_y = x, y
        elif prev_x == x:
            if y > prev_y:
                for row in range(prev_y, y+1):
                    cave_map[row][x] = 1
            else:
                for row in range(y, prev_y+1):
                    cave_map[row][x] = 1
            prev_y = y
        elif prev_y == y:
            if x > prev_x:
                for col in range(prev_x, x+1):
                    cave_map[y][col] = 1
            else:
                for col in range(x, prev_x+1):
                    cave_map[y][col] = 1
            prev_x = x
        # update map boundaries
        rows_min, rows_max = min(rows_min, y), max(rows_max, y)
        cols_min, cols_max = min(cols_min, x), max(cols_max, x)

# stimulates a single sand falling till rest, return false if sand falls into the abyss
def sand_falls():
    # sand oiriginates from 500, 0
    x, y = 500, 0
    while y <= rows_max:
        if cave_map[y+1][x] == 0:
            y += 1
        elif cave_map[y+1][x-1] == 0:
            y += 1
            x -= 1
        elif cave_map[y+1][x+1] == 0:
            y += 1
            x += 1
        else:
            cave_map[y][x] = -1
            return True
    return False

def part1():
    sand_count = 0
    while sand_falls():
        sand_count += 1
    return sand_count

def sand_falls_to_floor():
    x, y = 500, 0
    # floor is at rows_max + 2
    while y < rows_max + 1:
        if cave_map[y+1][x] == 0:
            y += 1
        elif cave_map[y+1][x-1] == 0:
            y += 1
            x -= 1
        elif cave_map[y+1][x+1] == 0:
            y += 1
            x += 1
        else:
            cave_map[y][x] = -1
            return
    cave_map[y][x] = -1

def part2():
    sand_count = 0
    while cave_map[0][500] == 0:
        sand_falls_to_floor()
        sand_count += 1
    return sand_count

# print(part1())
print(part2())