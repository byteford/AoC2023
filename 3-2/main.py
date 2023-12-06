#! /usr/bin/python3

import re
import string

symbles = ["*"]

def load_file(file_name):
    with open(file_name,'r') as input:
        return input.read()

def string_to_line(input):
    return input.splitlines()

def next_index(indexX,lenY):
    indexX += 1
    if indexX >= lenY:
        return True, indexX
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
    hit = []
    try:
        if lines[y][x] == "*":
            hit.append({"x": x, "y": y})
            #return True, x,y 
    except IndexError:
        pass
    try:
        if lines[y-1][x]== "*":
            hit.append({"x": x, "y": y-1})
            #return True, x, y-1
    except IndexError:
        pass
    try:
        if lines[y+1][x]== "*":
            hit.append({"x": x, "y": y+1})
            #return True, x, y+1
    except IndexError:
        pass
    return hit


def is_adjacent_to_numnber(input, endx,endy,lines):

    ####to check
    ####  #####
    ####  #000#
    ####  #####
    hit = []
    for i in range(len(input)+2):
        hit += (check_row(endx-i,endy,lines))
    print(hit)
    return hit

def main(file):
    input = load_file(file)
    lines = string_to_line(input)
    sum = 0
    gears = {}
    print("lines:",len(lines))
    for i in range(len(lines)):
        eol = False
        endx = -1
        while not eol:
            eol, endx, output = next_number(endx,i,lines)
            if output == "":
                break
            
            hit =  is_adjacent_to_numnber(output, endx,i,lines)
            for loc in hit:
                print("X:",endx,"Y:",i,"output:", output, "eol:", eol)
                print("hit:",hit,"X:",loc["x"],"Y",loc["y"])

                if str(loc["x"])+"-"+str(loc["y"]) in gears.keys():
                    #sum += gears[str(x)+"-"+str(y)]["1"]* int(output)
                    print("valid")
                    gears[str(loc["x"])+"-"+str(loc["y"])]["gears"].append(int(output))
                    gears[str(loc["x"])+"-"+str(loc["y"])]["valid"] = True
                    #gears[str(x)+"-"+str(y)].append(int(output))
                else:
                    gears[str(loc["x"])+"-"+str(loc["y"])] = {"gears": [int(output)], "valid": False}
                    #gears[str(x)+"-"+str(y)] = [int(output)]
                #sum += int(output)
    validGears = 0
    for i in gears:
        print(gears[i])
        total = 1
        if not gears[i]["valid"]:
            continue
        for val in gears[i]["gears"]:
            total *= val
        validGears += 1
        print(total)
        sum += total
    print(validGears)
    print(len(gears))
    return sum

if __name__ == "__main__":
    print(main("input.txt"))