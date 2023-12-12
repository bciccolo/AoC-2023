def count_winning_options(times, distances):
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

    return winning_options


file = open('day6.dat', 'r')
lines = [line.strip() for line in file.readlines()]

# Part 1
times = [int(x) for x in lines[0].split(':')[1].split()]
distances = [int(x) for x in lines[1].split(':')[1].split()]
print('Part 1: ' + str(count_winning_options(times, distances)))

# Part 2
times = [int(lines[0].split(':')[1].replace(' ', ''))]
distances = [int(lines[1].split(':')[1].replace(' ', ''))]
# print('Part 2: ' + str(count_winning_options(times, distances)))

"""
time = 56717999
distance = 334113513502430
(time - x) * x > distance, where 0 <= x <= time

0 = - x^2 + tx - d
"""
import math

a = -1
b = 56717999            # Fill in time number from user input
c = -334113513502430    # Fill in distance number from user input

discriminant = math.sqrt(b ** 2 - 4 * a * c)
root_1 = int((-b - discriminant) / (2 * a))
root_2 = int((-b + discriminant) / (2 * a))

print('Part 2: ' + str(abs(root_1 - root_2)))