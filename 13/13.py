"""
Day 13: Distress Signal
"""

import functools

# read the input
with open('./input.txt', 'r') as f:
    lines = f.readlines()
    packets = []
    for i in range(len(lines)):
        if not lines[i].strip(): continue
        packet = eval(lines[i].strip())
        packets.append(packet)

# returns 1 if left packet is smaller, -1 if right packet is smaller, 0 if undecided
# 0 will not happen in the outermost loop
def compare(left_packet, right_packet):
    i = 0
    while i < len(left_packet) and i < len(right_packet):
        left = left_packet[i]
        right = right_packet[i]
        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return 1
            elif left > right:
                return -1
        elif isinstance(left, list) and isinstance(right, list):
            sub_result = compare(left, right)
            if sub_result != 0:
                return sub_result
        elif isinstance(left, int):
            sub_result = compare([left], right)
            if sub_result != 0:
                return sub_result
        else:
            sub_result = compare(left, [right])
            if sub_result != 0:
                return sub_result
        i += 1
    if len(left_packet) < len(right_packet):
        return 1
    elif len(right_packet) < len(left_packet):
        return -1
    else:
        return 0

def part1():
    indices_sum = 0
    idx = 1
    for i in range(0, len(packets), 2):
        if compare(packets[i], packets[i + 1]) == 1:
            indices_sum += idx
        idx += 1
    return indices_sum

def part2():
    packets.append([[2]])
    packets.append([[6]])
    packets.sort(reverse=True, key=functools.cmp_to_key(compare))
    decoder_key = 1
    for i in range(len(packets)):
        if packets[i] == [[2]] or packets[i] == [[6]]:
            decoder_key *= i + 1
    return decoder_key

# print(part1())
print(part2())