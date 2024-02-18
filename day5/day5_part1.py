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
    return map_of_part

def map_transtion(transition_map, input):
    for source_start, destination_start, map_range in transition_map:
        if source_start <= input < source_start + map_range:
            return destination_start + input - source_start
    return input

def location(seed, maps):
    current_value = seed
    for map in maps:
        current_value = map_transtion(map, current_value)
    return current_value

if __name__ == "__main__":
    parts = read_parts('input_test.txt')
    seeds = filter_numbers(parts[0])
    maps = []
    locations = []
    for part in parts[1:]:
        maps.append(map_of_part(part))
    for seed in seeds:
        locations.append(location(seed, maps))
    print(min(locations))