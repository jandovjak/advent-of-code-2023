def readlines(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()]
    return lines

def nodes_from_line(nodes_lines):
    nodes = {}
    for line in nodes_lines:
        node, pair = line.split(' = ')
        left, right = pair.split(', ')
        nodes[node] = (left.replace('(', ''), right.replace(')', ''))
    return nodes

def get_direction(index, directions):
    return directions[index % len(directions)]

def steps(start_node, end_node, directions, nodes):
    steps = 0
    current_node = start_node
    while current_node != end_node:
        direction = get_direction(steps, directions)
        left, right = nodes[current_node]
        if direction == 'L':
            current_node = left
        else:
            current_node = right
        steps += 1
    return steps

if __name__ == "__main__":
    lines = readlines('input_test.txt')
    directions = lines[0]
    nodes = nodes_from_line(lines[2:])
    steps_to_ZZZ = steps('AAA', 'ZZZ', directions, nodes)
    print(steps_to_ZZZ)