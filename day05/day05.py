import sys

lines = []
seeds = []
seed_ranges = []
seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temperature = []
temperature_to_humidity = []
humidity_to_location = []

input_file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(input_file, 'r') as file:
    for line in file:
        lines.append(line.strip('\n'))

for i, l in enumerate(lines):
    if l == '':
        continue

    if 'seeds:' in l:
        seeds = [int(s) for s in l.strip().split(':')[1].split()]
        k = 0
        while k+1 < len(seeds):
            start, length = seeds[k], seeds[k+1]
            seed_ranges.append((start, start + length))
            k += 2

    if l == 'seed-to-soil map:':
        j = i+1
        while j < len(lines) and lines[j].strip() != '':
            destination_start, source_start, range_length = lines[j].split()
            seed_to_soil.append((int(source_start), int(destination_start), int(range_length)))
            j += 1

    if l == 'soil-to-fertilizer map:':
        j = i+1
        while j < len(lines) and lines[j].strip() != '':
            destination_start, source_start, range_length = lines[j].split()
            soil_to_fertilizer.append((int(source_start), int(destination_start), int(range_length)))
            j += 1

    if l == 'fertilizer-to-water map:':
        j = i+1
        while j < len(lines) and lines[j].strip() != '':
            destination_start, source_start, range_length = lines[j].split()
            fertilizer_to_water.append((int(source_start), int(destination_start), int(range_length)))
            j += 1

    if l == 'water-to-light map:':
        j = i+1
        while j < len(lines) and lines[j].strip() != '':
            destination_start, source_start, range_length = lines[j].split()
            water_to_light.append((int(source_start), int(destination_start), int(range_length)))
            j += 1

    if l == 'light-to-temperature map:':
        j = i+1
        while j < len(lines) and lines[j].strip() != '':
            destination_start, source_start, range_length = lines[j].split()
            light_to_temperature.append((int(source_start), int(destination_start), int(range_length)))
            j += 1

    if l == 'temperature-to-humidity map:':
        j = i+1
        while j < len(lines) and lines[j].strip() != '':
            destination_start, source_start, range_length = lines[j].split()
            temperature_to_humidity.append((int(source_start), int(destination_start), int(range_length)))
            j += 1

    if l == 'humidity-to-location map:':
        j = i+1
        while j < len(lines) and lines[j].strip() != '':
            destination_start, source_start, range_length = lines[j].split()
            humidity_to_location.append((int(source_start), int(destination_start), int(range_length)))
            j += 1


def getInRange(mapping, key):
    for ranges in mapping:
        start, end, length = ranges
        if key >= start and key < start + length:
            return end + (key - start)

    return key

def answer1():
    answer = 1 << 32
    for seed in seeds:
        soil = getInRange(seed_to_soil, seed)
        fertilizer = getInRange(soil_to_fertilizer, soil)
        water = getInRange(fertilizer_to_water, fertilizer)
        light = getInRange(water_to_light, water)
        temperature = getInRange(light_to_temperature, light)
        humidity = getInRange(temperature_to_humidity, temperature)
        location = getInRange(humidity_to_location, humidity)
        answer = min(int(location), answer)
    return answer


def answer2():
    answer = 1 << 32
    for seed_range in seed_ranges:
        for s in range(*seed_range):
            soil = getInRange(seed_to_soil, s)
            fertilizer = getInRange(soil_to_fertilizer, soil)
            water = getInRange(fertilizer_to_water, fertilizer)
            light = getInRange(water_to_light, water)
            temperature = getInRange(light_to_temperature, light)
            humidity = getInRange(temperature_to_humidity, temperature)
            location = getInRange(humidity_to_location, humidity)
            answer = min(int(location), answer)
    return answer


print(answer1())
print(answer2())
