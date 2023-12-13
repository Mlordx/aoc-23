import sys
from collections import defaultdict

SPACE = defaultdict(lambda: '.')
DISTANCE = defaultdict(lambda: { 'H': 1, 'V': 1})
PLANETS = []

input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(input_file, 'r') as file:
    for i, line in enumerate(file):
        stripped_line = line.strip()
        for j, c in enumerate(stripped_line):
            SPACE[(i, j)] = c
            DISTANCE[(i, j)] = { 'H': 1, 'V': 1 }
            if c == '#':
                PLANETS.append((i, j))


HEIGHT = i+1
WIDTH = j+1

for i in range(HEIGHT):
    no_planets = True
    for j in range(WIDTH):
        if SPACE[(i, j)] != '.':
            no_planets = False

    if no_planets:
        for j in range(WIDTH):
            DISTANCE[(i, j)]['V'] = 2

for j in range(WIDTH):
    no_planets = True
    for i in range(HEIGHT):
        if SPACE[(i, j)] != '.':
            no_planets = False

    if no_planets:
        for i in range(HEIGHT):
            DISTANCE[(i, j)]['H'] = 2


def distance(p1, p2, part2=False):
    i1, j1 = p1
    i2, j2 = p2

    distance = 0
    pos = (i1, j1)

    if i1 < i2:
        while pos[0] <= i2:
            if pos == p1:
                pos = (pos[0]+1, pos[1])
                continue
            dist = DISTANCE[pos]['V']
            if dist == 2 and part2:
                dist = 1000000
            distance += dist
            pos = (pos[0]+1, pos[1])
        pos = (pos[0]-1, pos[1])

    if i1 > i2:
        while pos[0] >= i2:
            if pos == p1:
                pos = (pos[0]-1, pos[1])
                continue
            dist = DISTANCE[pos]['V']
            if dist == 2 and part2:
                dist = 1000000
            distance += dist
            pos = (pos[0]-1, pos[1])
        pos = (pos[0]+1, pos[1])


    if j1 < j2:
        if distance > 0: # I was counting the same node twice
            distance -= 1
        while pos[1] <= j2:
            if pos == p1:
                pos = (pos[0], pos[1]+1)
                continue
            dist = DISTANCE[pos]['H']
            if dist == 2 and part2:
                dist = 1000000
            distance += dist
            pos = (pos[0], pos[1]+1)

    if j1 > j2:
        if distance > 0: # I was counting the same node twice
            distance -= 1
        while pos[1] >= j2:
            if pos == p1:
                pos = (pos[0], pos[1]-1)
                continue
            dist = DISTANCE[pos]['H']
            if dist == 2 and part2:
                dist = 1000000
            distance += dist
            pos = (pos[0], pos[1]-1)


    return distance


def answer1():
    counted = set()
    answer = 0
    for i in range(len(PLANETS)):
        for j in range(len(PLANETS)):
            if i == j:
                continue

            if (i, j) in counted or (j, i) in counted:
                continue
            else :
                dist = distance(PLANETS[i], PLANETS[j])
                answer += dist
                counted.add((i, j))
                counted.add((j, i))

    return answer


def answer2():
    counted = set()
    answer = 0
    for i in range(len(PLANETS)):
        for j in range(len(PLANETS)):
            if i == j:
                continue

            if (i, j) in counted or (j, i) in counted:
                continue
            else :
                dist = distance(PLANETS[i], PLANETS[j], True)
                answer += dist
                counted.add((i, j))
                counted.add((j, i))

    return answer

print(answer1())
print(answer2())
