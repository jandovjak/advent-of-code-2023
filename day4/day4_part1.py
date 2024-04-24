def readlines(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines


def split_numbers(numbers):
    winning_numbers_string, hand_numbers_string = numbers.split('|')
    winning_numbers = [int(number) for number
                       in winning_numbers_string.split(' ') if number]
    hand_numbers = [int(number) for number
                    in hand_numbers_string.split(' ') if number]
    return set(winning_numbers), set(hand_numbers)


def points_in_game(line):
    _, numbers = line.split(':')
    winning_numbers, hand_numbers = split_numbers(numbers)
    matches = len(winning_numbers.intersection(hand_numbers))
    if matches == 0:
        return 0
    return 2 ** (matches - 1)


if __name__ == "__main__":
    lines = readlines('input_test.txt')
    points = 0
    for line in lines:
        points += points_in_game(line)
    print(points)
