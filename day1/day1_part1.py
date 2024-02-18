def readlines(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def first_number_from_line(line):
    for character in line:
        if character.isdigit():
            return character
    return '0'

def last_number_from_line(line):
    for character in reversed(line):
        if character.isdigit():
            return character
    return '0'

def number_from_line(line):
    first_number = first_number_from_line(line)
    last_number = last_number_from_line(line)
    return int(first_number + last_number)

def sum_of_numbers(lines):
    total = 0
    for line in lines:
        total += number_from_line(line)
    return total

if __name__ == "__main__":
    lines = readlines('input_test.txt')
    print(sum_of_numbers(lines))