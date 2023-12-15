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


part_1 = 0

file = open('day15.dat', 'r')
for line in file.readlines():
    line = line.strip()
    part_1 = calculate_hash(line)

print('Part 1: ' + str(part_1))