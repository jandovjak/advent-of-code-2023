def readlines(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def numbers_from_line(line):
    return [int(number) for number in line.split(' ') if number]

def all_zeroes(numbers):
    return all(number == 0 for number in numbers)

def differences(numbers):
    return [x - y for x, y in zip(numbers, numbers[1:])]

def predicted_value(numbers):
    difference_steps = [numbers]
    difference_step = differences(numbers)
    difference_steps.append(difference_step)
    while not all_zeroes(difference_step):
        difference_step = differences(difference_step)
        difference_steps.append(difference_step)
    difference_steps[-1].append(0)
    difference_steps = difference_steps[::-1]
    for i in range(1, len(difference_steps)):
        placeholder = difference_steps[i][0] + difference_steps[i - 1][0]
        difference_steps[i] = [placeholder] + difference_steps[i]
    return difference_steps[-1][0]

if __name__ == "__main__":
    lines = readlines('input_test.txt')
    total = 0
    for line in lines:
        numbers = numbers_from_line(line)
        total += predicted_value(numbers)
    print(total)