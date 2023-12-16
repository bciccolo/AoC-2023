import re

def count_arrangements(pattern, groups):
    count = 0

    # print()
    # print('Groups: ' + str(groups))

    # print('Original pattern: ' + pattern)
    # print('Original range: ' + str(2 ** pattern.count('?')))

    # pattern = pre_process(pattern, groups)
    # print('Reduced pattern: ' + pattern)

    total_springs = sum(groups)
    total_hashes = pattern.count('#')
    total_questions = pattern.count('?')

    # print(pattern + ': ' + str(groups))
    # print('Total springs: ' + str(total_springs))
    # print('Total spots: ' + str(total_questions))

    # print('Reduced range: ' + str(2 ** total_questions))

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


def pre_process(pattern, groups):
    reduced_pattern = pattern

    required = 0
    target = groups[0]
    for token in reduced_pattern:
        if token == '#':
            required += 1

        if required > 0:
            pass

    return pattern


def compatible_dot(candidate, required):
    i = 0
    while i < len(candidate) and i < len(groups):
        if candidate[i] < required[i]:
            return False
        i += 1

    return True


def compatible_hash(candidate, required):
    i = 0
    while i < len(candidate) and i < len(groups):
        if candidate[i] > required[i]:
            return False
        i += 1

    return True


def pre_process_bad(pattern, groups):
    reduced_pattern = pattern

    question_indices = []
    for i, token in enumerate(pattern):
        if token == '?':
            question_indices.append(i)

    # Try putting an # in the next ? and see if we invalidate any of the groups
    for index in question_indices:
        x = list(reduced_pattern)

        x[index] = '#'
        test = ''.join(x)
        chunks = [len(chunk) for chunk in re.split('[\?\.]',test) if len(chunk) > 0]
        if not compatible_hash(chunks, groups):
            x[index] = '.'
            reduced_pattern = ''.join(x)
        else:
            # Try putting an . in the next ? and see if we invalidate any of the groups
            x[index] = '.'
            test = ''.join(x)
            chunks = [len(chunk) for chunk in re.split('[\?\.]',test) if len(chunk) > 0]
            if not compatible_dot(chunks, groups):
                x[index] = '#'
                reduced_pattern = ''.join(x)




    # There's something we can do to compare these possible 'chunks' to the actual 'groups'
    # chunks = [len(chunk) for chunk in reduced_pattern.split('.') if len(chunk) > 0]
    # chunks = [len(chunk) for chunk in re.split('[\?\.]', reduced_pattern) if len(chunk) > 0]
    # print(chunks)

    # Eliminate impossible spots


    # index = 0
    # run = ''
    # next_group = groups[0]
    # for token in pattern:
    #     if token == '.':
    #         reduced_pattern += '.'
    #         if len(run) > 0:
    #             next_group = groups[index]
    #             run = ''
    #             index += 1
    #     else:
    #         run += token




    return reduced_pattern


unfold = 1

# total = 0
# file = open('day12-snippet.dat', 'r')
# for line in file.readlines():
#     line = line.strip()

#     if line == '':
#         break

#     parts = line.split()
#     pattern = parts[0]
#     if (unfold > 1):
#          pattern += '?'
#          pattern *= 5
#          pattern = pattern[:-1]

#     original = [int(x) for x in parts[1].split(',')]
#     groups = []
#     for i in range(unfold):
#         groups.extend(original)

#     # print(pattern)
#     # print(groups)

#     total += count_arrangements(pattern, groups)

# print('Part 1: ' + str(total))

def compatible(candidate, groups):
    start = 0
    for group in groups:
        hashes = ''
        for i in range(start, len(candidate)):
            if candidate[i] == '.':
                if len(hashes) > 0:
                    hashes = ''
                    start = 1
                    break
            elif candidate[i] == '#':
                hashes += candidate[i]

            if len(hashes) > group:
                return False

    return True


def analyze_pattern(pattern, groups):
    reduced = list(pattern)

    for i, token in enumerate(pattern):
        if token == '?':
            reduced[i] = '#'
            if not compatible(reduced, groups):
                reduced[i] = '.'
                if not compatible(reduced, groups):
                    reduced[i] = '?'

    print('Original: ' + pattern + ' has ' + str(2 ** pattern.count('?')) + ' possibilities')
    print('Reduced:  ' + ''.join(reduced) + ' has ' + str(2 ** ''.join(reduced).count('?')) + ' possibilities')


# analyze_pattern('?#?#?#?#?#?#?#?', [1, 3, 1, 6])




def count_patterns(pattern, groups, start_pattern_index, start_group_index):
    group = groups[start_group_index]

    count = 0

    i = start_pattern_index
    # Chew through any leading '.' characters
    while i < len(pattern) and  pattern[i] == '.':
        i += 1

    # Limit of range is location of the next '#' or end of pattern
    stop = pattern.find('#', i)
    if stop == -1:
        stop = len(pattern)
    else:
        stop += 1
    for x in range(i, stop):
        i = x
        possible = True

        # See if we can fit the group in what's left of pattern (until we hit a '.')
        if i + group > len(pattern):
            possible = False

        # Range cannot contain a '.'
        if possible:
            start = i
            for i in range(i, i + group):
                if pattern[i] == '.':
                    possible = False
                    break

        # Boundaries cannot contain a '#'
        if possible:
            if start > 0 and pattern[start - 1] == '#':
                possible = False

            # HERE - necessary check?
            # if start_group_index < len(groups) - 1:
            if i + 1 < len(pattern) and pattern[i + 1] == '#':
                possible = False

        # Remainder cannot be a '#' if this is the last group
        if possible:
            if start_group_index == len(groups) - 1:
                if '#' in pattern[i + 1:]:
                    possible = False

        if possible:
            if start_group_index == len(groups) - 1:
                count += 1
                # print(pattern[:start].replace('?', '.') + ('#' * group) + '.' + pattern[start + group + 1:])
            else:
                updated = pattern[:start].replace('?', '.') + ('#' * group) + '.' + pattern[start + group + 1:]
                count += count_patterns(updated, groups, i + 2, start_group_index + 1)

    return count


# print(count_patterns('?#?#?#?#?#?#?#?', [1, 3, 1, 6], 0, 0))
# print(count_patterns('?###????????', [3, 2, 1], 0, 0))
# print(count_patterns('.??..??...?##.', [1,1,3], 0, 0))
# print(count_patterns('??#??????#???.?', [4,3], 0, 0))

# print(count_patterns('????????#????????.', [1,1,2,1,3], 0, 0))
# print(count_arrangements('????????#????????.', [1,1,2,1,3]))

# print(count_patterns('#????###???????#?', [3,3,1,4], 0, 0))
# print(count_arrangements('#????###???????#?', [3,3,1,4]))

# print(count_patterns('#??#?#.?.??????', [6,1,5], 0, 0))
# print(count_arrangements('#??#?#.?.??????', [6,1,5]))

import time
begin = time.time()

total = 0
file = open('day12.dat', 'r')
for line in file.readlines():
    parts = line.split()
    pattern = parts[0]
    groups = [int(x) for x in parts[1].split(',')]

    count = count_patterns(pattern, groups, 0, 0)
    # count = count_arrangements(pattern, groups)
    total += count

duration = time.time() - begin
print('Part 1:   ' + str(total))
print(str(duration) + " seconds")

# Original Algorithm
# Part 1:   7191
# 2.9085021018981934 seconds
# Updated Algorithm
# Part 1:   7191
# 0.0430750846862793 seconds
