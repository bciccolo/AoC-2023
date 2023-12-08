instructions = None
map = {}

def load_data(file):
    global instructions

    blank_found = False
    file = open(file, 'r')
    for line in file.readlines():
        line = line.strip()

        if not blank_found and not line == '':
            instructions = line
        elif line == '':
            blank_found = True
        else:
            # PBN = (JRP, RVT)
            key, list = [x.strip() for x in line.split('=')]
            left, right = [x.strip() for x in list[1:-1].split(',')]

            map[key] = [left, right]


load_data('day8.dat')
# print(instructions)
# print(map)

steps = 0
location = 'AAA'
while not location == 'ZZZ':
    choices = map[location]

    if instructions[steps % len(instructions)] == 'L':
        location = choices[0]
    else:
        location = choices[1]

    steps += 1

print('Part 1: ' + str(steps))
