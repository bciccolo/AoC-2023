X = 1
Y = 0

min_x = 0
max_x = 0

min_y = 0
max_y = 0

segments = []

def calculate_area():
    area = 0

    while len(segments) > 0:
        # HACK remove variable
        overhang = 0

        # Step 1: Find the highest horizontal segment (the one with the smallest Y value)
        top_side = segments[0]
        index = 0
        for i, segment in enumerate(segments):
            if not is_vertical(segment) and segment[Y] < top_side[Y]:
                top_side = segment
                index = i

        top_length = abs(top_side[0][X] - top_side[1][X]) + 1

        # Step 2: Make a box out of the horizontal segment and the shorter of its two vertical
        # neighbors and add it's area to the running total
        left_side = segments[(index - 1) % len(segments)]
        left_length = abs(left_side[0][Y] - left_side[1][Y])

        right_side = segments[(index + 1) % len(segments)]
        right_length = abs(right_side[0][Y] - right_side[1][Y])

        if left_length < right_length:
            area += left_length * top_length

            # Step 3: Adjust the endpoints of the longer vertical side and the shorter vertical side's
            # neighboring horizontal side; remove the top side and the shorter vertical side

            right_side[0][Y] = left_side[0][Y]

            bottom_side = segments[(index - 2) % len(segments)]

            if bottom_side[1][X] < bottom_side[0][X]:
                overhang = bottom_side[0][X] - bottom_side[1][X]
                area += overhang

            bottom_side[1][X] = right_side[0][X]

            segments.remove(top_side)
            segments.remove(left_side)

            print('Box with short left side')
            print(' Top:   ' + str(top_side))
            print(' Left:  ' + str(left_side))
            print(' Area:  ' + str(left_length * top_length))
            print(' Over:  ' + str(overhang))
            print(' Ttl A: ' + str(area))

        elif left_length > right_length:
            area += right_length * top_length

            # Step 3 (again)

            left_side[1][Y] = right_side[1][Y]

            bottom_side = segments[(index + 2) % len(segments)]

            if bottom_side[1][X] < bottom_side[0][X]:
                overhang = bottom_side[0][X] - bottom_side[1][X]
                area += overhang

            bottom_side[0][X] = left_side[0][X]

            segments.remove(top_side)
            segments.remove(right_side)

            print('Box with short right side')
            print(' Top:   ' + str(top_side))
            print(' Right: ' + str(right_side))
            print(' Area:  ' + str(right_length * top_length))
            print(' Over:  ' + str(overhang))
            print(' Ttl A: ' + str(area))

        else:
            area += right_length * top_length

            # Step 3 (again)

            left_left_side = segments[(index - 2) % len(segments)]
            right_right_side = segments[(index + 2) % len(segments)]
            if left_left_side == right_right_side:
                # This is the last square!
                # TODO: not really - we've cut-off lots of segments (areas that are concave opening down)
                #
                # ........F---7........
                # ........|...|........
                # F-------J...|........
                # |...........L---7....
                # |...............|....
                # |...............|....
                # |..............FJ....
                # |..............|.....
                # |..............|.....
                # |..............|.....
                # |..............|.....
                # |.....F-7....F-J..... <<<< Strategy falls apart here
                # |.....|.|....|.......
                # |.....|.L-7..|.......
                # |...F-J...|..|.......
                # |...|.....|..|.......
                # |...|.....|.FJ.......
                # |...|.....|.|........
                # |...|.....|.|........
                # |...|.....L-J........
                # L---J................

                area += top_length
                segments.clear()
            else:
                overhang = max(right_right_side[0][X], right_right_side[1][X]) - min(left_left_side[0][X], left_left_side[1][X]) + 1

                left_left_side[1][X] = right_right_side[1][X]

                overhang -= abs(left_left_side[0][X] - left_left_side[1][X]) + 1
                area += overhang

                segments.remove(top_side)
                segments.remove(left_side)
                segments.remove(right_side)
                segments.remove(right_right_side)

            print('Box with equal sides')
            print(' Top:   ' + str(top_side))
            print(' Sides: ' + str(right_side))
            print(' Area:  ' + str(right_length * top_length))
            print(' Over:  ' + str(overhang))
            print(' Ttl A: ' + str(area))


    return area


def is_vertical(segment):
    return segment[0][X] == segment[1][X]


def load_data(file_name):
    global min_x, max_x, min_y, max_y

    x = 0
    y = 0

    file = open(file_name, 'r')
    lines = file.readlines()

    last_point = [0, 0]

    for line in lines:
        direction, magnitude = parse_line(line)

        if direction == 'U':
            y -= magnitude
        elif direction == 'D':
            y += magnitude
        elif direction == 'L':
            x -= magnitude
        else:
            x += magnitude

        if x < min_x:
            min_x = x

        if x > max_x:
            max_x = x

        if y < min_y:
            min_y = y

        if y > max_y:
            max_y = y

        this_point = [y, x]

        segment = [last_point, this_point]
        segments.append(segment)

        last_point = this_point.copy()


def parse_line(line):
    if parse_method == 1:
        parts = line.split()
        direction = parts[0]
        magnitude = int(parts[1])
    else:
        code = line.split()[2]

        # 0 means R, 1 means D, 2 means L, and 3 means U.
        direction = code[7]
        if direction == '0':
            direction = 'R'
        elif direction == '1':
            direction = 'D'
        elif direction == '2':
            direction = 'L'
        elif direction == '3':
            direction = 'U'

        hex = code[2:7]
        magnitude = int(hex, 16)

    return (direction, magnitude)


parse_method = 1
load_data('day18-snippet-alt.dat')

# for segment in segments:
#     print(segment)

print('Part 2: ' + str(calculate_area())) # 50465