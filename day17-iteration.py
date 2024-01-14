# Order of these values matter: a left turn is (direction + 1) % 4, a right turn is (direction - 1) % 4
UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

# Vector positions
Y = 0
X = 1
DIRECTION = 2

grid = []

def can_move(y, x, direction):
    if direction == UP and y > 0:
        return True
    elif direction == DOWN and y < len(grid) - 1:
        return True
    elif direction == LEFT and x > 0:
        return True
    elif direction == RIGHT and x < len(grid[0]) - 1:
        return True
    else:
        return False


def find_min_loss(y, x, direction):
    min_loss = 9 * len(grid) * len(grid[0])

    sums_by_vector = {}
    paths_by_vector = {}
    attempted_vectors = set()

    vector = (y, x, direction)
    sums_by_vector[vector] = 0
    paths_by_vector[vector] = [(y, x)]

    while len(sums_by_vector) > 0:
        vector = list(sums_by_vector)[0]

        y = vector[Y]
        x = vector[X]
        direction = vector[DIRECTION]

        sum = sums_by_vector.pop(vector)
        path = paths_by_vector.pop(vector)

        if vector in attempted_vectors:
            continue
        attempted_vectors.add(vector)

        steps = 0
        while y != len(grid) - 1 or x != len(grid[0]) - 1:
            # Go straight, if allowed & possible
            if steps < 3 and can_move(y, x, direction):
                # Remember left and right options
                left_vector = (y, x, (direction + 1) % 4)
                if left_vector not in sums_by_vector or sum < sums_by_vector[left_vector]:
                    sums_by_vector[left_vector] = sum
                    paths_by_vector[left_vector] = path.copy()

                right_vector = (y, x, (direction - 1) % 4)
                if right_vector not in sums_by_vector or sum < sums_by_vector[right_vector]:
                    sums_by_vector[right_vector] = sum
                    paths_by_vector[right_vector] = path.copy()

                y, x = move(y, x, direction)
                steps += 1

            # Go left, if possible
            elif can_move(y, x, (direction + 1) % 4):
                # Remember right option
                right_vector = (y, x, (direction - 1) % 4)
                if right_vector not in sums_by_vector or sum < sums_by_vector[right_vector]:
                    # HERE: debug
                    # if right_vector in sums_by_vector and sum < sums_by_vector[right_vector]:
                    #     print('better')
                    sums_by_vector[right_vector] = sum
                    paths_by_vector[right_vector] = path.copy()

                direction = (direction + 1) % 4
                y, x = move(y, x, direction)
                steps = 0

            # Go right, if possible
            elif can_move(y, x, (direction - 1) % 4):
                direction = (direction - 1) % 4
                y, x = move(y, x, direction)
                steps = 0

            else:
                print('Stuck')
                break

            if (y, x) in path:
                # print('Repeat')
                break

            path.append((y, x))
            sum += grid[y][x]

            # print(str(y) + ',' + str(x) + ',' + str(grid[y][x]))

            # Stop following this path if it's already exceeded the best path
            if sum > min_loss:
                # print('Abandoned')
                break

        if y == len(grid) - 1 and x == len(grid[0]) - 1:
            if sum < min_loss:
                min_loss = sum
                print('Candidate: ' + str(min_loss) + ' along path: ' + str(path))

    return min_loss


def load_data(file_name):
    global destination

    file = open(file_name, 'r')
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        grid.append([int(digit) for digit in line])


def move(y, x, direction):
    if direction == UP and y > 0:
        return (y - 1, x)
    elif direction == DOWN and y < len(grid) - 1:
        return (y + 1, x)
    elif direction == LEFT and x > 0:
        return (y, x - 1)
    elif direction == RIGHT and x < len(grid[0]) - 1:
        return (y, x + 1)


load_data('day17-snippet.dat')


print('Part 1: '  + str(find_min_loss(0, 0, RIGHT)))
# find_min_loss(0, 0, DOWN)
