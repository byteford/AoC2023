#! /usr/bin/python3

import math
import re

converter_map = {
    "seed-soil": {},
    "soil-fertilizer": {},
    "fertilizer-water": {},
    "water-light": {},
    "light-temp": {},
    "temp-humid": {},
    "humid-loc": {}
}

def load_file(file_name):
    with open(file_name,'r') as input:
        return input.read()

def input_to_map(input):
    output = re.search(r'(?:seeds: )(.*)(?:\n\n)(?:seed-to-soil map:\n)((?:.*\n)*)(?:soil-to-fertilizer map:\n)((?:.*\n)*)(?:fertilizer-to-water map:\n)((?:.*\n)*)(?:water-to-light map:\n)((?:.*\n)*)(?:light-to-temperature map:\n)((?:.*\n)*)(?:temperature-to-humidity map:\n)((?:.*\n)*)(?:humidity-to-location map:\n)((?:.*\n)*)', input)
    print(output.groups())
    maps = {
        "seeds": output.group(1).split(" "),
        "seed-soil": output.group(2).rstrip().split("\n"),
        "soil-fertilizer": output.group(3).rstrip().split("\n"),
        "fertilizer-water": output.group(4).rstrip().split("\n"),
        "water-light": output.group(5).rstrip().split("\n"),
        "light-temp": output.group(6).rstrip().split("\n"),
        "temp-humid": output.group(7).rstrip().split("\n"),
        "humid-loc": output.group(8).rstrip().split("\n")
    }
    return maps

def load_converter(convter_type, input):
    print(convter_type)
    for i in input:
        print(i)
        lst = i.split(" ")
        print(lst)
        for j in range(int(lst[2])):
            print(j)
            dest = str(int(lst[0])+j)
            source = str(int(lst[1])+j)
            converter_map[convter_type][source] = dest

def load_converters(input):
    for key in input:
        if key != "seeds":
            load_converter(key, input[key])
    print(converter_map)

def get_next_number(number, converter_type):
    if number in converter_map[converter_type].keys():
        print(converter_type, converter_map[converter_type][number], "converted")
        return converter_map[converter_type][number]
    print(converter_type, number, "not converted")
    return number

def seed_location(start_number):
    next_number = get_next_number(start_number,"seed-soil")
    next_number = get_next_number(next_number,"soil-fertilizer")
    next_number = get_next_number(next_number,"fertilizer-water")
    next_number = get_next_number(next_number,"water-light")
    next_number = get_next_number(next_number,"light-temp")
    next_number = get_next_number(next_number,"temp-humid")
    next_number = get_next_number(next_number,"humid-loc")
    print(next_number)
    return next_number

def main(file):
    input = load_file(file)
    print(input)
    maps = input_to_map(input)
    load_converters(maps)
    smallest_amount = math.inf
    smallest_seed = ""
    for seed in maps["seeds"]:
        print(seed)
        localtion = seed_location(seed)
        print("location: ",localtion)
        if int(localtion) < smallest_amount:
            smallest_amount = int(localtion)
            smallest_seed = seed
    return smallest_amount



if __name__ == "__main__":
    print(main("input.txt"))