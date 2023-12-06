#! /usr/bin/python3

import re

max = {
        "blue": 14,
        "red":12,
        "green":13,
        }

def load_file(file_name):
    with open(file_name,'r') as input:
        return input.read()

def string_to_line(input):
    return input.split('\n')

def line_to_obj(input):
    print(input)
    return {
        "blue": find_biggest_colour(input, "blue"),
        "red":find_biggest_colour(input, "red"),
        "green":find_biggest_colour(input, "green"),
        }

def find_biggest_colour(input, colour):
    print(colour)
    col = re.findall("(([1-9][0-9]?) (?:{colour}))".format(colour=colour), input)
    biggest = 0
    for i in col:
        match = int(i[1])
        print(match)
        if match > biggest:
            biggest = match
    return biggest

def get_game_number(input):
    game = re.search("(?:Game )(.*)(?::)",input)
    return int(game.group(1))

def main(file):
    input = load_file(file)
    lines = string_to_line(input)
    total_possable = 0
    for line in lines:
        obj = line_to_obj(line)
        print(obj)
        possable = True
        for key in  max.keys():
            if max[key] < obj[key]:
                print("max")
                possable = False
                break
        if possable == True:
            total_possable += get_game_number(line)
    return total_possable


print(main("input.txt"))