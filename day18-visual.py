grid = []

X = 1
Y = 0
SHAPE = 2

def fill_trench():
    for row in range(len(grid)):
        outside = True
        last = ''
        for col in range(len(grid[row])):
            if grid[row][col] == '.':
                if not outside:
                    grid[row][col] = '#'
            elif grid[row][col] == '|':
                outside = not outside
                last = ''
            elif grid[row][col] == 'L':
                last = 'L'
            elif grid[row][col] == 'F':
                last = 'F'
            elif grid[row][col] == 'J':
                if last == 'F':
                    outside = not outside
                last = ''
            elif grid[row][col] == '7':
                if last == 'L':
                    outside = not outside
                last = ''


def get_angle(last_direction, direction):
    if last_direction == 'U' and direction == 'R':
        return 'F'
    elif last_direction == 'U' and direction == 'L':
        return '7'
    elif last_direction == 'D' and direction == 'R':
        return 'L'
    elif last_direction == 'D' and direction == 'L':
        return 'J'
    elif last_direction == 'R' and direction == 'U':
        return 'J'
    elif last_direction == 'R' and direction == 'D':
        return '7'
    elif last_direction == 'L' and direction == 'U':
        return 'L'
    elif last_direction == 'L' and direction == 'D':
        return 'F'


def load_data(file_name):
    points = []
    x = 0
    y = 0

    first_direcion = ''
    last_direction = '?'

    file = open(file_name, 'r')
    lines = file.readlines()
    for line in lines:
        parts = line.split()
        direction = parts[0]
        magnitude = int(parts[1])

        if first_direcion == '':
            first_direcion = direction

        angle = get_angle(last_direction, direction)

        points.append([y, x, angle])

        if direction == 'U':
            for _ in range(magnitude):
                y-= 1
                points.append([y, x, '|'])
        elif direction == 'D':
            for _ in range(magnitude):
                y += 1
                points.append([y, x, '|'])
        elif direction == 'L':
            for _ in range(magnitude):
                x -= 1
                points.append([y, x, '-'])
        else:
            for _ in range(magnitude):
                x += 1
                points.append([y, x, '-'])

        last_direction = direction

    angle = get_angle(last_direction, first_direcion)
    points[len(points) - 1][SHAPE] = angle

    min_x = points[0][X]
    max_x = points[0][X]

    min_y = points[0][Y]
    max_y = points[0][Y]

    for point in points:
        if point[X] < min_x:
            min_x = point[X]

        if point[X] > max_x:
            max_x = point[X]

        if point[Y] < min_y:
            min_y = point[Y]

        if point[Y] > max_y:
            max_y = point[Y]

    x_shift = abs(min_x)
    y_shift = abs(min_y)

    magnitude = max(max_x - min_x, max_y - min_y) + 1

    for row in range(magnitude):
        grid.append(list('.' * magnitude))

    for point in points:
        point[X] += x_shift
        point[Y] += y_shift

        grid[point[Y]][point[X]] = point[SHAPE]


load_data('day18.dat')

# for row in grid:
#     print(''.join(row))

fill_trench()

# print()
# for row in grid:
#     print(''.join(row))

total = 0
for row in grid:
    total += len(row) - row.count('.')

print('Part 1: ' + str(total))
