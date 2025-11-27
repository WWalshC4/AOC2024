#!/usr/bin/env python3

import os

inputFile = open("./input.txt", "r")
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
# totalAntinodes == 14
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

    an1 = [a2[0] + xDiff, a2[1] + yDiff]
    an2 = [a1[0] - xDiff, a1[1] - yDiff]

    an1Valid = True
    an2Valid = True
    if an1[0] < 0 or an1[0] >= maxX:
        an1Valid = False
    if an1[1] < 0 or an1[1] >= maxY:
        an1Valid = False
    if an2[0] < 0 or an2[0] >= maxX:
        an2Valid = False
    if an2[1] < 0 or an2[1] >= maxY:
        an2Valid = False

    if an1Valid:
        if not letter in antinodeLocations:
            antinodeLocationsByLetter[letter] = []
        if not an1 in antinodeLocationsByLetter[letter]:
            antinodeLocationsByLetter[letter].append(an1)
        if not an1 in antinodeLocations:
            antinodeLocations.append(an1)

    if an2Valid:
        if not letter in antinodeLocations:
            antinodeLocationsByLetter[letter] = []
        if not an2 in antinodeLocationsByLetter[letter]:
            antinodeLocationsByLetter[letter].append(an2)
        if not an2 in antinodeLocations:
            antinodeLocations.append(an2)


antinodeLocationsByLetter = {}
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
