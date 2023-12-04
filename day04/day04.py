import sys

lines = []
cards = []

input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(input_file, 'r') as file:
    for line in file:
        lines.append(line.strip('\n'))

    for l in lines:
        wins, have = l.split(':')[1].split('|')
        cards.append((set(wins.split()), set(have.split())))


def answer1():
    total = 0

    for card in cards:
        intersection = len(card[0].intersection(card[1]))
        total += 1 << (intersection - 1) if intersection > 0 else 0

    return total



def answer2():
    card_copies = [1 for _ in cards]

    for i, card in enumerate(cards):
        intersection = len(card[0].intersection(card[1]))
        if intersection > 0:
            for j in range(i+1, i+1+intersection):
                card_copies[j] += card_copies[i]

    return sum(card_copies)


print(answer1())
print(answer2())
