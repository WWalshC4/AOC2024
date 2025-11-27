#!/usr/bin/env python3

import os

inputFile = open("./python/day4/input.txt", "r")
data = inputFile.read()
inputFile.close()

test = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
# totalCount == 18
# data = test

totalCount = 0

grid = []

lines = data.splitlines()

for line in lines:
    gridline = list(line)
    grid.append(gridline)


def checkDirection(xDelta, yDelta, xPos, yPos):
    if xDelta == 0 and yDelta == 0:
        return False
    for i in range(1, 4):
        newXPos = (i * xDelta) + xPos
        newYPos = (i * yDelta) + yPos

        if newXPos < 0:
            return False
        if newYPos < 0:
            return False

        if newYPos >= len(grid):
            return False
        row = grid[newYPos]

        if newXPos >= len(row):
            return False
        letter = row[newXPos]

        if i == 1 and letter != "M":
            return False
        if i == 2 and letter != "A":
            return False
        if i == 3 and letter != "S":
            return False
    return True


for yPos, row in enumerate(grid):
    for xPos, letter in enumerate(row):
        if letter == "X":
            for xDelta in range(-1, 2):
                for yDelta in range(-1, 2):
                    xmas = checkDirection(xDelta, yDelta, xPos, yPos)
                    if xmas:
                        totalCount += 1

print(totalCount)
