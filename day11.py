X = 1
Y = 0

expansion_columns = []
expansion_rows = []

def find_galaxies(universe):
    galaxies = []

    for y in range(len(universe)):
        for x in range(len(universe[y])):
            if universe[y][x] == '#':
                galaxies.append([y, x])

    return galaxies


def get_distance(point_1, point_2):
    return abs(point_1[X] - point_2[X]) + abs(point_1[Y] - point_2[Y])


def load_universe(file_name):
    universe = []

    count = 0
    file = open(file_name, 'r')
    for line in file.readlines():
        line = line.strip()

        # Expand rows (easy)
        if line.count('#') == 0:
            universe.append(list(line))

        universe.append(list(line))

        count += 1

    # Expand columns (not so easy)
    i = 0
    while i < len(universe[0]):
        column = [row[i] for row in universe]
        if column.count('#') == 0:
            for row in universe:
                row.insert(i, '.')
            i += 1

        i += 1

    return universe


universe = load_universe('day11.dat')
galaxies = find_galaxies(universe)

# for row in universe:
#     print("".join(row))
# print(galaxies)

total_distance = 0
for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        total_distance += get_distance(galaxies[i], galaxies[j])

print('Part 1: ' + str(total_distance))
print('Part 2: ' + str(0))