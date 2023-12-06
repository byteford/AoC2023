#! /usr/bin/python3

import re
sum = 0
with open('input.txt', 'r') as input_file:
  input = input_file.read().split()
  for line in input:
    print(line)
    nums = re.findall('[1-9]', line)
    print(nums)
    print(nums[0], nums[-1])
    calibration = int(str(nums[0]) + str(nums[-1]))
    print(calibration)
    sum += calibration
print(sum)