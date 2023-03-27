"""
Day 6: Tuning Trouble
"""

# read the input
with open('./input.txt', 'r') as f:
    datastream = f.readline()

def get_start_of_packet_marker():
    window = set()
    left = 0
    right = 0
    while right < len(datastream):
        if len(window) < 4:
            if datastream[right] in window:
                window.remove(datastream[left])
                left += 1
                right -= 1
            else:
                window.add(datastream[right])
                if len(window) == 4:
                    return right
        else:
            window.remove(datastream[left])
            left += 1
        right += 1
    return left

def part1():
    marker_idx = get_start_of_packet_marker()
    return marker_idx + 1

def get_start_of_message_marker():
    window = set()
    left = 0
    right = 0
    while right < len(datastream):
        if len(window) < 14:
            if datastream[right] in window:
                window.remove(datastream[left])
                left += 1
                right -= 1
            else:
                window.add(datastream[right])
                if len(window) == 14:
                    return right
        else:
            window.remove(datastream[left])
            left += 1
        right += 1
    return left

def part2():
    marker_idx = get_start_of_message_marker()
    return marker_idx + 1

print(part1())
print(part2())