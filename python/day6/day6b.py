#!/usr/bin/env python3

import os, copy

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
# distinctPositions == 41
# len (possibleObstructions) == 6
# data = test

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
            grid[initialRow][initialColumn] = "."
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

def checkPath(checkGrid, row, column, direction):
    ### maybe we need to just write something to the value that says "this is speculative for this direction?"
    ### stop using single hex char, start using whole byte
    return dict(shouldMove=False, loop=False)
    thisPos = checkGrid[row][column]
    newVal = getChar(thisPos, direction)
    if thisPos == newVal:
        return dict(shouldMove=False, loop=True)
    checkGrid[row][column] = newVal

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
        return dict(shouldMove=False, loop=False)
    if nextRow >= len(checkGrid) or nextColumn >= (len(checkGrid[row])):
        return dict(shouldMove=False, loop=False)

    nextPos = checkGrid[nextRow][nextColumn]

    if nextPos == "#":
        nextRow = row
        nextColumn = column
        direction = direction + 1
        if direction == 4:
            direction = 0
    else:
        row = nextRow
        column = nextColumn

    return dict(
        shouldMove=True,
        nextColumn=nextColumn,
        nextRow=nextRow,
        nextDirection=direction,
    )


def move(regGrid, direction, row, column):
    newPosition = False
    thisPos = regGrid[row][column]
    if thisPos == ".":
        newPosition = True

    newVal = getChar(thisPos, direction)
    if thisPos == newVal:
        return dict(shouldMove=False, loop=True, newPosition=newPosition)

    regGrid[row][column] = getChar(thisPos, direction)

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
        return dict(shouldMove=False, loop=False, newPosition=newPosition)
    if nextRow >= len(regGrid) or nextColumn >= (len(regGrid[row])):
        return dict(shouldMove=False, loop=False, newPosition=newPosition)

    nextPos = regGrid[nextRow][nextColumn]

    if nextPos == "#":
        nextRow = row
        nextColumn = column
        direction = direction + 1
        if direction == 4:
            direction = 0
    else:
        whatIfDirection = direction + 1
        if whatIfDirection == 4:
            whatIfDirection = 0

        whatIfRow = row
        whatIfColumn = column

        shouldMove = True
        obstructionLocation = [nextRow, nextColumn]
        if obstructionLocation in possibleObstructions:
            shouldMove = False

        if shouldMove:
            checkGrid = regGrid
            #checkGrid = copy.deepcopy(regGrid)
            checkGrid[nextRow][nextColumn] = "#"

            while shouldMove:
                ret = checkPath(checkGrid, whatIfRow, whatIfColumn, whatIfDirection)
                shouldMove = ret["shouldMove"]
                if shouldMove:
                    whatIfDirection = ret["nextDirection"]
                    whatIfRow = ret["nextRow"]
                    whatIfColumn = ret["nextColumn"]
                else:
                    loop = ret["loop"]
                    if loop:
                        possibleObstructions.append(obstructionLocation)
            checkGrid[nextRow][nextColumn] = nextPos
        row = nextRow
        column = nextColumn

    return dict(
        shouldMove=True,
        nextColumn=nextColumn,
        nextRow=nextRow,
        nextDirection=direction,
        newPosition=newPosition,
    )


shouldMove = True
direction = initialDirection
row = initialRow
column = initialColumn
distinctPositions = 0
while shouldMove:
    ret = move(grid, direction, row, column)
    shouldMove = ret["shouldMove"]
    newPosition = ret["newPosition"]
    if newPosition:
        distinctPositions += 1
    if shouldMove:
        direction = ret["nextDirection"]
        row = ret["nextRow"]
        column = ret["nextColumn"]
    else:
        print(ret)

print(distinctPositions)
print(len(possibleObstructions) - 1) #remove the one we added at the starting location
