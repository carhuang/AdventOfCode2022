"""
Day 2: Rock Paper Scissors
"""

# read the input
with open('./input.txt', 'r') as f:
    lines = f.readlines()
    strategy_guide = [entry.strip() for entry in lines]

def get_round_score(strategy):
    opponent = strategy[0]
    me = strategy[2]
    def get_shape_score():
        if me == 'X': return 1
        elif me == 'Y': return 2
        elif me == 'Z': return 3
    def get_outcome_score():
        win_score = 6
        draw_score = 3
        lose_score = 0
        if opponent == 'A':
            if me == 'X': return draw_score
            if me == 'Y': return win_score
        elif opponent == 'B':
            if me == 'Y': return draw_score
            if me == 'Z': return win_score
        elif opponent == 'C':
            if me == 'Z': return draw_score
            if me == 'X': return win_score
        return lose_score
    return get_shape_score() + get_outcome_score()

def get_round_score2(strategy):
    opponent = strategy[0]
    outcome = strategy[2]
    shape_score = { 'A': 1, 'B': 2, 'C': 3 }
    # outcome is a lose
    if outcome == 'X': 
        if opponent == 'A': return shape_score['C']
        else: return shape_score[opponent] - 1
    # outcome is a draw
    elif outcome == 'Y': return 3 + shape_score[opponent]
    # outcome is a win
    elif outcome == 'Z': 
        if opponent == 'C': return 6 + shape_score['A']
        else: return 6 + shape_score[opponent] + 1

def get_total_score(strategy_guide, version):
    total_score = 0
    for strategy in strategy_guide:
        if version == 1:
            total_score += get_round_score(strategy)
        elif version == 2:
            total_score += get_round_score2(strategy)
    return total_score

def part1():
    return get_total_score(strategy_guide, 1)

def part2():
    return get_total_score(strategy_guide, 2)

print(part1())
print(part2())