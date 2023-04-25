"""
Day 12: Hill Climbing Algorithm
"""

from collections import deque

# read the input
with open('./input.txt', 'r') as f:
    lines = f.readlines()
    map = [list(entry.strip()) for entry in lines]
num_rows = len(map)
num_cols = len(map[0])

def find_origin_and_destination():
    for row in range(num_rows):
        for col in range(num_cols):
            if map[row][col] == 'S':
                origin = (row, col)
                map[row][col] = 'a'
            elif map[row][col] == 'E':
                destination = (row, col)
                map[row][col] = 'z'
    return [origin, destination]

def get_neighbours(pos):
    row, col = pos
    delta_row = [-1, 0, 1, 0]
    delta_col = [0, 1, 0, -1]
    neighbours = []
    for i in range(len(delta_row)):
        neighbor_row = row + delta_row[i]
        neighbor_col = col + delta_col[i]
        if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
            if ord(map[neighbor_row][neighbor_col]) - ord(map[row][col]) <= 1:
                neighbours.append((neighbor_row, neighbor_col))
    return neighbours

def bfs(origin, destination):
    queue = deque([origin])
    visited = set()
    steps = 0
    while len(queue) > 0:
        n = len(queue)
        for _ in range(n):
            pos = queue.popleft()
            if pos == destination:
                return steps
            for neighbour in get_neighbours(pos):
                row, col = neighbour
                if neighbour in visited:
                    continue
                queue.append(neighbour)
                visited.add(neighbour)
        steps += 1
    return -1

def part1():
    origin, destination = find_origin_and_destination()
    # use BFS to find shortest path from origin to destination
    return bfs(origin, destination)

def find_origins_and_destination():
    origins = []
    for row in range(num_rows):
        for col in range(num_cols):
            if map[row][col] == 'S' or map[row][col] == 'a':
                origins.append((row, col))
                map[row][col] = 'a'
            elif map[row][col] == 'E':
                destination = (row, col)
                map[row][col] = 'z'
    return [origins, destination]

def part2():
    origins, destination = find_origins_and_destination()
    min_steps = float('inf')
    for origin in origins:
        steps = bfs(origin, destination)
        # check to see if there exists a path from current origin to destination
        if steps != -1:
            min_steps = min(steps, min_steps)
    return min_steps

# print(part1())
print(part2())