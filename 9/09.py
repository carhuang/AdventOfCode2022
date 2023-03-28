"""
Day 9: Rope Bridge
"""

# read the input
with open('./input.txt', 'r') as f:
    lines = f.readlines()
    motions = [entry.strip() for entry in lines]

def is_neighbor(head, tail):
    return abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1

def move_tail(head, tail):
    if is_neighbor(head, tail):
        return None
    else:
        if head[0] == tail[0]:
            diff = 1 if head[1] > tail[1] else -1
            return (tail[0], tail[1] + diff)
        elif head[1] == tail[1]:
            diff = 1 if head[0] > tail[0] else -1
            return (tail[0] + diff, tail[1])
        else:
            delta_x = 1 if head[0] > tail[0] else -1
            delta_y = 1 if head[1] > tail[1] else -1
            return (tail[0] + delta_x, tail[1] + delta_y)
            
def part1():
    head = [0, 0]
    tail = (0, 0)
    visited_pos = set()
    visited_pos.add(tail)
    for motion in motions:
        direction, steps = motion.split()[0], int(motion.split()[1])
        while steps > 0:
            if direction == 'R':
                head[0] += 1
            elif direction == 'L':
                head[0] -= 1
            elif direction == 'U':
                head[1] += 1
            elif direction == 'D':
                head[1] -= 1
            steps -= 1
            new_tail = move_tail(head, tail)
            if new_tail:
                visited_pos.add(new_tail)
                tail = new_tail
    return len(visited_pos)

def part2():
    visited_pos = set()
    rope = [[0, 0] for _ in range(10)]
    head = rope[0]
    tail = rope[-1]
    visited_pos.add((tail[0], tail[1]))
    for motion in motions:
        direction, steps = motion.split()[0], int(motion.split()[1])
        while steps > 0:
            if direction == 'R':
                head[0] += 1
            elif direction == 'L':
                head[0] -= 1
            elif direction == 'U':
                head[1] += 1
            elif direction == 'D':
                head[1] -= 1
            steps -= 1
            for i in range(1, len(rope)):
                knot = rope[i]
                new_knot = move_tail(rope[i - 1], knot)
                if new_knot:
                    knot[0] = new_knot[0]
                    knot[1] = new_knot[1]
            visited_pos.add((tail[0], tail[1]))
    return len(visited_pos)

print(part1())
print(part2())