def check_all_zeros(numbers):
    for number in numbers:
        if not number == 0:
            return False
    return True


def extrapolate_values(numbers):
    first_numbers = []
    last_numbers = []

    while not check_all_zeros(numbers):
        first_numbers.append(numbers[0])
        last_numbers.append(numbers[len(numbers) - 1])
        diffs = []
        for i in range(len(numbers) - 1):
            diffs.append(numbers[i + 1] - numbers[i])
        # print(diffs)
        numbers = diffs

    # print(first_numbers)
    # print(last_numbers)

    diff_first = 0
    diff_last = 0
    for i in range(len(last_numbers) - 1, -1, -1):
        diff_first = first_numbers[i] - diff_first
        diff_last = last_numbers[i] + diff_last

    # print(diff_first)
    # print(diff_last)

    return (diff_first, diff_last)


part_1 = 0
part_2 = 0
file = open('day9.dat', 'r')
for line in file.readlines():
    numbers = [int(x) for x in line.strip().split()]
    previous, next = extrapolate_values(numbers)

    part_1 += next
    part_2 += previous

print('Part 1: ' + str(part_1))
print('Part 2: ' + str(part_2))