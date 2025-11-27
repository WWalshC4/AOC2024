#!/usr/bin/env python3

import os

inputFile = open("./input.txt", "r")
data = inputFile.read()
inputFile.close()

test = """2333133121414131402"""
# checksum == 1928
# data = test


def processDiskMap(diskMap):
    isFile = True
    diskLayout = []
    freeSpaceLocations = []
    id = 0
    for letter in diskMap:
        start = len(diskLayout)
        try:
            size = int(letter)
        except:
            # input file has a newline, use this to indicate we're done
            return diskLayout, freeSpaceLocations
        value = "."
        if isFile:
            value = id
            id += 1
        else:
            for i in range(size):
                freeSpaceLocations.append(start + i)
        isFile = not (isFile)
        thisChunk = [value] * size

        diskLayout.extend(thisChunk)
    return diskLayout, freeSpaceLocations


def optimize(diskLayout, freeSpaceLocations):
    for index in range(len(diskLayout) - 1, -1, -1):
        value = diskLayout[index]
        if value == ".":
            freeSpaceLocations.pop()
            continue

        try:
            firstFreeSpaceLocation = freeSpaceLocations.pop(0)
        except:
            return diskLayout
        if firstFreeSpaceLocation > index:
            return diskLayout

        diskLayout[index] = "."
        diskLayout[firstFreeSpaceLocation] = value
    return diskLayout


def getChecksum(diskLayout):
    checksum = 0
    for index in range(len(diskLayout)):
        value = diskLayout[index]
        if value == ".":
            continue
        checksum += index * value
    return checksum


diskLayout, freeSpaceLocations = processDiskMap(data)
diskLayout = optimize(diskLayout, freeSpaceLocations)
checksum = getChecksum(diskLayout)

print(checksum)
