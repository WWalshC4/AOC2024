#!/usr/bin/env python3

import os
import re
import math

inputFile = open("./python/day3/input.txt", "r")
data = inputFile.read()
inputFile.close()

test = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
# total == 48
# data = test

lines = data.splitlines()

total = 0

include = True

pattern = r"((don\'t\(\))|(do\(\)))|mul\((\d+)\,(\d+)\)"

for line in lines:
    for match in re.finditer(pattern, line):
        token = match.group()
        if token == "do()":
            include = True
        elif token == "don't()":
            include = False
        elif token.startswith("mul("):
            values = re.search(r"mul\((\d+)\,(\d+)\)", token)
            ints = list(map(int, values.groups()))
            result = math.prod(ints)
            if include:
                total += result

print(total)
