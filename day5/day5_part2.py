import math

def read_parts(filename):
    whole_file = ''
    with open(filename, 'r') as file:
        whole_file = file.read()
    return whole_file.split('\n\n')

def filter_numbers(line):
    numbers = []
    for string in line.split(' '):
        if string.isdigit():
            numbers.append(int(string))
    return numbers

def map_of_part(part):
    lines = part.split('\n')
    map_of_part = []
    for line in lines[1:]:
        destination_start, source_start, map_range = filter_numbers(line)
        map_of_part.append((source_start, destination_start, map_range))
    return sorted(map_of_part, key=lambda map_part: map_part[1])

def seeds_to_ranges(seeds):
    ranges = []
    for i in range(0, len(seeds) - 1, 2):
        ranges.append((seeds[i], seeds[i + 1]))
    return sorted(ranges, key=lambda one_range: one_range[1])

def generate_points(map_part, source):
    points = [0]
    for start, start_range in source:
        points += [start, start + start_range]
    for source_start, _, source_range in map_part:
        points += [source_start, source_start + source_range]
    return sorted(list(set(points)))

def splitted_source(points, source):
    splitted_source = []
    for i in range(len(points) - 1):
        new_point = points[i]
        new_range = points[i + 1] - points[i]
        for start, start_range in source:
            if start <= new_point < start + start_range:
                splitted_source.append((new_point, new_range))
    return splitted_source

def map_source(source, map_part):
    destination = []
    for start, start_range in source:
        found_mapping = False
        for source_start, destination_start, source_range in map_part:
            if source_start <= start < source_start + source_range:
                new_destination = destination_start + start - source_start
                destination.append((new_destination, start_range))
                found_mapping = True
        if not found_mapping:
            destination.append((start, start_range))
    return sorted(destination, key=lambda one_range: one_range[0]) 

if __name__ == "__main__":
    parts = read_parts('input_test.txt')
    seeds = filter_numbers(parts[0])
    source = seeds_to_ranges(seeds)
    for part in parts[1:]:
        map_part = map_of_part(part)
        points = generate_points(map_part, source)
        new_source = splitted_source(points, source)
        source = map_source(new_source, map_part)
    print(source[0])