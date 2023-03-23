"""
Day 5: Supply Stacks

Starting Stacks
[D]                     [N] [F]    
[H] [F]             [L] [J] [H]    
[R] [H]             [F] [V] [G] [H]
[Z] [Q]         [Z] [W] [L] [J] [B]
[S] [W] [H]     [B] [H] [D] [C] [M]
[P] [R] [S] [G] [J] [J] [W] [Z] [V]
[W] [B] [V] [F] [G] [T] [T] [T] [P]
[Q] [V] [C] [H] [P] [Q] [Z] [D] [W]
 1   2   3   4   5   6   7   8   9 
"""

import re

starting_stacks = [[]]
starting_stacks.append(['Q','W','P','S','Z','R','H','D'])
starting_stacks.append(['V','B','R','W','Q','H','F'])
starting_stacks.append(['C','V','S','H'])
starting_stacks.append(['H','F','G'])
starting_stacks.append(['P','G','J','B','Z'])
starting_stacks.append(['Q','T','J','H','W','F','L'])
starting_stacks.append(['Z','T','W','D','L','V','J','N'])
starting_stacks.append(['D','T','Z','C','J','G','H','F'])
starting_stacks.append(['W','P','V','M','B','H'])

# read the input
with open('./input.txt', 'r') as f:
    lines = f.readlines()
    procedures = [entry.strip() for entry in lines]

def move(amount, origin, destination):
    for i in range(amount):        
        starting_stacks[destination].append(starting_stacks[origin].pop())

def part1():
    for procedure in procedures:
        data = re.findall("\d+", procedure)
        move(int(data[0]), int(data[1]), int(data[2]))
    # print out top crate of every stack
    for i in range(1, 10):
        print(starting_stacks[i][-1], end='')
    print()

def move_9001(amount, origin, destination):
    buffer = [0] * amount
    for i in range(amount):        
        buffer[amount - i - 1] = starting_stacks[origin].pop()
    starting_stacks[destination].extend(buffer)

def part2():
    for procedure in procedures:
        data = re.findall("\d+", procedure)
        move_9001(int(data[0]), int(data[1]), int(data[2]))
    # print out top crate of every stack
    for i in range(1, 10):
        print(starting_stacks[i][-1], end='')
    print()

# part1()
part2()




        