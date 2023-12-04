import sys

lines = []
games = []

input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(input_file, 'r') as file:
    for line in file:
        lines.append(line.strip('\n'))

    for l in lines:
        ll = l.split(':')
        rounds = ll[1].strip().split(';')
        new_game = []
        for round in rounds:
            cubes = round.strip().split(',')

            aux_round = [0, 0, 0]
            for cube in cubes:
                qty, color = cube.split()

                if color == 'red':
                    aux_round[0] += int(qty)
                elif color == 'green':
                    aux_round[1] += int(qty)
                elif color == 'blue':
                    aux_round[2] += int(qty)

            new_game.append(aux_round)
        games.append(new_game)


def answer1():
    total = 0
    for i, game in enumerate(games):
        id = i+1
        go_to_next_game = False
        for round in game:
            r = round[0]
            g = round[1]
            b = round[2]

            if r > 12 or g > 13 or b > 14:
                go_to_next_game = True
                break

        if go_to_next_game:
            continue
        else:
            total += id

    return total


def answer2():
    total = 0
    for _, game in enumerate(games):
        min_r = -1
        min_b = -1
        min_g = -1

        for round in game:
            r = round[0]
            g = round[1]
            b = round[2]

            min_r = max(min_r, r)
            min_g = max(min_g, g)
            min_b = max(min_b, b)


        total += min_r * min_g * min_b

    return total


print(answer1())
print(answer2())
