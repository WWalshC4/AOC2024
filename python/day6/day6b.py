#!/usr/bin/env python3

import os

inputFile = open("./python/day6/input.txt", "r")
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
# len (possibleObstructions) == 6
data = test

grid = []

lines = data.splitlines()

startingPosFound = False
initialRow = 0
initialColumn = 0
for line in lines:
    gridline = list(line)
    grid.append(gridline)
    if not startingPosFound:
        if "^" in gridline:
            startingPosFound = True
            initialColumn = gridline.index("^")
            grid[initialRow][initialColumn] = "1"
        else:
            initialRow += 1

initialDirection = 0  # 0 = up, 1 = right, 2 = down, 3 = left

possibleObstructions = [[initialRow, initialColumn]]

def getChar(currentChar, direction):
    currentByte = 0
    try:
        currentByte = int(currentChar, base=16)
    except:
        currentByte = 0

    currentByte = currentByte | 2 ** (direction)
    return "{:X}".format(currentByte)


def move(direction, row, column):
    thisPos = grid[row][column]
    grid[row][column] = getChar(thisPos, direction)
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
        return dict(shouldMove=False)
    if nextRow >= len(grid) or nextColumn >= (len(grid[row])):
        return dict(shouldMove=False)

    nextPos = grid[nextRow][nextColumn]

    if nextPos == "#":
        nextRow = row
        nextColumn = column
        direction = direction + 1
        if direction == 4:
            direction = 0
    else:
        nextDirection = direction + 1
        if nextDirection == 4:
            nextDirection = 0

        joinsPath = False#checkPath(row, column, nextDirection)

        if joinsPath:
            obstructionLocation = [nextRow, nextColumn]
            if not obstructionLocation in possibleObstructions:
                possibleObstructions.append(obstructionLocation)
        row = nextRow
        column = nextColumn

    return dict(
        shouldMove=True, nextColumn=nextColumn, nextRow=nextRow, nextDirection=direction
    )


shouldMove = True
direction = initialDirection
row = initialRow
column = initialColumn

for r in grid:
    print(r)

while shouldMove:
    ret = move(direction, row, column)
    shouldMove = ret['shouldMove']
    if (shouldMove):
        direction = ret['nextDirection']
        row = ret['nextRow']
        column = ret['nextColumn']

for r in grid:
    print(r)
print(possibleObstructions)
print(len(possibleObstructions) - 1)
