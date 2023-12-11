X = 1
Y = 0

expansion_columns = []
expansion_rows = []
galaxies = []
universe = []

def get_total_distance(expansion_factor):
    total_distance = 0

    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            total_distance += get_distance(galaxies[i], galaxies[j], expansion_factor)

    return total_distance


def get_distance(point_1, point_2, expansion_factor):
    distance = abs(point_1[X] - point_2[X]) + abs(point_1[Y] - point_2[Y])

    # Check expansion rows
    min_y = min(point_1[Y], point_2[Y])
    max_y = max(point_1[Y], point_2[Y])
    for row in expansion_rows:
        if row > min_y and row < max_y:
            distance += expansion_factor

    # Check expansion columns
    min_x = min(point_1[X], point_2[X])
    max_x = max(point_1[X], point_2[X])
    for col in expansion_columns:
        if col > min_x and col < max_x:
            distance += expansion_factor

    return distance


def load_galaxies():
    for y in range(len(universe)):
        for x in range(len(universe[y])):
            if universe[y][x] == '#':
                galaxies.append([y, x])


def load_universe(file_name):
    count = 0
    file = open(file_name, 'r')
    for line in file.readlines():
        line = line.strip()

        # Find row expansions (easy)
        if line.count('#') == 0:
            # universe.append(list(line))
            expansion_rows.append(count)

        universe.append(list(line))

        count += 1

    # Find column expansions (not as easy)
    for i in range(len(universe[0])):
        column = [row[i] for row in universe]
        if column.count('#') == 0:
            expansion_columns.append(i)


load_universe('day11.dat')
load_galaxies()

# for row in universe:
#     print("".join(row))
# print(galaxies)

print('Part 1: ' + str(get_total_distance(1)))
print('Part 2: ' + str(get_total_distance(999_999)))