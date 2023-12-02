MAX_BLUE = 14
MAX_GREEN = 13
MAX_RED = 12

def calculate_power(game_results):
    max_blue = 0
    max_green = 0
    max_red = 0
    for round in game_results.split(':')[1].split(';'):
        for color_count in [ x.strip() for x in round.split(',') ]:
            count, color = [ entry.strip() for entry in color_count.split(' ')]
            count = int(count)

            if color == 'blue' and count > max_blue:
               max_blue = count

            if color == 'green' and count > max_green:
               max_green = count

            if color == 'red' and count > max_red:
                max_red = count

    return max_blue * max_green * max_red


def check_games(game_results):
    for round in game_results.split(':')[1].split(';'):
        for color_count in [ x.strip() for x in round.split(',') ]:
            count, color = [ entry.strip() for entry in color_count.split(' ')]
            count = int(count)

            if (color == 'blue'  and count > MAX_BLUE)  or \
               (color == 'green' and count > MAX_GREEN) or \
               (color == 'red'   and count > MAX_RED):
                return False

    return True


file = open('day2.txt', 'r')
lines = file.readlines()

count = 1
sum_part_1 = 0
sum_part_2 = 0
for line in lines:
    if check_games(line):
        sum_part_1 += count
    count += 1

    sum_part_2 += calculate_power(line)

print('Part 1: '  + str(sum_part_1))
print('Part 2: '  + str(sum_part_2))