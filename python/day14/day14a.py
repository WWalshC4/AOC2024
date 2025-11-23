#!/usr/bin/env python3

import os
import re

inputFile = open("./input.txt", "r")
data = inputFile.read()
inputFile.close()

test = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""
# totalSafetyFactor == 12
# testwidth = 11
# testheight = 7
# data = test

width = 101
height = 103

pattern = r"p=(\d+),(\d+) v=(\-?\d+),(\-?\d+)"

robots = []

for match in re.finditer(pattern, data):
    robot = {
        "xPos": int(match.group(1)),
        "yPos": int(match.group(2)),
        "xDiff": int(match.group(3)),
        "yDiff": int(match.group(4)),
    }
    robots.append(robot)


def iterateRobot(robot):
    nextXPos = robot["xPos"] + robot["xDiff"]
    nextYPos = robot["yPos"] + robot["yDiff"]

    while nextXPos < 0:
        nextXPos = nextXPos + width
    while nextXPos >= width:
        nextXPos = nextXPos - width

    while nextYPos < 0:
        nextYPos = nextYPos + height
    while nextYPos >= height:
        nextYPos = nextYPos - height

    robot["xPos"] = nextXPos
    robot["yPos"] = nextYPos


def checkRobots():
    tl = 0
    tr = 0
    bl = 0
    br = 0

    grid = [["."] * width for i in range(height)]

    for robot in robots:
        if grid[robot["yPos"]][robot["xPos"]] == ".":
            grid[robot["yPos"]][robot["xPos"]] = 0
        grid[robot["yPos"]][robot["xPos"]] += 1
        middleColumn = int(width / 2)
        middleRow = int(height / 2)

        if robot["xPos"] < middleColumn:
            if robot["yPos"] < middleRow:
                tl += 1
            elif robot["yPos"] > middleRow:
                bl += 1
        elif robot["xPos"] > middleColumn:
            if robot["yPos"] < middleRow:
                tr += 1
            elif robot["yPos"] > middleRow:
                br += 1
    safetyFactor = tl * tr * bl * br

    for gridline in grid:
        print("".join(list(map(str, gridline))))
    return safetyFactor


iterations = 100

for iteration in range(iterations):
    for robot in robots:
        iterateRobot(robot)

safetyFactor = checkRobots()
print(safetyFactor)
