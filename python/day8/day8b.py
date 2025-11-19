#!/usr/bin/env python3

import os

inputFile = open("./python/day8/input.txt", "r")
data = inputFile.read()
inputFile.close()

test = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
# totalAntinodes == 34
# data = test

grid = []

antennas = {}

lines = data.splitlines()

for line in lines:
    gridline = list(line)
    grid.append(gridline)

for yPos, row in enumerate(grid):
    for xPos, letter in enumerate(row):
        if letter != ".":
            if not letter in antennas:
                antennas[letter] = []
            antennas[letter].append([xPos, yPos])

maxY = len(grid)
maxX = len(grid[0])


def calculateAntinodes(letter, a1, a2):
    xDiff = a2[0] - a1[0]
    yDiff = a2[1] - a1[1]

    integerRatio = (xDiff % yDiff == 0 or yDiff % xDiff == 0) and (
        xDiff > 1 and yDiff > 1
    )

    if integerRatio:
        print(xDiff, yDiff, integerRatio)

    x = a1[0]
    y = a1[1]

    while x >= 0 and x < maxX and y >= 0 and y < maxY:
        antinode = [x, y]
        if not antinode in antinodeLocations:
            antinodeLocations.append(antinode)
        x -= xDiff
        y -= yDiff

    x = a2[0]
    y = a2[1]

    while x >= 0 and x < maxX and y >= 0 and y < maxY:
        antinode = [x, y]
        if not antinode in antinodeLocations:
            antinodeLocations.append(antinode)
        x += xDiff
        y += yDiff


antinodeLocations = []

for letter in antennas:
    if len(antennas[letter]) < 2:
        continue
    for i, a1 in enumerate(antennas[letter]):
        for j in range(i + 1, len(antennas[letter])):
            a2 = antennas[letter][j]
            calculateAntinodes(letter, a1, a2)

for location in antinodeLocations:
    grid[location[1]][location[0]] = "#"

for line in grid:
    print("".join(line))

totalAntinodes = len(antinodeLocations)

print(totalAntinodes)
