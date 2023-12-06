#! /usr/bin/python3

import re

convert = {"one": "1",
      "two": "2",
      "three": "3",
      "four": "4",
      "five": "5",
      "six": "6",
      "seven":"7",
      "eight": "8",
      "nine": "9",
      }
sum = 0

def to_Digit(input):
  if(input.isdigit()):
    return(input)
  return convert[input]

def find_all_digits(input):
  findinfo = '[1-9]|one|two|three|four|five|six|seven|eight|nine'
  res = re.search("({findinfo})((?:.*)({findinfo}))?".format(findinfo=findinfo),input)
  return [res.group(1),res.group(3)]

with open('input.txt', 'r') as input_file:
  input = input_file.read().split()
  for line in input:
    print("input:", line)
    nums = find_all_digits(line)
    print(nums)
    print(nums[0], nums[-1])
    if nums[-1] == None:
      nums[-1] = nums[0]
    calibration = int(str(to_Digit(nums[0])) + str(to_Digit(nums[-1])))
    print(calibration)
    sum += calibration
print(sum)