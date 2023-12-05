"""seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

# It's faster to parse the input this way...
seeds = [int(i) for i in "79 14 55 13".split()]

seed_to_soil = [
  [int(i) for i in "50 98 2".split()],
  [int(i) for i in "52 50 48".split()] 
]
soil_to_fertilizer = [
  [int(i) for i in "0 15 37".split()],
  [int(i) for i in "37 52 2".split()],
  [int(i) for i in "39 0 15".split()] 
]
fertilizer_to_water = [
  [int(i) for i in "49 53 8".split()],
  [int(i) for i in "0 11 42".split()],
  [int(i) for i in "42 0 7".split()],
  [int(i) for i in "57 7 4".split()]
]
water_to_light = [
  [int(i) for i in "88 18 7".split()],
  [int(i) for i in "18 25 70".split()]
]
light_to_temperature = [
  [int(i) for i in "45 77 23".split()],
  [int(i) for i in "81 45 19".split()],
  [int(i) for i in "68 64 13".split()]
]
temperature_to_humudity = [
  [int(i) for i in "0 69 1".split()],
  [int(i) for i in "1 0 69".split()]
]
humidity_to_location = [
  [int(i) for i in "60 56 37".split()],
  [int(i) for i in "56 93 4".split()]
]

def mapper(input_item, which_map):
  for map_line in which_map:
    if( input_item >= map_line[1] and input_item < map_line[1] + map_line[2]):
      diff = input_item - map_line[1]
      return map_line[0]+diff
  return input_item

lowest_location = None

for s in seeds:
  soil = mapper(s, seed_to_soil)
  fertilizer = mapper(soil, soil_to_fertilizer)
  water = mapper(fertilizer, fertilizer_to_water)
  light = mapper(water, water_to_light)
  temperature = mapper(light, light_to_temperature)
  humidity = mapper(temperature, temperature_to_humudity)
  location = mapper(humidity, humidity_to_location)
  print(f"{s} {soil} {fertilizer} {water} {light} {temperature} {humidity} {location}")
  if lowest_location is None or location < lowest_location:
    lowest_location = location
    
print(f"Part One: {lowest_location}")