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
    return 0 <= row + d_row < len(platform) \
        and 0 <= col + d_col < len(platform[row + d_row])


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
        platform[new_row][new_col], platform[old_row][old_col] = \
            platform[old_row][old_col], platform[new_row][new_col]
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


def cycle(platform):
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for direction in directions:
        rocks = find_rocks(platform)
        rocks = sort_rocks(rocks, direction)
        for rock in rocks:
            platform = tilt_rock(platform, rock, direction)
    return platform


def to_str(platform):
    return '\n'.join([''.join(line) for line in platform])


def to_platform(string):
    return string.split('\n')


if __name__ == "__main__":
    platform = readlines('input_test.txt')
    seen_platform = to_str(platform)
    seen_platforms_set = {seen_platform}
    seen_platforms_list = [seen_platform]
    for i in range(1_000_000_000):
        platform = cycle(platform)
        seen_platform = to_str(platform)
        if to_str(platform) in seen_platforms_set:
            break
        seen_platforms_set.add(seen_platform)
        seen_platforms_list.append(seen_platform)
    start_of_cycle = seen_platforms_list.index(seen_platform)
    cycle_length = len(seen_platforms_list) - start_of_cycle
    index_of_final = ((1_000_000_000 - start_of_cycle) % cycle_length) \
        + start_of_cycle
    final_platform = to_platform(seen_platforms_list[index_of_final])
    print(total_load(final_platform))
