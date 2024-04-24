def readlines(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines


def numbers_from_line(line):
    _, numbers = line.split(':')
    return [int(number) for number in numbers.split(' ') if number]


def ways_to_win(time, record_distance):
    total_ways = 0
    for start_time in range(1, time):
        possible_distance = (time - start_time) * start_time
        if possible_distance > record_distance:
            total_ways += 1
    return total_ways


if __name__ == "__main__":
    lines = readlines('input_test.txt')
    times = numbers_from_line(lines[0])
    distances = numbers_from_line(lines[1])
    margin_of_error = 1
    for i in range(len(times)):
        margin_of_error *= ways_to_win(times[i], distances[i])
    print(margin_of_error)
