number_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def readlines(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def line_starts_with_number(line):
    for key in number_dict.keys():
        if line.startswith(key):
            return True
    return False


def line_start_to_number(line):
    for key in number_dict.keys():
        if line.startswith(key):
            return number_dict[key]
    return -1


def line_starts_with_number(line):
    for key in number_dict.keys():
        if line.startswith(key):
            return True
    return False

def first_number_from_line(line):
    for i in range(len(line)):
        if line[i].isdigit():
            return int(line[i])
        if line_starts_with_number(line[i:]):
            return line_start_to_number(line[i:])
    return 0

def last_number_from_line(line):
    for i in range(-1, -1 - len(line), -1):
        if line[i].isdigit():
            return int(line[i])
        if line_starts_with_number(line[i:]):
            return line_start_to_number(line[i:])
    return 0

def number_from_line(line):
    first_number = first_number_from_line(line)
    last_number = last_number_from_line(line)
    return first_number * 10 + last_number

def sum_of_numbers(lines):
    total = 0
    for line in lines:
        total += number_from_line(line)
    return total

if __name__ == "__main__":
    lines = readlines('input_test2.txt')
    print(sum_of_numbers(lines))