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