file = open('day4.txt', 'r')
lines = file.readlines()

sum = 0
for line in lines:
    line = line.strip()

    groups = line.split(':')[1].split('|')
    winning_numbers = [int(n) for n in groups[0].split()]
    my_numbers = [int(n) for n in groups[1].split()]

    round = 0

    for winning_number in winning_numbers:
        if winning_number in my_numbers:
            if round == 0:
                round = 1
            else:
                round *= 2

    sum += round

file.close()

print('Part 1: '  + str(sum))