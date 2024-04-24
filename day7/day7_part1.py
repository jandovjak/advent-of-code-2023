from functools import cmp_to_key

CARDS = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

FIVE_OF_A_KIND = 7
FOUR_OF_A_KIND = 6
FULL_HOUSE = 5
THREE_OF_A_KIND = 4
TWO_PAIRS = 3
ONE_PAIR = 2
HIGH_CARD = 1


def readlines(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines


def type(hand):
    counts = [hand.count(card) for card in CARDS.keys()]
    if 5 in counts:
        return FIVE_OF_A_KIND
    if 4 in counts:
        return FOUR_OF_A_KIND
    if 3 in counts and 2 in counts:
        return FULL_HOUSE
    if 3 in counts:
        return THREE_OF_A_KIND
    if counts.count(2) == 2:
        return TWO_PAIRS
    if 2 in counts:
        return ONE_PAIR
    return HIGH_CARD


def compare_hands(first, second):
    first_hand, first_type, _ = first
    second_hand, second_type, _ = second
    if first_type != second_type:
        return first_type - second_type
    for i in range(len(first_hand)):
        if CARDS[first_hand[i]] != CARDS[second_hand[i]]:
            return CARDS[first_hand[i]] - CARDS[second_hand[i]]
    return 0


if __name__ == "__main__":
    lines = readlines('input_test.txt')
    total = 0
    hands = []
    for line in lines:
        hand, bid = line.split(' ')
        type_of_hand = type(hand)
        hands.append((hand, type_of_hand, bid))
    hands.sort(key=cmp_to_key(compare_hands))
    for index, (_, _, bid) in enumerate(hands):
        total += (index + 1) * int(bid)
    print(total)
