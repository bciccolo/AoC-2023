X = 0
Y = 1

def calculate_area(file_name, parse_method):
    x = 0
    y = 0

    perimeter = 0
    points = []

    # Load points
    points.append([x, y]) # Starting point

    file = open(file_name, 'r')
    lines = file.readlines()
    for line in lines:
        direction, magnitude = parse_line(line, parse_method)

        perimeter += magnitude

        if direction == 'U':
            y -= magnitude
        elif direction == 'D':
            y += magnitude
        elif direction == 'L':
            x -= magnitude
        else:
            x += magnitude

        points.append([x, y])

    # Shoelace theorem
    sum = 0
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]

        determinant = (x1 * y2) - (y1 * x2)
        sum += determinant

    sum /= 2

    # Add back the perimeter
    sum += perimeter / 2 + 1

    return sum


def parse_line(line, parse_method):
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


file_name = 'day18.dat'

print('Part 1: ' + str(calculate_area(file_name, 1)))
print('Part 2: ' + str(calculate_area(file_name, 2)))