import sys

sequences = []

input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(input_file, 'r') as file:
    for line in file:
        stripped_line = line.strip('\n')
        sequences.append([int(x) for x in stripped_line.split()])


def estimate_value(sequence, part2=False):
    subsequences = [sequence[::]]
    i = 0
    while True:
        subsequences.append([])
        number_of_zeroes = 0
        for j in range(len(subsequences[i])-1):
            diff = subsequences[i][j+1] - subsequences[i][j]
            if diff == 0:
                number_of_zeroes += 1
            subsequences[i+1].append(diff)

        if number_of_zeroes == len(subsequences[i+1]):
            break

        i += 1

    subsequences = subsequences[:-1] # remove all zeros
    subsequences = subsequences[::-1] # reverse

    for i in range(len(subsequences)-1):
        x = subsequences[i][-1]
        y = subsequences[i+1][-1]

        subsequences[i+1].append(x+y)
        x = subsequences[i][0]
        y = subsequences[i+1][0]
        subsequences[i+1].insert(0, y-x)

    return subsequences[-1][0] if part2 else subsequences[-1][-1]


def answer1():
    answer = 0
    for seq in sequences:
        answer += estimate_value(seq)

    return answer


def answer2():
    answer = 0
    for seq in sequences:
        answer += estimate_value(seq, True)

    return answer


print(answer1())
print(answer2())
