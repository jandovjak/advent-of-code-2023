def read_parts(filename):
    whole_file = ''
    with open(filename, 'r') as file:
        whole_file = file.read()
    return whole_file.split('\n\n')

def pattern_part(part):
    pattern = []
    for line in part.split('\n'):
        pattern.append(list(line))
    return pattern

def vertical_reflection(pattern):
    reflections_total = 0
    for i in range(1, len(pattern[0])):
        reflection = True
        for line in pattern:
            left = list(reversed(line[:i]))
            right = line[i:]
            for j in range(min(len(left), len(right))):
                reflection = reflection and left[j] == right[j]
        if reflection:
            reflections_total = i
    return reflections_total

def horizontal_reflection(pattern):
    flipped_pattern = [[pattern[j][i] for j in range(len(pattern))] for i in range(len(pattern[0]))]
    return vertical_reflection(flipped_pattern)

if __name__ == "__main__":
    parts = read_parts('input_test.txt')
    patterns = []
    total = 0
    for part in parts:
        patterns.append(pattern_part(part))
    for pattern in patterns:
        total += vertical_reflection(pattern)
        total += 100 * horizontal_reflection(pattern)
    print(total)