DIGIT_NAMES = [ 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def find_first_digit(text, consider_names):
    i = 0
    while i < len(text):
        if text[i].isdigit():
            return int(text[i])

        if consider_names:
            for index, name in enumerate(DIGIT_NAMES):
                if text[i:i + len(name)] == name:
                    return index

        i += 1


def find_last_digit(text, consider_names):
    i = len(text) - 1
    while i >= 0:
        if text[i].isdigit():
            return int(text[i])

        if consider_names:
            for index, name in enumerate(DIGIT_NAMES):
                if text[i - len(name):i] == name:
                    return index

        i -= 1


file = open('day1.dat', 'r')
lines = file.readlines()

total_part_1 = 0
total_part_2 = 0
for line in lines:
    total_part_1 += find_first_digit(line, False) * 10 + find_last_digit(line, False)
    total_part_2 += find_first_digit(line, True) * 10 + find_last_digit(line, True)

print('Part 1: '  + str(total_part_1))
print('Part 2: '  + str(total_part_2))