# Order of these values matter: a left turn is (direction + 1) % 4, a right turn is (direction - 1) % 4
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

X = 1
Y = 0

grid = []
path_losses = []
paths = []
min_loss = 9 * 141 * 141 # 141x141 is the dimension of the full data set

def find_paths(x, y, direction, straight_count, sum, visited, path):
    # Go straight, if allowed
    if straight_count < 2:
        move(x, y, direction, straight_count + 1, sum, visited, path.copy()) # visited.copy()?

    # Turn left
    move(x, y, (direction + 1) % 4, 0, sum, visited, path.copy()) # visited.copy()?

    # Turn right
    move(x, y, (direction - 1) % 4, 0, sum, visited, path.copy()) # visited.copy()?


def load_data(file_name):
    global destination

    file = open(file_name, 'r')
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        grid.append([int(digit) for digit in line])

cache = {}
def move(x, y, direction, straight_count, sum, visited, path):
    global min_loss

    if direction == UP and y > 0:
        y -= 1
    elif direction == DOWN and y < len(grid) - 1:
        y += 1
    elif direction == LEFT and x > 0:
        x -= 1
    elif direction == RIGHT and x < len(grid[0]) - 1:
        x += 1
    else:
        return

    loss = grid[y][x]
    sum += loss

    # Stop following this path if it's already exceeded the best path
    if sum > min_loss:
        return

    # if x == 9 and y == 2:
    #     print('breakpoint')

    point = (x, y)
    if point not in visited:
        visited[point] = sum
        # visited.add(point)
    elif visited[point] < sum:
        return
    else:
        visited[point] = sum

    path.append(point)

    if y == len(grid) - 1 and x == len(grid[0]) - 1:
        path_losses.append(sum)
        if sum < min_loss:
            min_loss = sum
        paths.append(path)
    else:
        find_paths(x, y, direction, straight_count, sum, visited, path)


import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())

load_data('day17.dat')
visited = set()
visited = {}

min_loss = 0
for i in range(len(grid)):
    min_loss += grid[i][i]

find_paths(0, 0, RIGHT, 0, 0, visited, [])
# find_paths(0, 0, DOWN, 0, 0, visited, [])
print(len(path_losses))
# for path in paths:
#     print(path)
# for point in paths[len(paths)-1]:
#     print(point)
print('Part 1: '  + str(min(path_losses)))
print('Part 1: '  + str(min_loss))
