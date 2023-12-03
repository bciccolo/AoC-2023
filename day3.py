import re

DIGITS_REGEX = re.compile("\d+")

def contains_symbol(string):
    for char in string:
        if not char.isdigit() and not char == '.':
            return True
    return False


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
        # else:
        #     print('>>>>>>>>>>>>>>>>>> part ' + part + ' on line ' + str(row + 1) + ' is BAD - search string: ' + string)
        #     print('   START: ' + str(start))
        #     print('   END:   ' + str(end))

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

i = 0
sum = 0
for parts in part_numbers:
    sum += get_parts_on_line(i, parts, grid)
    i += 1

print('Part 1: '  + str(sum))