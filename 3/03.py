"""
Day 3: Rucksack Reorganization
"""

# read the input
with open('./input.txt', 'r') as f:
    lines = f.readlines()
    rucksacks = [entry.strip() for entry in lines]

def get_priority(item_type):
    if item_type.isupper():
        return ord(item_type) - 38
    else:
        return ord(item_type) - 96

def find_duplicate_item_type(rucksack):
    half_idx = len(rucksack) // 2
    first_compartment, second_compartment = rucksack[:half_idx], rucksack[half_idx:]
    first_set = set(first_compartment)
    for item_type in second_compartment:
        if item_type in first_set:
            return item_type

def part1():
    priorities_sum = 0
    for rucksack in rucksacks:
        item_type = find_duplicate_item_type(rucksack)
        priorities_sum += get_priority(item_type)
    return priorities_sum

def find_badge_in_group(elf1, elf2, elf3):
    set1 = set(elf1)
    set2 = set(elf2)
    set3 = set(elf3)
    # use pop() to retrieve the 1 item from the intersection set
    return set1.intersection(set2, set3).pop()

def part2():
    priorities_sum = 0
    for i in range(0, len(rucksacks), 3):
        badge = find_badge_in_group(rucksacks[i], rucksacks[i+1], rucksacks[i+2])
        priorities_sum += get_priority(badge)
    return priorities_sum

print(part1())
print(part2())
