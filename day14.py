grid = []

def calculate_weight():
    weight = 0

    for i, row in enumerate(grid):
        rocks = row.count('O')
        distance = len(grid) - i
        weight += rocks * distance

    return weight


def load_data(file_name):
    file = open(file_name, 'r')
    for line in file.readlines():
        line = line.strip()
        grid.append(list(line))


def shift_east():
    for row in range(len(grid)):
        for col in reversed(range(len(grid[0]))):
            # If there's an open spot, slide the next rock right
            if grid[row][col] == '.':
                next = col - 1
                while next > -1:
                    if grid[row][next] == 'O':
                        grid[row][col] = 'O'
                        grid[row][next] = '.'
                        break
                    elif grid[row][next] == '#':
                        break
                    next -= 1


def shift_north():
    for col in range(len(grid[0])):
        for row in range(len(grid)):
            # If there's an open spot, slide the next rock up
            if grid[row][col] == '.':
                next = row + 1
                while next < len(grid):
                    if grid[next][col] == 'O':
                        grid[row][col] = 'O'
                        grid[next][col] = '.'
                        break
                    elif grid[next][col] == '#':
                        break
                    next += 1


def shift_south():
    for col in range(len(grid[0])):
        for row in reversed(range(len(grid))):
            # If there's an open spot, slide the next rock down
            if grid[row][col] == '.':
                next = row - 1
                while next > -1:
                    if grid[next][col] == 'O':
                        grid[row][col] = 'O'
                        grid[next][col] = '.'
                        break
                    elif grid[next][col] == '#':
                        break
                    next -= 1


def shift_west():
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # If there's an open spot, slide the next rock left
            if grid[row][col] == '.':
                next = col + 1
                while next < len(grid):
                    if grid[row][next] == 'O':
                        grid[row][col] = 'O'
                        grid[row][next] = '.'
                        break
                    elif grid[row][next] == '#':
                        break
                    next += 1


load_data('day14.dat')

hashes = []

i = 0
while i < 1_000_000_000:
    shift_north()
    if i == 0:
        print('Part 1: ' + str(calculate_weight()))
    shift_west()
    shift_south()
    shift_east()

    # We don't have to *really* iterate 1 billion times,
    # we just need to find when the pattern starts to
    # repeat...
    value = hash(''.join([''.join(row) for row in grid]))
    if value in hashes:
        # Now all we have to do is complete some extra
        # cycles until we reach 1 billion
        original = hashes.index(value)
        period = i - original
        remainder = (1_000_000_000 - original) % period
        i = 1_000_000_000 - remainder + 1

        # Forgetting to clear the list will cause an infinite loop!
        hashes.clear()
    else:
        hashes.append(value)
        i += 1

print('Part 2: ' + str(calculate_weight()))