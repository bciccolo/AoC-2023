def process_pattern(pattern):
    total = 0
    count = 0

    # Horizontal reflection
    for i in range(len(pattern) - 1):
        if pattern[i] == pattern[i + 1]:
            found = True
            top = i - 1
            bottom = i + 2
            while top >= 0 and bottom < len(pattern):
                if not pattern[top] == pattern[bottom]:
                    found = False
                    break
                top -= 1
                bottom += 1

            if found:
                count +=1
                total += 100 * (i + 1)

    # Vertical reflection
    for i in range(len(pattern[0]) - 1):
        column_1 = [row[i] for row in pattern]
        column_2 = [row[i + 1] for row in pattern]
        if column_1 == column_2:
            found = True
            left = i - 1
            right = i + 2
            while left >= 0 and right < len(pattern[0]):
                column_1 = [row[left] for row in pattern]
                column_2 = [row[right] for row in pattern]
                if not column_1 == column_2:
                    found = False
                    break
                left -= 1
                right += 1

            if found:
                count +=1
                total += i + 1

    # This case never printed anything...
    if count > 1:
        print("\n".join(pattern))

    return total


total = 0
pattern = []
file = open('day13.dat', 'r')
for line in file.readlines():
    line = line.strip()

    if line == '':
        total += process_pattern(pattern)
        pattern.clear()
    else:
        pattern.append(line)

# Fencepost
total += process_pattern(pattern)

print('Part 1: ' + str(total))