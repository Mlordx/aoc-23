import sys

lines = []

input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(input_file, 'r') as file:
    for line in file:
        lines.append(line.strip('\n'))

def answer1():
    answer = 0
    for line in lines:
        n1 = n2 = None
        for c1, c2 in zip(line, line[::-1]):
            if n1 is None and c1 in '0123456789':
                n1 = c1

            if n2 is None and c2 in '0123456789':
                n2 = c2

        answer += int(n1+n2)

    return answer

numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def answer2():
    answer = 0
    for line in lines:
        n1 = n2 = None

        for i, j in zip(range(len(line)), range(len(line)-1,-1, -1)):
            c1 = line[i]
            c2 = line[j]

            if n1 is None:
                if c1 in '0123456789':
                    n1 = c1

                for number in numbers:
                    length = len(number)
                    if line.find(number, i, i+length) != -1:
                        n1 = numbers[number]
                        break

            if n2 is None:
                if c2 in '0123456789':
                    n2 = c2

                for number in numbers:
                    length = len(number)
                    if line.find(number, j - length +1, j+1) != -1:
                        n2 = numbers[number]
                        break

        answer += int(n1+n2)


    return answer

print(answer1())
print(answer2())
