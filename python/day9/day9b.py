#!/usr/bin/env python3

import os

inputFile = open("./input.txt", "r")
data = inputFile.read()
inputFile.close()

test = """2333133121414131402"""
# checksum == 1928
data = test

data = data.strip()


def processDiskMap(diskMap):
    idStartsBySize = {}
    freeSpaceStartsBySize = {}

    id = 0
    isFile = True
    currentPosInDisk = 0

    for letter in diskMap:
        size = int(letter)

        if isFile:
            if not size in idStartsBySize:
                idStartsBySize[size] = []

            idStartsBySize[size].append({"pos": currentPosInDisk, "id": id})
            id += 1
        else:
            if not size in freeSpaceStartsBySize:
                freeSpaceStartsBySize[size] = []
            freeSpaceStartsBySize[size].append(currentPosInDisk)
        isFile = not (isFile)
        currentPosInDisk += size

    return idStartsBySize, freeSpaceStartsBySize


def optimize(idStartsBySize, newIdStartsBySize, freeSpaceStartsBySize):

    highestPosFound = -1
    highestPosSize = -1
    for size in idStartsBySize:
        try:
            lastFile = idStartsBySize[size][-1]
        except:
            continue
        pos = lastFile["pos"]
        if pos > highestPosFound:
            highestPosSize = size

    if highestPosFound == -1 and highestPosSize == -1:
        print("could not find highest pos")
        return False

    fileToProcess = idStartsBySize[size].pop()
    if len(idStartsBySize[size]) == 0:
        del idStartsBySize[size]

    earliestFreeSpaceFound = highestPosFound
    earliestFreeSpaceSize = 0

    # print("highestPosSize" + str(highestPosSize))
    for size in freeSpaceStartsBySize:
        # print("freeSpaceStartsBySize" + str(size))
        freeSpacePos = freeSpaceStartsBySize[size][0]
        if size >= highestPosSize:
            if freeSpacePos < earliestFreeSpaceFound:
                earliestFreeSpaceFound = freeSpacePos
                earliestFreeSpaceSize = size

    if earliestFreeSpaceFound == highestPosFound:
        if not highestPosSize in newIdStartsBySize:
            newIdStartsBySize[highestPosSize] = []
        newIdStartsBySize[highestPosSize].append(fileToProcess)
        # print("could not find earlier free space")
        return False

    remainingSpace = earliestFreeSpaceSize - highestPosSize
    if remainingSpace > 0:
        if not remainingSpace in freeSpaceStartsBySize:
            freeSpaceStartsBySize[remainingSpace] = []
        freeSpaceStartsBySize[remainingSpace].append(
            earliestFreeSpaceFound + highestPosSize
        )
        freeSpaceStartsBySize[remainingSpace].sort()
    fileToProcess["pos"] = earliestFreeSpaceFound
    if not highestPosSize in newIdStartsBySize:
        newIdStartsBySize[highestPosSize] = []
    newIdStartsBySize[highestPosSize].append(fileToProcess)
    return True


def getChecksum(diskLayout):
    checksum = 0
    for index in range(len(diskLayout)):
        value = diskLayout[index]
        if value == ".":
            continue
        checksum += index * value
    return checksum


idStartsBySize, freeSpaceStartsBySize = processDiskMap(data)
newIdStartsBySize = {}
print(idStartsBySize)
while len(idStartsBySize) > 0:
    optimize(idStartsBySize, newIdStartsBySize, freeSpaceStartsBySize)
print(newIdStartsBySize)

# checksum = getChecksum(diskLayout)

# print(checksum)
