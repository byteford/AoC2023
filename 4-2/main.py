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
    CardsToPlay = {}
    for line in lines:
        obj = line_to_obj(line)
        print(obj)
        winning = list(set(obj["winning"]).intersection(obj["have"]))
        if int(obj["number"]) not in CardsToPlay:
            CardsToPlay[int(obj["number"])] = 0
        CardsToPlay[int(obj["number"])] += 1
        if '' in winning:
            winning.remove('')
        if len(winning) > 0:
            current = int(obj["number"])+1
            for i in range(len(winning)):
                if (current+i) not in CardsToPlay:
                    CardsToPlay[current+i] = 0
                CardsToPlay[current+i] += CardsToPlay[int(obj["number"])]
            print("len:",len(winning),"extra:", CardsToPlay)
    print(CardsToPlay)
    total = 0
    for i in CardsToPlay:
        total += CardsToPlay[i]
    return total



if __name__ == "__main__":
    print(main("input.txt"))