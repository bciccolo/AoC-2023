grid = []

def load_data(file_name):
    file = open(file_name, 'r')
    for line in file.readlines():
        line = line.strip()
        grid.append(list(line))


def shift_north():
    # print('************ POST SHIFT: ')
    # for row in grid:
    #     print(''.join(row))

    for col in range(len(grid[0])):
        for row in range(len(grid)):
            # If there's an open spot, slide the next rock down
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

    # print('************ POST SHIFT: ')
    # for row in grid:
    #     print(''.join(row))


load_data('day14.dat')
shift_north()

weight = 0
for i, row in enumerate(grid):
    rocks = row.count('O')
    distance = len(grid) - i
    weight += rocks * distance

print('Part 1: ' + str(weight))