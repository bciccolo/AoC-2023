from pprint import pprint

DOWN = 1
LEFT = 2
RIGHT = 3
UP = 4

X = 1
Y = 0

maze = []
start = []
start_pipe = ''

def load_maze(filename):
    global start

    file = open(filename, 'r')
    for row, line in enumerate(file.readlines()):
        line = line.strip()

        # Snippet file contains multiple mazes separated by blank lines
        if line == '':
            break

        maze.append([])

        for col, char in enumerate(line):
            if char == 'S':
                start = [row, col]
            maze[row].append(char)

    # pprint(maze)
    # print(start)


def load_waypoints():
    global start_pipe

    waypoints = []

    up = False
    left = False
    down = False
    right = False

    move = move_up(start)
    if move:
        waypoints.append(move)
        up = True

    move = move_left(start)
    if move:
        waypoints.append(move)
        left = True

    move = move_down(start)
    if move:
        waypoints.append(move)
        down = True

    move = move_right(start)
    if move:
        waypoints.append(move)
        right = True

    if up and down:
        start_pipe = '|'
    elif left and right:
        start_pipe = '-'
    elif up and right:
        start_pipe = 'L'
    elif up and left:
        start_pipe = 'J'
    elif down and right:
        start_pipe = 'F'
    elif down and left:
        start_pipe = '7'

    return waypoints


def mark_points(grid):
    for row in range(len(grid)):
        outside = True
        last = ''
        for col in range(len(grid[row])):
            if grid[row][col] == '.':
                if outside:
                    grid[row][col] = 'O'
                else:
                    grid[row][col] = 'I'
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


def move_along_path(waypoint):
    x = waypoint['point'][X]
    y = waypoint['point'][Y]
    entry = waypoint['entry']

    pipe = maze[y][x]
    if pipe == '|':
        if waypoint['entry'] == UP:
            y += 1
        else:
            y -= 1
    elif pipe == '-':
        if waypoint['entry'] == LEFT:
            x += 1
        else:
            x -= 1
    elif pipe == '7':
        if waypoint['entry'] == LEFT:
            y += 1
            entry = UP
        else:
            x -= 1
            entry = RIGHT
    elif pipe == 'F':
        if waypoint['entry'] == RIGHT:
            y += 1
            entry = UP
        else:
            x += 1
            entry = LEFT
    elif pipe == 'J':
        if waypoint['entry'] == LEFT:
            y -= 1
            entry = DOWN
        else:
            x -= 1
            entry = RIGHT
    elif pipe == 'L':
        if waypoint['entry'] == RIGHT:
            y -= 1
            entry = DOWN
        else:
            x += 1
            entry = LEFT

    return {'point': [y, x], 'entry': entry}


def move_down(point):
    if point[Y] < len(maze) - 1 and maze[point[Y] + 1][point[X]] in ('|', 'J', 'L'):
        return {'point': [point[Y] + 1, point[X]], 'entry': UP}
    return False


def move_left(point):
    if point[X] > 0 and maze[point[Y]][point[X] - 1] in ('-', 'L', 'F'):
        return {'point': [point[Y], point[X] - 1], 'entry': RIGHT}
    return False


def move_right(point):
    if point[X] < len(maze[0]) and maze[point[Y]][point[X] + 1] in ('-', 'J', '7'):
        return {'point': [point[Y], point[X] + 1], 'entry': LEFT}
    return False


def move_up(point):
    if point[Y] > 0 and maze[point[Y] - 1][point[X]] in ('|', '7', 'F'):
        return {'point': [point[Y] - 1, point[X]], 'entry': DOWN}
    return False

load_maze('day10.dat')

waypoint_1, waypoint_2 = load_waypoints()
full_path = [start, waypoint_1['point'], waypoint_2['point']]

steps = 1
# print(steps)
# pprint(waypoint_1)
# pprint(waypoint_2)
while not waypoint_1['point'] == waypoint_2['point']:
    waypoint_1 = move_along_path(waypoint_1)
    waypoint_2 = move_along_path(waypoint_2)

    full_path.append(waypoint_1['point'])
    full_path.append(waypoint_2['point'])

    steps += 1
    # print(steps)
    # pprint(waypoint_1)
    # pprint(waypoint_2)

print('Part 1: ' + str(steps))

grid = []
for i in range(len(maze)):
    grid.append(list('.' * (len(maze[i]))))

for point in full_path:
    grid[point[Y]][point[X]] = maze[point[Y]][point[X]]

# for row in grid:
#     print("".join(row))

# print('Start pipe: ' + start_pipe)
grid[start[Y]][start[X]] = start_pipe

mark_points(grid)

# for row in grid:
#     print("".join(row))

inside = 0
for row in grid:
    inside += row.count('I')

print('Part 2: ' + str(inside))