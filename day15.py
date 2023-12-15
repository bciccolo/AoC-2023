def calculate_hash(text):
    sum = 0

    value = 0
    for c in text:
        if c == ',':
            sum += value
            value = 0
        else:
            value += ord(c)
            value *= 17
            value %= 256

    # Fencepost
    sum += value

    return sum


file = open('day15.dat', 'r')
line = file.readlines()[0].strip()

print('Part 1: ' + str(calculate_hash(line)))

boxes = []
for i in range(256):
    boxes.append([])

for instruction in line.split(','):
    operator = '='
    if operator not in instruction:
        operator = '-'
    label, focal_length = instruction.split(operator)
    box_index = calculate_hash(label)
    # print(instruction + ' >> label: ' + label + ' hash: ' + str(value) + ' lens: ' + lens)

    slots = boxes[box_index]
    slot_index = -1
    for i in range(len(slots)):
        if slots[i][0] == label:
            slot_index = i
            break

    if operator == '=':
        if slot_index == -1:
            slots.append([label, focal_length])
        else:
            slots[slot_index][1] = focal_length
    else:
        if slot_index > -1:
            slots.pop(slot_index)

focusing_power = 0
for i, box in enumerate(boxes):
    if len(box) > 0:
        # print('Box ' + str(i) + ': ' + str(box))
        for j, slot in enumerate(box):
            focusing_power += (i + 1) * (j + 1) * int(slot[1])

print('Part 2: ' + str(focusing_power))