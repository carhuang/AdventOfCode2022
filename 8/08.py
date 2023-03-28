"""
Day 8: Treetop Tree House
"""

# read the input
with open('./input.txt', 'r') as f:
    lines = f.readlines()
    grid = []
    for i in range(len(lines)):
        line = lines[i].strip()
        row = []
        for tree in line:
            row.append(int(tree))
        grid.append(row)
num_rows = len(grid)
num_cols = len(grid[0])

def part1():
    visible_trees_num = 0 

    # build a grid that marks all the visible trees
    visible_grid = [[False] * num_cols for _ in range(num_rows)]
    # mark all trees in top and bottom rows as visible
    for c in range(num_cols):
        visible_grid[0][c] = True
        visible_grid[-1][c] = True
        visible_trees_num += 2
    # mark all trees in right-most and left-most columns as visible
    for r in range(1, num_rows - 1):
        visible_grid[r][0] = True
        visible_grid[r][-1] = True
        visible_trees_num += 2

    # check if trees are visible from the top and right
    max_height_top = grid[0].copy()
    for r in range(1, num_rows - 1):
        row = grid[r]
        max_height_right = row[0]
        for c in range(1, num_cols - 1):
            # check if tree is visible from top
            if row[c] > max_height_top[c]:
                max_height_top[c] = row[c]
                visible_grid[r][c] = True
                visible_trees_num += 1
            # check if tree is visible from right
            if row[c] > max_height_right:
                max_height_right = row[c]
                if not visible_grid[r][c]:
                    visible_grid[r][c] = True
                    visible_trees_num += 1

    # check if trees are visible from the bottom and left
    max_height_bottom = grid[-1].copy()
    for r in range(num_rows - 2, 0, -1):
        row = grid[r]
        max_height_left = row[-1]
        for c in range(num_cols - 2, 0, -1):
            # check if tree is visible from bottom
            if row[c] > max_height_bottom[c]:
                max_height_bottom[c] = row[c]
                if not visible_grid[r][c]:
                    visible_grid[r][c] = True
                    visible_trees_num += 1
            # check if tree is visible from left
            if row[c] > max_height_left:
                max_height_left = row[c]
                if not visible_grid[r][c]:
                    visible_grid[r][c] = True
                    visible_trees_num += 1

    return visible_trees_num

def get_up_viewing_distance(r, c):
    tree_height = grid[r][c]
    r_pos = r - 1
    while r_pos > 0 and tree_height > grid[r_pos][c]:
        r_pos -= 1
    return r - r_pos

def get_down_viewing_distance(r, c):
    tree_height = grid[r][c]
    r_pos = r + 1
    while r_pos < num_rows-1 and tree_height > grid[r_pos][c]:
        r_pos += 1
    return r_pos - r

def get_left_viewing_distance(r, c):
    tree_height = grid[r][c]
    c_pos = c - 1
    while c_pos > 0 and tree_height > grid[r][c_pos]:
        c_pos -= 1
    return c - c_pos

def get_right_viewing_distance(r, c):
    tree_height = grid[r][c]
    c_pos = c + 1
    while c_pos < num_cols-1 and tree_height > grid[r][c_pos]:
        c_pos += 1
    return c_pos - c

def part2():
    max_scenic_score = 0
    # skip the trees on the outer edges since they will have 0 score
    for r in range(1, num_rows - 1):
        for c in range(1, num_cols - 1):
            up_dis = get_up_viewing_distance(r, c)
            down_dis = get_down_viewing_distance(r, c)
            left_dis = get_left_viewing_distance(r, c)
            right_dis = get_right_viewing_distance(r, c)
            score = up_dis * down_dis * left_dis * right_dis
            max_scenic_score = max(score, max_scenic_score)
    return max_scenic_score

print(part1())
print(part2())