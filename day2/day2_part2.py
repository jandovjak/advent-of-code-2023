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


def power_of_game(line):
    power_of_game = 1
    game_cubes = {
                'red': 0,
                'green': 0,
                'blue': 0}
    for event in events_from_line(line):
        for color, number in event:
            if number > game_cubes.get(color, 0):
                game_cubes[color] = number
    for color, number in game_cubes.items():
        power_of_game *= number
    return power_of_game


if __name__ == "__main__":
    lines = readlines('input_test.txt')
    total = 0
    for line in lines:
        total += power_of_game(line)
    print(total)
