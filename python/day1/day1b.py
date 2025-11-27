#!/usr/bin/env python3

import os

inputFile = open("./python/day1/input.txt", "r")
data = inputFile.read()
inputFile.close()

test = """3   4
4   3
2   5
1   3
3   9
3   3"""
# totalSimilarity == 31
# data = test

left = []
right = []

lines = data.splitlines()
for line in lines:
    locationIds = line.split()
    left.append(locationIds[0])
    right.append(locationIds[1])

rightCount = {}

for num in right:
    if num in rightCount:
        rightCount[num] += 1
    else:
        rightCount[num] = 1


totalSimilarity = 0
for i, leftElement in enumerate(left):
    similarity = 0
    if leftElement in rightCount:
        similarity = int(leftElement) * rightCount[leftElement]
    totalSimilarity += similarity

print(totalSimilarity)
