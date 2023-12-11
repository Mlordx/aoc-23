import sys
from collections import defaultdict
from math import gcd

lines = []
input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(input_file, 'r') as file:
    for line in file:
        stripped_line = line.strip('\n')
        lines.append(stripped_line)

map = defaultdict()

for line in lines[2:]:
    origin, dest = line.split('=')
    origin = origin.strip()
    l, r = dest.replace('(', '').replace(')', '').replace(',', '').strip().split(' ')
    map[origin] = (l, r)


def answer1():
    current_node = 'AAA'
    steps = 0

    moves = lines[0].strip()
    current_move = 0

    while current_node != 'ZZZ':
        index = 0 if moves[current_move] == 'L' else 1
        next_node = map[current_node][index]
        steps += 1
        current_node = next_node
        current_move = (current_move + 1) % len(moves)

    return steps


def lcm(a, b):
    return (a * b) // gcd(a, b)


def answer2():
    starts = []
    steps = []

    for key in map:
        if key[-1] == 'A':
            starts.append(key)

    for start in starts:
        current_node = start
        steps_aux = 0

        moves = lines[0].strip()
        current_move = 0

        while current_node[-1] != 'Z':
            index = 0 if moves[current_move] == 'L' else 1
            next_node = map[current_node][index]
            steps_aux += 1
            current_node = next_node
            current_move = (current_move + 1) % len(moves)

        steps.append(steps_aux)

    answer = steps[0]

    for step in steps[1:]:
        answer = lcm(answer, step)

    return answer


print(answer1())
print(answer2())
