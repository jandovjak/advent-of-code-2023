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


def steps(start_node, end_nodes, directions, nodes):
    steps = 0
    current_node = start_node
    while current_node not in end_nodes:
        direction = get_direction(steps, directions)
        left, right = nodes[current_node]
        if direction == 'L':
            current_node = left
        else:
            current_node = right
        steps += 1
    return steps


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def least_common_multiplier(steps):
    lcm = 1
    for step in steps:
        lcm = lcm * step // gcd(lcm, step)
    return lcm


if __name__ == "__main__":
    lines = readlines('input_test3.txt')
    directions = lines[0]
    nodes = nodes_from_line(lines[2:])
    start_nodes = list(filter(lambda node: node[-1] == 'A', nodes))
    end_nodes = list(filter(lambda node: node[-1] == 'Z', nodes))
    nodes_steps = []
    for start_node in start_nodes:
        nodes_steps.append(steps(start_node, end_nodes, directions, nodes))
    print(least_common_multiplier(nodes_steps))
