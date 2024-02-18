CUBES = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def readlines(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def events_from_line(line):
    all_events = line.split(':')[1]
    events = []
    for event in all_events.split(';'):
        current_event = []
        for throw in event.strip().split(','):
            number, color = throw.strip().split(' ')
            current_event.append((color, int(number)))
        events.append(current_event)
    return events

def game_id(line):
    game = line.split(':')[0]
    _, game_id = game.split(' ')
    return int(game_id)

def is_valid_game(line):
    is_valid = True
    for event in events_from_line(line):
        for color, number in event:
            maximum_for_color = CUBES.get(color, 0)
            is_valid = is_valid and number <= maximum_for_color
    return is_valid



if __name__ == "__main__":
    lines = readlines('input_test.txt')
    total = 0
    for line in lines:
        if is_valid_game(line):
            total += game_id(line)
    print(total)
            