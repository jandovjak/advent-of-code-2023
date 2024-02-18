def readlines(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def is_in_range(i, j, delta_i, delta_j, height, width):
    return 0 <= i + delta_i < height and 0 <= j + delta_j < width

def generate_neighbours(i, j, height, width):
    neighbours = []
    for delta_i in [-1, 0, 1]:
        for delta_j in [-1, 0, 1]:
            if is_in_range(i, j, delta_i, delta_j, height, width) \
                and (delta_i != 0 or delta_j != 0):
                neighbours.append((i + delta_i, j + delta_j))
    return neighbours

def is_symbol(character):
    return character != '.' and not character.isdigit()

def has_adjacent_symbol(lines, i, j, height, width):
    has_adjacent_symbol = False
    neighbours = generate_neighbours(i, j, height, width)
    for neighbour_i, neighbour_j in neighbours:
        has_adjacent_symbol = has_adjacent_symbol or is_symbol(lines[neighbour_i][neighbour_j])
    return has_adjacent_symbol

def is_period(character):
    return character == '.'

def is_last_in_line(j, width):
    return j == width - 1

def part_numbers(lines):
    total = 0
    height = len(lines)
    width = len(lines[0])
    for i in range(height):
        in_number = False
        current_number = ''
        adjacent_symbol_to_number = False
        for j in range(width):
            character = lines[i][j]
            if character.isdigit():
                in_number = True
                current_number += character
            if is_period(character) or is_symbol(character) or is_last_in_line(j, width):
                if in_number and adjacent_symbol_to_number:
                    total += int(current_number)
                current_number = ''
                in_number = False
                adjacent_symbol_to_number = False
            if in_number and has_adjacent_symbol(lines, i, j, height, width):
                adjacent_symbol_to_number = True
    return total
                    
if __name__ == "__main__":
    a = int('')
    lines = readlines('input_test.txt')
    total = part_numbers(lines)
    print(total)