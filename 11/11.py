"""
Day 11: Monkey in the Middle
"""

from collections import deque

# read the input
with open('./input.txt', 'r') as f:
    lines = f.readlines()
    lines = [entry.strip() for entry in lines]

class Monkey:
    def __init__(self, data):
        _, starting_items_str = data[1].split(":")
        self.items = [int(item) for item in starting_items_str.split(', ')]
        self.operation = data[2].split('= ')[1]
        self.test = int(data[3].split('by ')[1])
        self.true_monkey = int(data[4].split('monkey ')[1])
        self.false_monkey = int(data[5].split('monkey ')[1])
        self.inspections = 0

    def inspects_items(self):
        for i in range(len(self.items)):
            self.inspections += 1
            old = self.items[i]
            self.items[i] = eval(self.operation)

    def gets_bored(self):
        for i in range(len(self.items)):
            self.items[i] //= 3

    def throws_items(self):
        pending_throws = []
        for item in self.items:
            if item % self.test == 0:
                pending_throws.append((item, self.true_monkey))
            else:
                pending_throws.append((item, self.false_monkey))
        self.items.clear()
        return pending_throws

    def receives_item(self, item):
        self.items.append(item)

    # part 2
    def manages_worry_level(self):
        for i in range(len(self.items)):
            self.items[i] %= PRODUCT  
            # PRODUCT is the product of all the monkey's divisibility test numbers


monkeys = []
PRODUCT = 1  # part 2
while len(lines) > 0:
    new_monkey = Monkey(lines)
    monkeys.append(new_monkey)
    PRODUCT *= new_monkey.test  # part 2
    lines = lines[7:] if len(lines) > 7 else []

def part1():
    for round in range(20):
        for monkey in monkeys:
            monkey.inspects_items()
            monkey.gets_bored()
            pending_throws = monkey.throws_items()
            for item, recipient in pending_throws:
                monkeys[recipient].receives_item(item)
    inspections = [monkey.inspections for monkey in monkeys]
    inspections.sort(reverse=True)
    return inspections[0] * inspections[1]

def part2():
    for round in range(10000):
        for monkey in monkeys:
            monkey.inspects_items()
            monkey.manages_worry_level()
            pending_throws = monkey.throws_items()
            for item, recipient in pending_throws:
                monkeys[recipient].receives_item(item)
    inspections = [monkey.inspections for monkey in monkeys]
    inspections.sort(reverse=True)
    return inspections[0] * inspections[1]

# print(part1())
print(part2())