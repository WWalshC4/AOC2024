#!/usr/bin/env python3

import os

inputFile = open ('./python/day1/input.txt', 'r')
data = inputFile.read ()
inputFile.close ()

test = '''3   4
4   3
2   5
1   3
3   9
3   3'''
#totalDistance == 11
#data = test

left = []
right = []

lines = data.splitlines ()
for line in lines:
	locationIds = line.split ()
	left.append (locationIds [0])
	right.append (locationIds [1])

left.sort ()
right.sort ()

totalDistance = 0
for i, leftElement in enumerate (left):
	rightElement = right [i]
	difference = abs (int (rightElement) - int (leftElement))
	totalDistance += difference

print (totalDistance)
