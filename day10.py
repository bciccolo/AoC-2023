from pprint import pprint

DOWN = 1
LEFT = 2
RIGHT = 3
UP = 4

X = 1
Y = 0

maze = []
start = []

def load_maze(filename):
    global start

    file = open(filename, 'r')
    for row, line in enumerate(file.readlines()):
        line = line.strip()
        maze.append([])

        for col, char in enumerate(line):
            if char == 'S':
                start = [row, col]
            maze[row].append(char)

    # pprint(maze)
    print(start)


def load_waypoints():
    waypoints = []

    move = move_up(start)
    if move:
        waypoints.append(move)

    move = move_left(start)
    if move:
        waypoints.append(move)

    move = move_down(start)
    if move:
        waypoints.append(move)

    move = move_right(start)
    if move:
        waypoints.append(move)

    return waypoints


def move_along_path(waypoint):
    x = waypoint['point'][X]
    y = waypoint['point'][Y]
    pipe = maze[y][x]
    if pipe == '|':
        if waypoint['entry'] == UP:
            waypoint['point'][Y] = y + 1
            return
        else:
            waypoint['point'][Y] = y - 1
            return
    if pipe == '-':
        if waypoint['entry'] == LEFT:
            waypoint['point'][X] = x + 1
            return
        else:
            waypoint['point'][X] = x - 1
            return
    if pipe == '7':
        if waypoint['entry'] == LEFT:
            waypoint['point'][Y] = y + 1
            waypoint['entry'] = UP
            return
        else:
            waypoint['point'][X] = x - 1
            waypoint['entry'] = RIGHT
            return
    if pipe == 'F':
        if waypoint['entry'] == RIGHT:
            waypoint['point'][Y] = y + 1
            waypoint['entry'] = UP
            return
        else:
            waypoint['point'][X] = x + 1
            waypoint['entry'] = LEFT
            return
    if pipe == 'J':
        if waypoint['entry'] == LEFT:
            waypoint['point'][Y] = y - 1
            waypoint['entry'] = DOWN
            return
        else:
            waypoint['point'][X] = x - 1
            waypoint['entry'] = RIGHT
            return
    if pipe == 'L':
        if waypoint['entry'] == RIGHT:
            waypoint['point'][Y] = y - 1
            waypoint['entry'] = DOWN
            return
        else:
            waypoint['point'][X] = x + 1
            waypoint['entry'] = LEFT
            return


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

steps = 1
# print(steps)
pprint(waypoint_1)
pprint(waypoint_2)
while not waypoint_1['point'] == waypoint_2['point']:
# for i in range(8):
    move_along_path(waypoint_1)
    move_along_path(waypoint_2)
    steps += 1
    # print(steps)
    # pprint(waypoint_1)
    # pprint(waypoint_2)

print('Part 1: ' + str(steps))
print('Part 2: ' + str(0))