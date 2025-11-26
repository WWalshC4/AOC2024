#!/usr/bin/env python3

import os
import re

inputFile = open("./input.txt", "r")
data = inputFile.read()
inputFile.close()

test = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""
# gpsSum == 10092

test2 = """########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>v
v<v>>v<<"""
# gpsSum2 == 2028
# data = test

matches = re.match(r"^([#.O@\n]+?)\n\n([<>^v\n]*)", data)

gridString = matches.group(1)
directionsString = matches.group(2)

grid = []

lines = gridString.splitlines()

for line in lines:
    gridline = list(line)
    grid.append(gridline)

maxY = len(grid)
maxX = len(grid[0])


def findCurrentPosition(grid):
    for yPos, row in enumerate(grid):
        for xPos, occupant in enumerate(row):
            if occupant == "@":
                return xPos, yPos


startingX, startingY = findCurrentPosition(grid)

directions = list("".join(directionsString.split()))
print(startingX, startingY)


def move(xPos, yPos, direction):
    xDiff = 0
    yDiff = 0
    if direction == "<":
        xDiff = -1
    elif direction == ">":
        xDiff = 1
    elif direction == "^":
        yDiff = -1
    elif direction == "v":
        yDiff = 1

    currentOccupant = grid[yPos][xPos]
    targetSpace = grid[yPos + yDiff][xPos + xDiff]

    if targetSpace == "#":
        return False
    elif targetSpace == ".":
        grid[yPos + yDiff][xPos + xDiff] = currentOccupant
        grid[yPos][xPos] = "."
        return True
    else:
        canMove = move(xPos + xDiff, yPos + yDiff, direction)
        if canMove:
            grid[yPos + yDiff][xPos + xDiff] = currentOccupant
            grid[yPos][xPos] = "."
        return canMove


def calculateGPS(grid):
    gpsSum = 0
    for yPos, row in enumerate(grid):
        for xPos, occupant in enumerate(row):
            if occupant == "O":
                gpsSum += (yPos * 100) + xPos

    return gpsSum


currentX = startingX
currentY = startingY
for direction in directions:
    # print("Move: " + direction, currentX, currentY)
    moved = move(currentX, currentY, direction)
    # print("Success: " + str(moved))
    if moved:
        if direction == "<":
            currentX -= 1
        elif direction == ">":
            currentX += 1
        elif direction == "^":
            currentY -= 1
        elif direction == "v":
            currentY += 1

for gridline in grid:
    print("".join(gridline))
gpsSum = calculateGPS(grid)
print(gpsSum)
