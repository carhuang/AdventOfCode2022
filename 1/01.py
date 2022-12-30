"""
Day 1: Calorie Counting
"""

# read the input
with open('./input.txt', 'r') as f:
    lines = f.readlines()
    rations = [entry.strip() for entry in lines]

def _parse(rations):
    calories_of_all_elves = []
    curr_calories = 0
    for item in rations:
        if item:
            curr_calories += int(item)
        else:
            calories_of_all_elves.append(curr_calories)
            curr_calories = 0
    calories_of_all_elves.append(curr_calories)
    return calories_of_all_elves

def part1():
    return max(_parse(rations))

def part2():
    calories = _parse(rations)
    calories.sort(reverse=True)
    top_three = calories[0] + calories[1] + calories[2]
    return top_three

print(part1())
print(part2())
    
