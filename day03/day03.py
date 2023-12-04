import sys
from collections import defaultdict
from functools import reduce

GRID = defaultdict(lambda: '.')
GEARS = dict()

input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(input_file, 'r') as file:
    for i, line in enumerate(file):
        stripped_line = line.strip()
        for j, c in enumerate(stripped_line):
            GRID[(i, j)] = c

            if c == '*':
                GEARS[(i, j)] = []

HEIGHT = i
WIDTH = j

def answer1():
    total = 0
    i = 0
    j = 0

    while i <= HEIGHT:
        j = 0
        while j <= WIDTH:
            if GRID[(i, j)] in '0123456789':
                num = GRID[(i, j)]
                j_aux = j+1

                while j_aux <= WIDTH:
                    if GRID[(i, j_aux)] in '0123456789':
                        num += GRID[(i, j_aux)]
                    else:
                        break
                    j_aux += 1


                for k in range(j, j_aux):
                    added = False
                    adjacents = [
                        (0, -1), (0, +1), (-1, 0), (+1, 0), (-1, -1), (+1, -1), (-1, +1), (+1, +1)
                    ]

                    for adj in adjacents:
                        x_off, y_off = adj
                        pos = GRID[(i + x_off, k + y_off)]

                        if pos not in '.0123456789':
                            total += int(num)
                            added = True
                            break

                    if added:
                        break

                j = j_aux
            else:
                j += 1

        i += 1

    return total


def answer2():
    total = 0
    i = 0
    j = 0

    while i <= HEIGHT:
        j = 0
        while j <= WIDTH:
            if GRID[(i, j)] in '0123456789':
                num = GRID[(i, j)]
                j_aux = j+1

                while j_aux <= WIDTH:
                    if GRID[(i, j_aux)] in '0123456789':
                        num += GRID[(i, j_aux)]
                    else:
                        break
                    j_aux += 1


                for k in range(j, j_aux):
                    added = False
                    adjacents = [
                        (0, -1), (0, +1), (-1, 0), (+1, 0), (-1, -1), (+1, -1), (-1, +1), (+1, +1)
                    ]

                    for adj in adjacents:
                        x_off, y_off = adj
                        pos = (i + x_off, k + y_off)

                        if GRID[pos] == '*':
                            GEARS[pos].append(int(num))
                            added = True
                            break

                    if added:
                        break

                j = j_aux
            else:
                j += 1

        i += 1

    for GEAR in GEARS:
        if len(GEARS[GEAR]) == 2:
            total += reduce(lambda x, y: x * y, GEARS[GEAR])

    return total


print(answer1())
print(answer2())
