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

def vertical_reflections(pattern):
    reflections = []
    for i in range(1, len(pattern[0])):
        reflection = True
        for line in pattern:
            left = list(reversed(line[:i]))
            right = line[i:]
            for j in range(min(len(left), len(right))):
                reflection = reflection and left[j] == right[j]
        if reflection:
            reflections.append(i)
    return reflections

def horizontal_reflections(pattern):
    flipped_pattern = [[pattern[j][i] for j in range(len(pattern))] for i in range(len(pattern[0]))]
    return vertical_reflections(flipped_pattern)

def smudge(old_character):
    if old_character == '.':
        return '#'
    return '.'

def find_new_reflection(old_vertical_reflections, new_vertical_reflections):
    if len(new_vertical_reflections) == 0:
        return 0
    if len(old_vertical_reflections) == 0:
        return new_vertical_reflections[0]
    if old_vertical_reflections[0] in new_vertical_reflections:
        new_vertical_reflections.remove(old_vertical_reflections[0])
    if len(new_vertical_reflections) == 0:
        return 0
    return new_vertical_reflections[0]

def new_vertical_reflection(pattern, old_vertical_reflections):
    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            old_character = pattern[i][j]
            pattern[i][j] = smudge(old_character)
            new_vertical_reflections = vertical_reflections(pattern)
            pattern[i][j] = old_character
            new_vertical_reflection = find_new_reflection(old_vertical_reflections, new_vertical_reflections)
            if new_vertical_reflection != 0:
                return new_vertical_reflection
    return 0

def new_horizontal_reflection(pattern, old_horizontal_reflections):
    flipped_pattern = [[pattern[j][i] for j in range(len(pattern))] for i in range(len(pattern[0]))]
    return new_vertical_reflection(flipped_pattern, old_horizontal_reflections)

if __name__ == "__main__":
    parts = read_parts('input_test.txt')
    patterns = []
    total = 0
    for part in parts:
        patterns.append(pattern_part(part))
    for pattern in patterns:
        old_vertical_reflections = vertical_reflections(pattern)
        total += new_vertical_reflection(pattern, old_vertical_reflections)
        old_horizontal_reflections = horizontal_reflections(pattern)
        total += 100 * new_horizontal_reflection(pattern, old_horizontal_reflections)
    print(total)