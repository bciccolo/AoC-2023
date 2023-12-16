def count_patterns(pattern, groups, start_pattern_index, start_group_index):
    global cache_hits

    # Note: We have to join the groups with something other than the empty string
    # because otherwise lists like [1,1] and [11] will result in the same string.
    params = pattern[start_pattern_index:] + '|'.join([str(size) for size in groups[start_group_index:]])
    if params in cache:
        cache_hits += 1
        return cache[params]

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
            else:
                updated = pattern[:start].replace('?', '.') + ('#' * group) + '.' + pattern[start + group + 1:]
                count += count_patterns(updated, groups, i + 2, start_group_index + 1)

    cache[params] = count

    return count


def solve(unfold):
    total = 0

    file = open('day12.dat', 'r')
    for line in file.readlines():
        parts = line.split()

        pattern = parts[0]
        if (unfold > 1):
            pattern += '?'
            pattern *= unfold
            pattern = pattern[:-1]

        original = [int(x) for x in parts[1].split(',')]
        groups = []
        for _ in range(unfold):
            groups.extend(original)

        count = count_patterns(pattern, groups, 0, 0)
        total += count

    return total


cache = {}
cache_hits = 0
print('Part 1: ' + str(solve(1))) # 7191
print('Part 2: ' + str(solve(5))) # 6512849198636
print('Cache hits: ' + str(cache_hits))