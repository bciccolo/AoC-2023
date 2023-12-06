file = open('day6.dat', 'r')
lines = [line.strip() for line in file.readlines()]

times = [int(x) for x in lines[0].split(':')[1].split()]
distances = [int(x) for x in lines[1].split(':')[1].split()]

winning_options = 1
for i in range(len(times)):
    time = times[i]
    distance = distances[i]

    count = 0
    for j in range(time + 1):
        # print('Hold time: ' + str(j) + ', distance: ' + str(2 * j * (time - j)))
        if j * (time - j) > distance:
            count += 1

    winning_options *= count
    # print('Race ' + str(i) + ' has ' + str(count) + ' winning options')

    count = 0

print('Part 1: ' + str(winning_options))
print('Part 2: ' + str(0))