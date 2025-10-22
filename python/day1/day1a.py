#!/usr/bin/env python3

test = '''3   4
4   3
2   5
1   3
3   9
3   3'''
#totalDistance == 11

left = []
right = []

data = test

lines = data.split ('\n')
for line in lines:
	locationIds = line.split ()
	left.append (locationIds [0])
	right.append (locationIds [1])

left.sort ()
right.sort ()

totalDistance = 0
for i, leftElement in enumerate (left):
	rightElement = right [i]
	difference = int (rightElement) - int (leftElement)
	totalDistance += difference

print (totalDistance)