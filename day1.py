DIGIT_NAMES = [ 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# This updated solution to find the number in one pass of the text
# (versus reading from the left and then again from the right) was
# inspired by Neil Thistlethwaite (https://www.youtube.com/watch?v=R8qGPFRksCY)
#
# NOTE: I got both stars for this puzzle BEFORE using Neil's algorithm :)
def find_number(text, consider_names):
    first = 0
    last = 0
    i = 0
    while i < len(text):
        if text[i].isdigit():
            if first == 0:
                first = int(text[i])
            last = int(text[i])

        if consider_names:
            for index, name in enumerate(DIGIT_NAMES):
                if text[i:i + len(name)] == name:
                    if first == 0:
                        first = index
                    last = index

        i += 1

    return first * 10 + last


file = open('day1.dat', 'r')
lines = file.readlines()

total_part_1 = 0
total_part_2 = 0
for line in lines:
    total_part_1 += find_number(line, False)
    total_part_2 += find_number(line, True)

print('Part 1: '  + str(total_part_1))
print('Part 2: '  + str(total_part_2))