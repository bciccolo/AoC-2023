file = open('day4.txt', 'r')
lines = file.readlines()

sum_part_1 = 0
sum_part_2 = 0
card_number = 0
card_counts = [1] * 213
for line in lines:
    line = line.strip()

    groups = line.split(':')[1].split('|')
    winning_numbers = [int(n) for n in groups[0].split()]
    my_numbers = [int(n) for n in groups[1].split()]

    winnings = 0
    matches = 0
    for winning_number in winning_numbers:
        if winning_number in my_numbers:
            if winnings == 0:
                winnings = 1
            else:
                winnings *= 2
            matches += 1

    sum_part_1 += winnings

    for i in range(matches):
        if i < len(card_counts) - 1:
            card_counts[card_number + 1 + i] += card_counts[card_number]
    # print('card: ' + str(card_number + 1) + ', wins: ' + str(matches) + ': ' + str(card_counts))

    card_number += 1

file.close()

print('Part 1: '  + str(sum_part_1))
print('Part 1: '  + str(sum(card_counts)))