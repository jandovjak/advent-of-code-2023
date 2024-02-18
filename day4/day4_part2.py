def readlines(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def split_numbers(numbers):
    winning_numbers_string, hand_numbers_string = numbers.split('|')
    winning_numbers = [int(number) for number in winning_numbers_string.split(' ') if number]
    hand_numbers = [int(number) for number in hand_numbers_string.split(' ') if number]
    return set(winning_numbers), set(hand_numbers)

def points_in_game(line):
    _, numbers = line.split(':')
    winning_numbers, hand_numbers = split_numbers(numbers)
    return len(winning_numbers.intersection(hand_numbers))

def update_copies(copies, start, end, points):
    for i in range(start, end + 1):
        copies[i] += points
    return copies

if __name__ == "__main__":
    lines = readlines('input_test.txt')
    copies = [1] * len(lines)
    for i in range(len(lines)):
        points = points_in_game(lines[i])
        copies_of_card = copies[i]
        copies = update_copies(copies, i + 1, i + points, copies_of_card)
    total = sum(copies)
    print(total)