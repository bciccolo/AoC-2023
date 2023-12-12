def count_arrangements(pattern, groups):
    count = 0

    total_springs = sum(groups)
    total_hashes = pattern.count('#')
    total_questions = pattern.count('?')

    # Possible optimization: Eliminate impossible spots

    # print(pattern + ': ' + str(groups))
    # print('Total springs: ' + str(total_springs))
    # print('Total spots: ' + str(total_questions))

    for i in range(2 ** total_questions):
        bits = bin(i)[2:].zfill(total_questions)
        if bits.count('1') + total_hashes == total_springs:
            # print(bits)
            test_arrangement = ''
            for c in pattern:
                if c == '?':
                    if bits[0] == '1':
                        test_arrangement += '#'
                    else:
                        test_arrangement += '.'
                    bits = bits[1:]
                else:
                    test_arrangement += c
            chunks = [len(chunk) for chunk in test_arrangement.split('.') if len(chunk) > 0]
            if chunks == groups:
                # print(chunks)
                count += 1

    return count


total = 0
file = open('day12.dat', 'r')
for line in file.readlines():
    line = line.strip()

    if line == '':
        break

    parts = line.split()
    pattern = parts[0]
    groups = [int(x) for x in parts[1].split(',')]

    total += count_arrangements(pattern, groups)

print('Part 1: ' + str(total))
