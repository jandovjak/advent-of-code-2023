def readlines(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def number_from_line(line):
    _, numbers = line.split(':')
    numbers = [number for number in numbers.split(' ') if number]
    return int(''.join(numbers))

def ways_to_win(time, record_distance):
    total_ways = 0
    for start_time in range(1, time):
        possible_distance = (time - start_time) * start_time
        if possible_distance > record_distance:
            total_ways += 1
    return total_ways


if __name__ == "__main__":
    lines = readlines('input_test.txt')
    time = number_from_line(lines[0])
    distance = number_from_line(lines[1])
    margin_of_error = ways_to_win(time, distance)
    print(margin_of_error)