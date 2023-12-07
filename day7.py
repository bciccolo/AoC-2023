from functools import cmp_to_key
from pprint import pprint

FIVE_OF_KIND = 6
FOUR_OF_KIND = 5
FULL_HOUSE = 4
THREE_OF_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0

def compare_hands(h1, h2):
    if h1['value'] == h2['value']:
        for i in range(5):
            h1_card = get_card_value(h1['cards'][i])
            h2_card = get_card_value(h2['cards'][i])
            if not h1_card == h2_card:
                return h2_card - h1_card

    return h2['value'] - h1['value']


def get_card_value(card):
    if card.isdigit():
        return int(card)
    elif card == 'T':
        return 10
    elif card == 'J':
        if jokers:
            return 0
        return 11
    elif card == 'Q':
        return 12
    elif card == 'K':
        return 13
    return 14


def load_hands(file_name):
    hands = []

    file = open(file_name, 'r')
    for line in file.readlines():
        components = line.strip().split()

        cards = components[0]
        bid = int(components[1])

        matches = {}
        for card in cards:
            if card in matches:
                matches[card] += 1
            else:
                matches[card] = 1

        # Boost the best count if we're using jokers
        boost = 0
        if jokers:
            for match, count in matches.items():
                if match == 'J':
                    boost = count
                    break

            if boost > 0:
                matches.pop('J')
                # It's possible the hand was all jokers ('JJJJJ')
                if len(matches) == 0:
                    matches['A'] = 0

        values = list(matches.values())
        values.sort(reverse=True)

        values[0] += boost

        value = HIGH_CARD
        if values[0] == 5:
            value = FIVE_OF_KIND
        elif values[0] == 4:
            value = FOUR_OF_KIND
        elif values[0] == 3 and values[1] == 2:
            value = FULL_HOUSE
        elif values[0] == 3:
            value = THREE_OF_KIND
        elif values[0] == 2 and values[1] == 2:
            value = TWO_PAIR
        elif values[0] == 2:
            value = ONE_PAIR

        hand = {
            'cards': cards,
            'value': value,
            'bid': bid
        }

        hands.append(hand)

    return hands

def get_winnings():
    hands = load_hands('day7.dat')
    # pprint(hands)

    hands.sort(key=cmp_to_key(compare_hands), reverse=True)
    # pprint(hands)

    winnings = 0
    for i, hand in enumerate(hands):
        # print(hand['cards'] + ': ' + str(i + 1) + ' * ' + str(hand['bid']))
        winnings += (i + 1) * hand['bid']

    return winnings


jokers = False
print('Part 1: ' + str(get_winnings()))
jokers = True
print('Part 2: ' + str(get_winnings()))
