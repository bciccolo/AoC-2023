seeds = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

def convert_source_to_destination(value, lookup_map):
    for entry in lookup_map:
        dest, source, range = entry

        if value >= source and value < source + range:
            return value + (dest - source)

    return value


def load_data(file):
    global seeds

    file = open(file, 'r')
    lines = file.readlines()

    blank_counter = 0
    for line in lines:
        line = line.strip()

        if line == '':
            blank_counter += 1
            continue


        if blank_counter == 0:
            seeds = [int(x.strip()) for x in line.split(':')[1].split()]
        else:
            # Skip map header
            if not line[0].isdigit():
                continue

            range = [int(x.strip()) for x in line.split()]

            if blank_counter == 1:
                seed_to_soil.append(range)
            elif blank_counter == 2:
                soil_to_fertilizer.append(range)
            elif blank_counter == 3:
                fertilizer_to_water.append(range)
            elif blank_counter == 4:
                water_to_light.append(range)
            elif blank_counter == 5:
                light_to_temperature.append(range)
            elif blank_counter == 6:
                temperature_to_humidity.append(range)
            elif blank_counter == 7:
                humidity_to_location.append(range)


def part_1():
    min_location = -1
    for seed in seeds:
        soil = convert_source_to_destination(seed, seed_to_soil)
        fertilizer = convert_source_to_destination(soil, soil_to_fertilizer)
        water = convert_source_to_destination(fertilizer, fertilizer_to_water)
        light = convert_source_to_destination(water, water_to_light)
        temperature = convert_source_to_destination(light, light_to_temperature)
        humidity = convert_source_to_destination(temperature, temperature_to_humidity)
        location = convert_source_to_destination(humidity, humidity_to_location)
        if min_location == -1 or location < min_location:
            min_location = location

        # print('Seed ' + str(seed) + ', ' +
        #       'soil ' + str(soil) + ', ' +
        #       'fertilizer ' + str(fertilizer) + ', ' +
        #       'water ' + str(water) + ', ' +
        #       'light ' + str(light) + ', ' +
        #       'temperature ' + str(temperature) + ', ' +
        #       'humidity ' + str(humidity) + ', ' +
        #       'location ' + str(location))

    print('Part 1: ' + str(min_location))

load_data('day5.dat')
# print(seeds)
# print(seed_to_soil)
# print(soil_to_fertilizer)
# print(fertilizer_to_water)
# print(water_to_light)
# print(light_to_temperature)
# print(temperature_to_humidity)
# print(humidity_to_location)

part_1()