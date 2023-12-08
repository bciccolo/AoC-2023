from math import lcm
from re import match

instructions = None
map = {}

def count_steps(start_pattern, end_pattern):
    start_points = []
    for location in map.keys():
        if match(start_pattern, location):
            start_points.append(location)

    # print(start_points)

    all_steps = []
    for location in start_points:
        steps = 0
        while not match(end_pattern, location):
            choices = map[location]
            if instructions[steps % len(instructions)] == 'L':
                location = choices[0]
            else:
                location = choices[1]

            steps += 1

        all_steps.append(steps)

    return lcm(*all_steps)


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
            key, list = [x.strip() for x in line.split('=')]
            left, right = [x.strip() for x in list[1:-1].split(',')]

            map[key] = [left, right]


load_data('day8.dat')
# print(instructions)
# print(map)

print('Part 1: ' + str(count_steps('AAA', 'ZZZ')))
print('Part 2: ' + str(count_steps(".*A$", ".*Z$")))