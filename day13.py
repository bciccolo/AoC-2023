MATCH = 0
SMUDGE = 1

def match(value_1, value_2, must_fix_smudge, did_fix_smudge):
    if value_1 == value_2:
        return (True, False)
    elif must_fix_smudge and not did_fix_smudge:
        count = 0
        for i in range(len(value_1)):
            if not value_1[i] == value_2[i]:
                count += 1
        if count == 1:
            return (True, True)

    return (False, False)

def process_pattern(pattern, must_fix_smudge):
    # Horizontal reflection
    for i in range(len(pattern) - 1):
        did_fix_smudge = False
        result = match(pattern[i], pattern[i + 1], must_fix_smudge, did_fix_smudge)
        if result[MATCH]:
            if result[SMUDGE]:
                did_fix_smudge = True
            found = True
            top = i - 1
            bottom = i + 2
            while top >= 0 and bottom < len(pattern):
                result = match(pattern[top], pattern[bottom], must_fix_smudge, did_fix_smudge)
                if not result[MATCH]:
                    found = False
                    break
                elif result[SMUDGE]:
                    did_fix_smudge = True
                top -= 1
                bottom += 1

            if (found and not must_fix_smudge) or (found and must_fix_smudge and did_fix_smudge):
                return 100 * (i + 1)

    # Vertical reflection
    for i in range(len(pattern[0]) - 1):
        did_fix_smudge = False
        column_1 = [row[i] for row in pattern]
        column_2 = [row[i + 1] for row in pattern]
        result = match(column_1, column_2, must_fix_smudge, did_fix_smudge)
        if result[MATCH]:
            if result[SMUDGE]:
                did_fix_smudge = True
            found = True
            left = i - 1
            right = i + 2
            while left >= 0 and right < len(pattern[0]):
                column_1 = [row[left] for row in pattern]
                column_2 = [row[right] for row in pattern]
                result = match(column_1, column_2, must_fix_smudge, did_fix_smudge)
                if not result[MATCH]:
                    found = False
                    break
                elif result[SMUDGE]:
                    did_fix_smudge = True
                left -= 1
                right += 1

            if (found and not must_fix_smudge) or (found and must_fix_smudge and did_fix_smudge):
                return i + 1

    # Something went wrong - we did not find the reflection!
    return -1_000_000


total_part_1 = 0
total_part_2 = 0
pattern = []
file = open('day13.dat', 'r')
for line in file.readlines():
    line = line.strip()

    if line == '':
        total_part_1 += process_pattern(pattern, False)
        total_part_2 += process_pattern(pattern, True)
        pattern.clear()
    else:
        pattern.append(line)

# Fencepost
total_part_1 += process_pattern(pattern, False)
total_part_2 += process_pattern(pattern, True)

print('Part 1: ' + str(total_part_1))
print('Part 2: ' + str(total_part_2))