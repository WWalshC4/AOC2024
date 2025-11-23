#!/usr/bin/env python3

import os
import re

inputFile = open("./input.txt", "r")
data = inputFile.read()
inputFile.close()

test = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""
# minimumWinTokens == 480
# data = test

costA = 3
costB = 1

clawMachines = []

pattern = r"Button A: X([\+\-]?\d+), Y([\+\-]?\d+)\nButton B: X([\+\-]?\d+), Y([\+\-]?\d+)\nPrize: X=(\d+), Y=(\d+)"

for match in re.finditer(pattern, data):
    clawMachine = {
        "aX": int(match.group(1)),
        "aY": int(match.group(2)),
        "bX": int(match.group(3)),
        "bY": int(match.group(4)),
        "targetX": int(match.group(5)),
        "targetY": int(match.group(6)),
    }
    clawMachines.append(clawMachine)

maxPresses = 100
maxPrice = (maxPresses + 1) * (costA + costB)


def getWinConditions(clawMachine):
    winConditions = []
    for aCount in range(maxPresses):
        for bCount in range(maxPresses):
            x = (clawMachine["aX"] * aCount) + (clawMachine["bX"] * bCount)
            y = (clawMachine["aY"] * aCount) + (clawMachine["bY"] * bCount)
            if x > clawMachine["targetX"] or y > clawMachine["targetY"]:
                break
            if x == clawMachine["targetX"] and y == clawMachine["targetY"]:
                price = (aCount * costA) + (bCount * costB)
                winConditions.append(
                    {"aCount": aCount, "bCount": bCount, "price": price}
                )

    return winConditions


minimumWinTokens = 0

for clawMachine in clawMachines:
    winConditions = getWinConditions(clawMachine)
    minPrice = maxPrice
    for winCondition in winConditions:
        if winCondition["price"] < minPrice:
            minPrice = winCondition["price"]
    if minPrice < maxPrice:
        minimumWinTokens += minPrice

print(minimumWinTokens)
