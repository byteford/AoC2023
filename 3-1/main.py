#! /usr/bin/python3

import re
import string

symbles = string.punctuation.replace('.','')#["*","#","+","$","=","%","%","@","/", "-"]

def load_file(file_name):
    with open(file_name,'r') as input:
        return input.read()

def string_to_line(input):
    return input.splitlines()

def next_index(indexX,lenY):
    indexX += 1
    if indexX >= lenY:
        return True, -1
    return False, indexX

def next_number(indexX, indexY, input):
    eol, indexX = next_index(indexX,len(input[indexY]))
    if eol:
        return True, 0,""
    output = ""
    is_diget = True
    c = input[indexY][indexX]
    is_diget =  c.isdigit()
    while not is_diget:
        eol, indexX = next_index(indexX,len(input[indexY]))
        if eol:
            return True, 0,output
        c = input[indexY][indexX]
        is_diget =  c.isdigit()
    while is_diget:
        output += c
        eol, indexX = next_index(indexX,len(input[indexY]))
        if eol:
            return True, indexX, output
        
        c = input[indexY][indexX]
        is_diget =  c.isdigit()
    return False, indexX, output

def check_row(x,y,lines):
    try:
        if lines[y][x] in symbles:
            print(lines[y][x])
            return True
    except IndexError:
        pass
    try:
        if lines[y-1][x] in symbles:
            print(lines[y-1][x])
            return True
    except IndexError:
        pass
    try:
        if lines[y+1][x] in symbles:
            print(lines[y+1][x])
            return True
    except IndexError:
        pass
    return False


def is_adjacent_to_numnber(input, endx,endy,lines):

    ####to check
    ####  #####
    ####  #000#
    ####  #####

    for i in range(len(input)+2):
        if check_row(endx-i,endy,lines):
            return True
    return False

def main(file):
    input = load_file(file)
    lines = string_to_line(input)
    sum = 0
    print("lines:",len(lines))
    for i in range(len(lines)):
        eol = False
        endx = -1
        while not eol:
            eol, endx, output = next_number(endx,i,lines)
            if output == "":
                break
            print("X:",endx,"Y:",i,"output:", output, "eol:", eol)
            if is_adjacent_to_numnber(output, endx,i,lines):
                sum += int(output)
                print("symbole")
    return sum

if __name__ == "__main__":
    print(main("input.txt"))