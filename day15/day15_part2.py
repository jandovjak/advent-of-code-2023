HASH_RANGE = 256

def read_steps(filename):
    whole_file = ''
    with open(filename, 'r') as file:
        whole_file = file.read()
    return whole_file.replace('\n', '').split(',')

def hash_label(label):
    current_value = 0
    for character in label:
        current_value = current_value + ord(character)
        current_value = (current_value * 17) % HASH_RANGE
    return current_value

def generate_boxes():
    boxes = []
    for _ in range(HASH_RANGE):
        boxes.append([])
    return boxes

def split_step(step):
    label = ''
    operation = ''
    focal_length = ''
    if step[-1] == '-':
        label = step[:len(step)-1]
        operation = '-'
        focal_length = '0'
    if '=' in step:
        label, focal_length = step.split('=')
        operation = '='
    return label, operation, int(focal_length)

def find_label_in_box(box, label_to_search):
    for index, (label, _) in enumerate(box):
        if label == label_to_search:
            return index
    return -1

def update_boxes(boxes, operation, lens):
    label, focal_length = lens
    box_index = hash_label(label)
    if operation == '=':
        label_index = find_label_in_box(boxes[box_index], label)
        if label_index != -1:
            boxes[box_index][label_index] = (label, focal_length)
        else:
            boxes[box_index].append((label, focal_length))
    if operation == '-':
        label_index = find_label_in_box(boxes[box_index], label)
        if label_index != -1:
            boxes[box_index] = boxes[box_index][:label_index] + boxes[box_index][label_index + 1:]
    return boxes

def valuate_boxes(boxes):
    total = 0
    for index_of_box, box in enumerate(boxes):
        for index_of_lens, (_, focal_length) in enumerate(boxes[index_of_box]):
            total += (index_of_box + 1) * (index_of_lens + 1) * focal_length
    return total

if __name__ == "__main__":
    steps = read_steps('input_test.txt')
    boxes = generate_boxes()
    for step in steps:
        label, operation, focal_length = split_step(step)
        boxes = update_boxes(boxes, operation, (label, focal_length))
    print(valuate_boxes(boxes))