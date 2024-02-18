def readlines(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def empty_line(line):
    return all(character == '.' for character in line)

def galaxies_points(universe):
    points = []
    for row in range(len(universe)):
        for col in range(len(universe[row])):
            if universe[row][col] == '#':
                points.append((row, col))
    return points

def rows_to_expand(universe):
    row_indexes = []
    for index, row in enumerate(universe):
        if empty_line(row):
            row_indexes.append(index)
    return row_indexes

def expanded_between_points(start_index, end_index, indexes):
    expanded_between_points = []
    if end_index < start_index:
        start_index, end_index = end_index, start_index
    for index in indexes:
        if start_index <= index <= end_index:
            expanded_between_points.append(index)
    return len(expanded_between_points)

def distance_of_galaxy(start, end, row_indexes, cols_indexes):
    start_row, start_col = start
    end_row, end_col = end
    expanded_rows_count = expanded_between_points(start_row, end_row, row_indexes) * 999_999
    expanded_cols_count = expanded_between_points(start_col, end_col, cols_indexes) * 999_999
    return abs(start_row - end_row) + abs(start_col - end_col) + expanded_rows_count + expanded_cols_count

def total_length_from_galaxy(galaxy, galaxies, row_indexes, cols_indexes):
    lengths = []
    for next_galaxy in galaxies:
        lengths.append(distance_of_galaxy(galaxy, next_galaxy, row_indexes, cols_indexes))
    return sum(lengths)

def cols_to_expand(universe):
    cols_indexes = []
    for index in range(len(universe[0])):
        col = [row[index] for row in universe]
        if empty_line(col):
            cols_indexes.append(index)
    return cols_indexes

if __name__ == "__main__":
    universe = readlines('input_test.txt')
    galaxies = galaxies_points(universe)
    row_indexes = rows_to_expand(universe)
    col_indexes = cols_to_expand(universe)
    total = 0
    for galaxy in galaxies:
        total += total_length_from_galaxy(galaxy, galaxies, row_indexes, col_indexes)
    print(total//2)