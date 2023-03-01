"""
Day 4: Camp Cleanup
"""

# read the input
with open('./input.txt', 'r') as f:
    lines = f.readlines()
    assignment_pairs = [entry.strip() for entry in lines]

def pair_fully_contained(pair):
    ass1, ass2 = pair.split(',')
    ass1_range, ass2_range = ass1.split('-'), ass2.split('-')
    ass1_start, ass1_end = int(ass1_range[0]), int(ass1_range[1])
    ass2_start, ass2_end = int(ass2_range[0]), int(ass2_range[1])
    if ass1_end == ass2_end:
        return True
    elif ass1_end > ass2_end:
        if ass1_start <= ass2_start:
            return True
    else:
        if ass1_start >= ass2_start:
            return True
    return False

def part1():
    num_fully_contained_pairs = 0
    for pair in assignment_pairs:
        if pair_fully_contained(pair):
            num_fully_contained_pairs += 1
    return num_fully_contained_pairs

def pair_overlaps(pair):
    ass1, ass2 = pair.split(',')
    ass1_range, ass2_range = ass1.split('-'), ass2.split('-')
    ass1_start, ass1_end = int(ass1_range[0]), int(ass1_range[1])
    ass2_start, ass2_end = int(ass2_range[0]), int(ass2_range[1])
    return not(ass1_end < ass2_start or ass1_start > ass2_end)

def part2():
    num_overlap_pairs = 0
    for pair in assignment_pairs:
        if pair_overlaps(pair):
            num_overlap_pairs += 1
    return num_overlap_pairs

print(part1())
print(part2())