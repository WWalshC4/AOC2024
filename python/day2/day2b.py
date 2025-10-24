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
#safeReports == 4
#data = test

lines = data.splitlines ()

max_change = 3

safeReports = 0

reports = []
unsafeReports = []

for line in lines:
	reports.append (list (map (int, line.split ())))

def checkReport (levels):
	safe = True
	increasing = False
	decreasing = False
	lastLevel = levels.pop (0)
	firstLevel = lastLevel
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
	levels.insert (0, firstLevel)
	return safe

for report in reports:
	safe = checkReport (report)
	if (safe):
		safeReports += 1
	else:
		unsafeReports.append (report)

for report in unsafeReports:
	safe = False
	index = 0
	for level in report:
		rem = report.pop (index)
		withRemoveSafe = checkReport (report)
		report.insert (index, rem)
		if (withRemoveSafe):
			safe = True
		index += 1
	if (safe):
		safeReports += 1

print (safeReports)

