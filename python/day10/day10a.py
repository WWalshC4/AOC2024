#!/usr/bin/env python3

import os

inputFile = open("./input.txt", "r")
data = inputFile.read()
inputFile.close()

test = """125 17"""
# stoneCount25 == 55312
# data = test


def blink(stones):
    newstones = []
    for stone in stones:
        stoneString = str(stone)
        if stone == 0:
            newstones.append(1)
        elif len(stoneString) % 2 == 0:
            half = int(len(stoneString) / 2)
            newstones.append(int(stoneString[:half]))
            newstones.append(int(stoneString[half:]))
        else:
            newstones.append(stone * 2024)
    return newstones


stones = list(map(int, data.split()))

for index in range(25):
    stones = blink(stones)
    # print(stones)

stoneCount25 = len(stones)
print(stoneCount25)
