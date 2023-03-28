"""
Day 10: Cathode-Ray Tube
"""

# read the input
with open('./input.txt', 'r') as f:
    lines = f.readlines()
    program = [entry.strip() for entry in lines]

class CPU:
    def __init__(self):
        self.cycle = 0
        self.x = 1
        self.v = 0
        self.pending = False
        self.sum_signal_strengths = 0
        self.crt_row = ''

    def execute_op(self, instruction):
        if instruction == 'noop':
            pass
        else:
            _, v = instruction.split()
            self.v = int(v)
            self.pending = True
    
    def execute_program(self, program):
        i = 0
        while i < len(program):
            instruction = program[i]
            self.cycle += 1
            self.draw_pixel()
            if (self.cycle - 20) % 40 == 0:
                signal_strength = self.get_signal_strength()
                self.sum_signal_strengths += signal_strength
            if self.pending:
                self.x += self.v
                self.pending = False
            else:
                self.execute_op(instruction)
                if self.pending: continue
            i += 1
        print(self.crt_row)
        return self.sum_signal_strengths

    def get_signal_strength(self):
        return self.cycle * self.x

    # part 2
    def draw_pixel(self):
        crt_pos = len(self.crt_row)
        if crt_pos > 39:
            print(self.crt_row)
            self.crt_row = ''
            crt_pos = 0
        if abs(crt_pos - self.x) <= 1:
            self.crt_row += '#'
        else:
            self.crt_row += '.'

def part1():
    cpu = CPU()
    return cpu.execute_program(program)

print(part1())