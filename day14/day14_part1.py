def readlines(filename):
    with open(filename, 'r') as file:
        lines = [list(line.strip()) for line in file.readlines()]
    return lines

def find_rocks(platform):
    rocks = []
    for i in range(len(platform)):
        for j in range(len(platform[i])):
            if platform[i][j] == 'O':
                rocks.append((i, j))
    return rocks

def sort_rocks(rocks, direction):
    if direction == (-1, 0):
        return sorted(rocks, key=lambda rock: (rock[0], rock[1]))
    if direction == (1, 0):
        return sorted(rocks, key=lambda rock: (rock[0], rock[1]), reverse=True)
    if direction == (0, -1):
        return sorted(rocks, key=lambda rock: (rock[1], rock[0]))
    if direction == (0, 1):
        return sorted(rocks, key=lambda rock: (rock[1], rock[0]), reverse=True)
    return rocks

def is_tilt_in_platform(platform, position, direction):
    row, col = position
    d_row, d_col = direction
    return 0 <= row + d_row < len(platform) and 0 <= col + d_col < len(platform[row + d_row])

def new_position(position, direction):
    row, col = position
    d_row, d_col = direction
    return row + d_row, col + d_col

def is_empty_space(platform, row, col):
    return platform[row][col] == '.'

def can_tilt(platform, position, direction):
    if not is_tilt_in_platform(platform, position, direction):
        return False
    new_row, new_col = new_position(position, direction)
    return is_empty_space(platform, new_row, new_col)
    
def tilt_rock(platform, rock, direction):
    while can_tilt(platform, rock, direction):
        old_row, old_col = rock
        new_row, new_col = new_position(rock, direction)
        platform[new_row][new_col], platform[old_row][old_col] =  platform[old_row][old_col], platform[new_row][new_col]
        rock = (new_row, new_col)
    return platform

def total_load(platform):
    total_load = 0
    height = len(platform)
    for i in range(len(platform)):
        for j in range(len(platform[i])):
            if platform[i][j] == 'O':
                total_load += height - i
    return total_load

if __name__ == "__main__":
    platform = readlines('input_test.txt')
    rocks = find_rocks(platform)
    direction = (-1, 0)
    rocks = sort_rocks(rocks, direction)
    for rock in rocks:
        platform = tilt_rock(platform, rock, direction)
    print(total_load(platform))