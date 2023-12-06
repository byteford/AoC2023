#! /usr/bin/python3

import math
import re

#Card x: winning | have

symbles = ["*"]

def load_file(file_name):
    with open(file_name,'r') as input:
        return input.read()

def string_to_line(input):
    return input.splitlines()

def line_to_obj(line):
    print(line)
    split = re.search(r'(?:Card +)([1-9][0-9]?[0-9]?): ((?:(?:[1-9 ])[0-9](?: ))*)(?:\|) ((?:[1-9| ][0-9] ?)*)', line)
    print(split.groups())
    return { "number": split.group(1), "winning": split.group(2).split(" "), "have": split.group(3).split(" ")}

def main(file):
    input = load_file(file)
    lines = string_to_line(input)
    print(lines)
    points = 0
    for line in lines:
        obj = line_to_obj(line)
        print(obj)
        winning = list(set(obj["winning"]).intersection(obj["have"]))
        if '' in winning:
            winning.remove('')
        print(winning)
        if len(winning) > 0:
            print(math.pow(2, len(winning)-1))
            points += math.pow(2, len(winning)-1)
    return points

# 1, 2, 4, 8, 16
# 0 1 2 3
#2, 4, 6, 8, 10

if __name__ == "__main__":
    print(main("input.txt"))