#!/usr/bin/env python3

import os

inputFile = open("./python/day10/input.txt", "r")
data = inputFile.read()
inputFile.close()

test = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
# totalScore == 81
# data = test

grid = []

trailheads = []

lines = data.splitlines()

for line in lines:
    gridline = []
    for letter in line:
        try:
            value = int(letter)
        except:
            value = -1
        gridline.append(value)
    grid.append(gridline)

for yPos, row in enumerate(grid):
    for xPos, height in enumerate(row):
        if height == 0:
            trailheads.append([xPos, yPos])

maxY = len(grid)
maxX = len(grid[0])


def climb(xPos, yPos, peaks):
    currentHeight = grid[yPos][xPos]
    location = [xPos, yPos]
    if currentHeight == 9:
        locationAsString = str(xPos) + ":" + str(yPos)
        if not locationAsString in peaks:
            peaks[locationAsString] = 0
        peaks[locationAsString] += 1
        return
    for xDiff in range(-1, 2):
        for yDiff in range(-1, 2):
            if abs(xDiff) == abs(yDiff):
                continue
            newX = xPos + xDiff
            newY = yPos + yDiff
            if 0 <= newX < maxX and 0 <= newY < maxY:
                nextHeight = grid[newY][newX]
                nextLocation = [newX, newY]
                if nextHeight == currentHeight + 1:
                    climb(newX, newY, peaks)


totalScore = 0

for trailhead in trailheads:
    xPos = trailhead[0]
    yPos = trailhead[1]
    peaks = {}
    climb(xPos, yPos, peaks)
    for peak in peaks:
        totalScore += peaks[peak]

print(totalScore)
