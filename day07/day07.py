import sys
from collections import Counter
from functools import cmp_to_key



hands = []

input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(input_file, 'r') as file:
    for line in file:
        stripped_line = line.strip('\n')
        hand, bid = stripped_line.split(' ')
        hands.append((hand, int(bid)))


suits_strength = {
    '2': 0,
    '3': 1,
    '4': 2,
    '5': 3,
    '6': 4,
    '7': 5,
    '8': 6,
    '9': 7,
    'T': 8,
    'J': 9,
    'Q': 10,
    'K': 11,
    'A': 12
}

suits_strength2 = {
    'J': -1,
    '2': 0,
    '3': 1,
    '4': 2,
    '5': 3,
    '6': 4,
    '7': 5,
    '8': 6,
    '9': 7,
    'T': 8,
    'Q': 10,
    'K': 11,
    'A': 12
}

part2 = False

def determine_hand_strength(hand):
    global part2
    c = dict(Counter(hand))
    if len(c) == 1: # Five of a kind
        return 6

    number_of_jokers = 0

    if 'J' in c:
        number_of_jokers = c['J']

    number_of_pairs = 0
    has_three_of_same = False

    if (part2 and number_of_jokers == 0) or not part2:
        if len(c) == 5: #High card
            return 0

        for char in c:
            if c[char] == 4:
                return 5

            if c[char] == 2:
                number_of_pairs += 1

            if c[char] == 3:
                has_three_of_same = True

        if has_three_of_same and number_of_pairs == 1:
            return 4

        if has_three_of_same and number_of_pairs == 0:
            return 3

        if not has_three_of_same and number_of_pairs == 2:
            return 2

        if not has_three_of_same and number_of_pairs == 1:
            return 1
    else:
        if len(c) == 5:
            return 1 # now has a pair

        for char in c:
            if char == 'J':
                continue

            if c[char] == 4:
                return 6 # became a five of a kind

            if c[char] == 2:
                number_of_pairs += 1

            if c[char] == 3:
                has_three_of_same = True

        if has_three_of_same:
            if number_of_jokers == 1:
                return 5 # became four of a kind
            else:
                return 6 # became a five of a kind

        if number_of_pairs == 1:
            if number_of_jokers == 3:
                return 6 # became a five of a kind
            if number_of_jokers == 2:
                return 5 # became a four of a kind
            if number_of_jokers == 1:
                return 3 # became a three of a kind

        if number_of_pairs == 2:
            return 4 # became a full house

        if number_of_jokers == 1:
            return 1 # became a one pair

        if number_of_jokers == 2:
            return 3 # became a three of a kind

        if number_of_jokers == 3:
            return 5 # became a four of a kind

        if number_of_jokers == 4:
            return 6 # became a five of a kind

def compare_same_hand(hand1, hand2):
    global part2
    for i in range(len(hand1)):
        c1, c2 = hand1[i], hand2[i]
        strength = suits_strength2 if part2 else suits_strength
        diff = strength[c1] - strength[c2]

        if diff != 0:
            return diff

    return 0


def compare_hands(hand1, hand2):
    val1 = determine_hand_strength(hand1[0])
    val2 = determine_hand_strength(hand2[0])

    if val1 != val2:
        return val1 - val2

    return compare_same_hand(hand1[0], hand2[0])


def answer1():
    sorted_hands = sorted(hands, key=cmp_to_key(compare_hands))

    answer = 0
    for i, hand in enumerate(sorted_hands):
        answer += (i+1) * hand[1]

    return answer


def answer2():
    global part2
    part2 = True

    sorted_hands = sorted(hands, key=cmp_to_key(compare_hands))

    answer = 0
    for i, hand in enumerate(sorted_hands):
        answer += (i+1) * hand[1]

    return answer


print(answer1())
print(answer2())
