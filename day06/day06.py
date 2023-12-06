import sys

lines = []
targets = []

input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(input_file, 'r') as file:
    for line in file:
        lines.append(line.strip('\n'))

times = [int(time) for time in lines[0].split(':')[1].strip().split('   ')]
distances = [int(distance) for distance in lines[1].split(':')[1].strip().split('   ')]

for i in range(len(times)):
    targets.append((times[i], distances[i]))


def answer1():
    answer = 1
    for target in targets:
        number_of_wins = 0

        time, distance = target
        t = 0
        while t < time:
            total_distance = t * (time - t)

            if total_distance > distance:
                number_of_wins += 1
            t += 1

        answer *= number_of_wins
    return answer


def answer2():
    target_time =  int(''.join(map(str, times)))
    target_distance =  int(''.join(map(str, distances)))

    answer = 0

    t = 0
    while t < target_time:
        total_distance = t * (target_time - t)

        if total_distance > target_distance:
            answer += 1
        t += 1

    return answer


print(answer1())
print(answer2())
