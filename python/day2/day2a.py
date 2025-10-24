#!/usr/bin/env python3

import os

inputFile = open ('./python/day2/input.txt', 'r')
data = inputFile.read ()
inputFile.close ()

test = '''7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9'''
#safeReports == 2
#data = test

lines = data.splitlines ()

max_change = 3

safeReports = 0

for line in lines:
	levels = list (map (int, line.split ()))
	safe = True
	increasing = False
	decreasing = False
	lastLevel = levels.pop (0)
	for level in levels:
		if (abs (level - lastLevel) > max_change):
			safe = False
		if (increasing):
			if (level <= lastLevel):
				safe = False
		elif (decreasing):
			if (level >= lastLevel):
				safe = False
		else:
			if (level == lastLevel):
				safe = False
			elif (level < lastLevel):
				decreasing = True
			elif (level > lastLevel):
				increasing = True
		lastLevel = level
	if (safe):
		safeReports += 1

print (safeReports)

