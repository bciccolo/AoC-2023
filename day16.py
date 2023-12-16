DOWN = 0
LEFT = 1
RIGHT = 2
UP = 3

X = 1
Y = 0
DIRECTION = 2

VISITED = '#'

grid = []

def load_data(file_name):
    file = open(file_name, 'r')
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        grid.append(list(line))


def track_beams(x, y, direction):
    beams = [[y, x, direction]]
    tiles = set()

    visited = []
    for row in grid:
        visited.append(list('.' * len(row)))

    while len(beams) > 0:
        beam = beams.pop()
        tiles.add((beam[Y], beam[X], beam[DIRECTION]))

        # Move beam one spot based on current direction
        #  mark spot visited
        #  if split, add beam to beams
        #  continue until WALL or REPEAT
        while True:
            if beam[DIRECTION] == DOWN:
                beam[Y] += 1

                # Hit bottom wall
                if beam[Y] == len(grid):
                    break

                # Split left/right
                if grid[beam[Y]][beam[X]] == '-':
                    beam[DIRECTION] = LEFT
                    beams.append([beam[Y], beam[X], RIGHT])

                # Turn right
                if grid[beam[Y]][beam[X]] == '\\':
                    beam[DIRECTION] = RIGHT

                # Turn left
                if grid[beam[Y]][beam[X]] == '/':
                    beam[DIRECTION] = LEFT

            elif beam[DIRECTION] == LEFT:
                beam[X] -= 1

                # Hit left wall
                if beam[X] < 0:
                    break

                # Split up/down
                if grid[beam[Y]][beam[X]] == '|':
                    beam[DIRECTION] = UP
                    beams.append([beam[Y], beam[X], DOWN])

                # Turn up
                if grid[beam[Y]][beam[X]] == '\\':
                    beam[DIRECTION] = UP

                # Turn down
                if grid[beam[Y]][beam[X]] == '/':
                    beam[DIRECTION] = DOWN

            elif beam[DIRECTION] == RIGHT:
                beam[X] += 1

                # Hit right wall
                if beam[X] == len(grid[0]):
                    break

                # Split up/down
                if grid[beam[Y]][beam[X]] == '|':
                    beam[DIRECTION] = UP
                    beams.append([beam[Y], beam[X], DOWN])

                # Turn down
                if grid[beam[Y]][beam[X]] == '\\':
                    beam[DIRECTION] = DOWN

                # Turn up
                if grid[beam[Y]][beam[X]] == '/':
                    beam[DIRECTION] = UP

            elif beam[DIRECTION] == UP:
                beam[Y] -= 1

                # Hit top wall
                if beam[Y] < 0:
                    break

                # Split left/right
                if grid[beam[Y]][beam[X]] == '-':
                    beam[DIRECTION] = LEFT
                    beams.append([beam[Y], beam[X], RIGHT])

                # Turn left
                if grid[beam[Y]][beam[X]] == '\\':
                    beam[DIRECTION] = LEFT

                # Turn right
                if grid[beam[Y]][beam[X]] == '/':
                    beam[DIRECTION] = RIGHT

            # Marked visited
            visited[beam[Y]][beam[X]] = '#'

            # Stop tracking if we've been here before
            vector = (beam[Y], beam[X], beam[DIRECTION])
            if vector in tiles:
                break
            tiles.add(vector)

    energized = 0
    for row in visited:
        energized += row.count('#')

    return energized


load_data('day16.dat')

print('Part 1: '  + str(track_beams(-1, 0, RIGHT)))

max_energized = 0
for i in range(len(grid)):
    max_energized = max(max_energized, \
                        track_beams(-1, i, RIGHT), \
                        track_beams(len(grid), i, LEFT), \
                        track_beams(i, -1, DOWN), \
                        track_beams(i, len(grid), UP))

print('Part 2: '  + str(max_energized))