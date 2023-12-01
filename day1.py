DATA_FILE = 'day1.txt'

DIGIT_NAMES = [ 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def convert_words_to_digits(text):
    updated = ''
    i = 0
    while i < len(text):
        found = False
        for index, name in enumerate(DIGIT_NAMES):
            if text[i:].startswith(name):
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
        print(original + " --> " + line + ' : '  + str(find_number(line)))
        total += find_number(line)

    print(' Part 2: '  + str(total))


# part1()
part2() #54100 - too high

# print(convert_words_to_digits('twongdsevenfivefive3foureightwonn'))
# print(convert_words_to_digits('threesevenseventwoqrcvpvvrdljfone3'))










# def convert_words_to_digits_x(text):
#     updated = ''
#     word = ''
#     for letter in text:
#         print('updated: ' + updated + ", word: "  +  word + ", next leter: " + letter)
#         if letter.isdigit():
#             updated += letter
#             word = ''
#             continue
#         word += letter
#         if word == 'zero':
#             updated += '0'
#             word = ''
#         elif word == 'one':
#             updated += '1'
#             word = ''
#         elif word == 'two':
#             updated += '2'
#             word = ''
#         elif word == 'three':
#             updated += '3'
#             word = ''
#         elif word == 'four':
#             updated += '4'
#             word = ''
#         elif word == 'five':
#             updated += '5'
#             word = ''
#         elif word == 'six':
#             updated += '6'
#             word = ''
#         elif word == 'seven':
#             updated += '7'
#             word = ''
#         elif word == 'eight':
#             updated += '8'
#             word = ''
#         elif word == 'nine':
#             updated += '9'
#             word = ''
#         elif not ('zero'.startswith(word) or \
#                   'one'.startswith(word) or \
#                   'two'.startswith(word) or \
#                   'three'.startswith(word) or \
#                   'four'.startswith(word) or \
#                   'five'.startswith(word) or \
#                   'six'.startswith(word) or \
#                   'seven'.startswith(word) or \
#                   'eight'.startswith(word) or \
#                   'nine'.startswith(word)):
#             updated += word[:-1]
#             word = letter

#     return updated + word
