HASH_RANGE = 256


def read_steps(filename):
    whole_file = ''
    with open(filename, 'r') as file:
        whole_file = file.read()
    return whole_file.replace('\n', '').split(',')


def hash_step(step):
    current_value = 0
    for character in step:
        current_value = current_value + ord(character)
        current_value = (current_value * 17) % HASH_RANGE
    return current_value


if __name__ == "__main__":
    steps = read_steps('input_test.txt')
    total = 0
    for step in steps:
        total += hash_step(step)
    print(total)
