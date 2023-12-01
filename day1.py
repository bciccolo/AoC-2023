DATA_FILE = 'day1.txt'

DIGIT_NAMES = [ 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def convert_words_to_digits(text):
    updated = ''
    i = 0
    while i < len(text):
        found = False
        for index, name in enumerate(DIGIT_NAMES):
            if text[i:i + len(name)] == name:
                updated += str(index)
                i += len(name)
                found = True
                break

        if not found:
            updated += text[i]
            i += 1

    return updated


def find_number(line):
    digits = [int(c) for c in [*line] if c.isdigit()]
    length = len(digits)
    if length > 1:
        return digits[0] * 10 + digits[length - 1]
    return digits[0] * 10 + digits[0]


def part1():
    file = open(DATA_FILE, 'r')
    lines = file.readlines()

    total = 0
    for line in lines:
        total += find_number(line.strip())

    print(' Part 1: '  + str(total))


def part2():
    file = open(DATA_FILE, 'r')
    lines = file.readlines()

    total = 0
    for line in lines:
        original = line.strip()
        line = convert_words_to_digits(line.strip())
        # print(original + " --> " + line + ' : '  + str(find_number(line)))
        total += find_number(line)

    print(' Part 2: '  + str(total))


part1()
part2() #54100 - too high

# print(convert_words_to_digits('twongdsevenfivefive3foureightwonn'))
# print(convert_words_to_digits('threesevenseventwoqrcvpvvrdljfone3'))