#!/usr/bin/env python3

import os

inputFile = open("./input.txt", "r")
data = inputFile.read()
inputFile.close()

test = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
# totalPrice == 1930
# data = test

grid = []

regions = []

lines = data.splitlines()

for line in lines:
    gridline = list(line)
    grid.append(gridline)

maxY = len(grid)
maxX = len(grid[0])


def consumeRegion(xPos, yPos, region):
    region["positions"].append([xPos, yPos])
    grid[yPos][xPos] = None
    for xDiff in range(-1, 2):
        for yDiff in range(-1, 2):
            if abs(xDiff) == abs(yDiff):
                continue
            newX = xPos + xDiff
            newY = yPos + yDiff
            if not (0 <= newX < maxX and 0 <= newY < maxY):
                region["edges"] += 1
                continue
            if [newX, newY] in region["positions"]:
                continue

            nextPlot = grid[newY][newX]
            if nextPlot == region["plot"]:
                consumeRegion(newX, newY, region)
            else:
                region["edges"] += 1


for yPos, row in enumerate(grid):
    for xPos, plot in enumerate(row):
        if plot != None:
            region = {"plot": plot, "positions": [], "edges": 0}
            consumeRegion(xPos, yPos, region)
            regions.append(region)


def calculateArea(region):
    return len(region["positions"])


def calculatePerimeter(region):
    return region["edges"]


totalPrice = 0

for region in regions:
    area = calculateArea(region)
    perimeter = calculatePerimeter(region)
    price = area * perimeter
    totalPrice += price

print(totalPrice)
