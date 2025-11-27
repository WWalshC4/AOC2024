#!/usr/bin/env python3

import os

inputFile = open("./input.txt", "r")
data = inputFile.read()
inputFile.close()

test = """125 17"""
# stoneCount25 == 55312
# data = test

cache = {}


def blink(stone):
    newstones = []
    stoneString = str(stone)
    if stone == 0:
        newstones.append(1)
    elif len(stoneString) % 2 == 0:
        half = int(len(stoneString) / 2)
        newstones.append(int(stoneString[:half]))
        newstones.append(int(stoneString[half:]))
    else:
        newstones.append(stone * 2024)
    return newstones


def getCountAfterBlinks(stone, blinks):
    if blinks < 1:
        return 0

    try:
        thisStoneCache = cache[stone]
    except:
        cache[stone] = {}

    try:
        thisStoneBlinkCache = cache[stone][blinks]
        return thisStoneBlinkCache
    except:
        pass

    nextStones = blink(stone)
    nextStonesCount = len(nextStones)
    cache[stone][1] = nextStonesCount
    if blinks == 1:
        return nextStonesCount

    thisStoneCount = 0
    for nextStone in nextStones:
        thisStoneCount += getCountAfterBlinks(nextStone, blinks - 1)

    cache[stone][blinks] = thisStoneCount

    return thisStoneCount


startingStones = list(map(int, data.split()))

stoneCount = 0
blinkCount = 75
for stone in startingStones:
    stoneCount += getCountAfterBlinks(stone, blinkCount)

print(stoneCount)

# for stoneCache in cache:
#    print(stoneCache, cache[stoneCache])
