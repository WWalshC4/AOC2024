#!/usr/bin/env python3

import os
import re
import math

inputFile = open("./python/day3/input.txt", "r")
data = inputFile.read()
inputFile.close()

test = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
# total == 161
# data = test

lines = data.splitlines()

total = 0

for line in lines:
    validMuls = re.findall(r"mul\((\d+)\,(\d+)\)", line)
    for validMul in validMuls:
        ints = list(map(int, validMul))
        result = math.prod(ints)
        total += result

print(total)
