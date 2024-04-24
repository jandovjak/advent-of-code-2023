TILE_DIRECTION = {
    '.': {
        (0, 1): [(0, 1)],
        (1, 0): [(1, 0)],
        (0, -1): [(0, -1)],
        (-1, 0): [(-1, 0)]
    },
    '/': {
        (0, 1): [(-1, 0)],
        (1, 0): [(0, -1)],
        (0, -1): [(1, 0)],
        (-1, 0): [(0, 1)]
    },
    '\\': {
        (0, 1): [(1, 0)],
        (1, 0): [(0, 1)],
        (0, -1): [(-1, 0)],
        (-1, 0): [(0, -1)]
    },
    '|': {
        (0, 1): [(-1, 0), (1, 0)],
        (1, 0): [(1, 0)],
        (0, -1): [(-1, 0), (1, 0)],
        (-1, 0): [(-1, 0)]
    },
    '-': {
        (0, 1): [(0, 1)],
        (1, 0): [(0, -1), (0, 1)],
        (0, -1): [(0, -1)],
        (-1, 0): [(0, -1), (0, 1)]
    }
}


def readlines(filename):
    with open(filename, 'r') as file:
        lines = [list(line.strip()) for line in file.readlines()]
    return lines


def is_in_grid(grid, position, direction):
    height = len(grid)
    width = len(grid[0])
    row, col = position
    d_row, d_col = direction
    return 0 <= row + d_row < height and 0 <= col + d_col < width


def get_next_positions(grid, position, direction):
    next_positions = []
    row, col = position
    tile = grid[row][col]
    for next_direction in TILE_DIRECTION[tile][direction]:
        if is_in_grid(grid, position, next_direction):
            next_d_row, next_d_col = next_direction
            next_positions.append(((row + next_d_row, col + next_d_col),
                                   (next_direction)))
    return next_positions


def energize_tiles(grid, start_position, start_direction):
    height = len(grid)
    width = len(grid[0])
    energized_tiles = [['.' for _ in range(width)] for _ in range(height)]
    beams_of_lights = [(start_position, start_direction)]
    visited_tiles = set(beams_of_lights)
    while beams_of_lights:
        position, direction = beams_of_lights.pop()
        visited_tiles.add((position, direction))
        row, col = position
        energized_tiles[row][col] = '#'
        for next_position in get_next_positions(grid, position, direction):
            if next_position not in visited_tiles:
                beams_of_lights.append(next_position)
    return energized_tiles


if __name__ == "__main__":
    grid = readlines('input_test.txt')
    start_position = (0, 0)
    start_direction = (0, 1)
    energized_tiles = energize_tiles(grid, start_position, start_direction)
    energized_tiles = [tile for sub_list in energized_tiles
                       for tile in sub_list]
    total = energized_tiles.count('#')
    print(total)
