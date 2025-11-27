#!/usr/bin/env python3

import os

inputFile = open("./input.txt", "r")
data = inputFile.read()
inputFile.close()

test = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""
# distinctPositions == 41
# data = test

grid = []

lines = data.splitlines()

startingPosFound = False
row = 0
column = 0
for line in lines:
    gridline = list(line)
    grid.append(gridline)
    if not startingPosFound:
        if "^" in gridline:
            startingPosFound = True
            column = gridline.index("^")
        else:
            row += 1

distinctPositions = 0

direction = 0  # 0 = up, 1 = right, 2 = down, 3 = left


def move():
    global distinctPositions
    global direction
    global row
    global column
    if grid[row][column] != "X":
        distinctPositions += 1
        grid[row][column] = "X"
    nextRow = row
    nextColumn = column
    if direction == 0:
        nextRow -= 1
    elif direction == 1:
        nextColumn += 1
    elif direction == 2:
        nextRow += 1
    elif direction == 3:
        nextColumn -= 1

    if nextRow < 0 or nextColumn < 0:
        return False
    if nextRow >= len(grid) or nextColumn >= (len(grid[row])):
        return False

    nextSpace = grid[nextRow][nextColumn]

    if nextSpace == "#":
        direction = direction + 1
        if direction == 4:
            direction = 0
    else:
        row = nextRow
        column = nextColumn

    return True


shouldMove = True
while shouldMove:
    shouldMove = move()

print(distinctPositions)
