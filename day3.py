import re

DIGITS_REGEX = re.compile("\d+")

def contains_symbol(string):
    for char in string:
        if not char.isdigit() and not char == '.':
            return True
    return False


def find_gear_ratio(grid, row, col):
    gears = []

    # Search current row
    gears += find_gears_in_row(grid, row, col, False)

    # Search row above, if present
    if row > 0:
        gears += find_gears_in_row(grid, row - 1, col, True)

    # Search row below, if present
    if row  < len(grid) - 1:
        gears += find_gears_in_row(grid, row + 1, col, True)

    if len(gears) == 2:
        # print(gears)
        # print('gear ratio in line ' + str(row + 1) + ' is ' + str(gears[0] * gears[1]))
        return gears[0] * gears[1]

    return 0


def find_gears_in_row(grid, row, col, include_col):
    gears = []

    if grid[row][col].isdigit():
        number = grid[row][col]

        # Add digits to the left
        if col > 0:
            search_col = col - 1
            while search_col > -1 and grid[row][search_col].isdigit():
                number = grid[row][search_col] + number
                search_col -= 1

        # Add digits to the right
        if col < len(grid[row]) - 1:
            search_col = col + 1
            while search_col < len(grid[row]) and grid[row][search_col].isdigit():
                number += grid[row][search_col]
                search_col += 1

        gears.append(int(number))
    else:
        # Try left...
        if col > 0:
            search_col = col - 1
            number = ''
            while search_col > -1 and grid[row][search_col].isdigit():
                number = grid[row][search_col] + number
                search_col -= 1
            if len(number) > 0:
                gears.append(int(number))

        # Try right...
        if col < len(grid[row]) - 1:
            search_col = col + 1
            number = ''
            while search_col < len(grid[row]) and grid[row][search_col].isdigit():
                number += grid[row][search_col]
                search_col += 1
            if len(number) > 0:
                gears.append(int(number))

    return gears


def get_parts_on_line(row, parts, grid):
    total = 0
    end = 0
    for part in parts:
        start = grid[row].find(part, end)
        end = start + len(part) - 1

        if start > 0:
            start -= 1

        if end < len(grid[row]) - 1:
            end += 1

        # Current row
        string = grid[row][start:end + 1]

        # Previous row, if present
        if row > 0:
            string += grid[row - 1][start:end + 1]

        # Next row, if present
        if row  < len(grid) - 1:
            string += grid[row + 1][start:end + 1]

        if contains_symbol(string):
            total += int(part)

    return total


file = open('day3.txt', 'r')
lines = file.readlines()

part_numbers = []
grid = []

for line in lines:
    line = line.strip()
    part_numbers.append(DIGITS_REGEX.findall(line))
    grid.append(line)

file.close()

#
# Part 1
#
i = 0
sum = 0
for parts in part_numbers:
    sum += get_parts_on_line(i, parts, grid)
    i += 1

print('Part 1: '  + str(sum))

#
# Part 2
#
sum = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == '*':
            sum += find_gear_ratio(grid, row, col)

print("Part 2: " + str(sum))