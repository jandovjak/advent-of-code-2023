def readlines(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def left_numbers(lines, i, j):
    number = ''
    while j >= 0 and lines[i][j].isdigit():
        number = lines[i][j] + number
        j -= 1
    return number

def right_numbers(lines, i, j, width):
    number = ''
    while j < width and lines[i][j].isdigit():
        number += lines[i][j]
        j += 1
    return number

def append_number(numbers, number):
    if number != '':
        numbers.append(int(number))
    return numbers

def line_number_neighbours(lines, i, j, width):
    left_number = left_numbers(lines, i, j - 1)
    right_number = right_numbers(lines, i, j + 1, width)
    numbers = []
    if lines[i][j].isdigit():
        new_number = left_number + lines[i][j] + right_number
        numbers = append_number(numbers, new_number)
    else:
        numbers = append_number(numbers, left_number)
        numbers = append_number(numbers, right_number)
    return numbers
    
def gear_ratio(lines, i, j, height, width):
    number_neighbours = []
    for delta_i in [-1, 0, 1]:
        number_neighbours += line_number_neighbours(lines, i + delta_i, j, width)
    if len(number_neighbours) == 2:
        return number_neighbours[0] * number_neighbours[1]
    return 0

def is_star(character):
    return character == '*'

def total_gear_ratio(lines):
    total = 0
    height = len(lines)
    width = len(lines[0])
    for i in range(height):
        for j in range(width):
            character = lines[i][j]
            if is_star(character):
                total += gear_ratio(lines, i, j, height, width)
    return total
                    
if __name__ == "__main__":
    lines = readlines('input_test.txt')
    total = total_gear_ratio(lines)
    print(total)