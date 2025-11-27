#!/usr/bin/env python3

import os

inputFile = open("./input.txt", "r")
data = inputFile.read()
inputFile.close()

test = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
# totalTrueResults == 3749
# data = test


def test(target, currentTotal, values, chain):
    pos = len(chain) + 1
    if pos == len(values):
        # print (chain, currentTotal, target)
        if currentTotal == target:
            return True
        else:
            return False

    nextValue = values[pos]
    plus = currentTotal + nextValue
    times = currentTotal * nextValue

    validPlus = None
    validTimes = None

    if plus <= target:
        validPlus = test(target, plus, values, chain + "+")
    if times <= target:
        validTimes = test(target, times, values, chain + "*")

    if validPlus or validTimes:
        return True


def processLine(line):
    line = line.replace(":", "")
    values = list(map(int, line.split()))
    targetResult = values.pop(0)
    firstValue = values[0]
    correctResult = test(targetResult, firstValue, values, "")
    if correctResult:
        return targetResult
    else:
        return 0


totalTrueResults = 0

lines = data.splitlines()
for line in lines:
    result = processLine(line)
    if result >= 0:
        totalTrueResults += result

print(totalTrueResults)
