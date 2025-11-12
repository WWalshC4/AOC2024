#!/usr/bin/env python3

import os

inputFile = open ('./python/day4/input.txt', 'r')
data = inputFile.read ()
inputFile.close ()

test = '''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX'''
#totalCount == 9
#data = test

totalCount = 0

grid = []

lines = data.splitlines ()

for line in lines:
	gridline = list (line)
	grid.append (gridline)

def checkDirection (xPos, yPos):
	if (xPos < 1):
		return False
	if (yPos < 1):
		return False
	if (yPos + 1 >= len (grid)):
		return False
	row = grid [yPos]
	if (xPos + 1 >= len (row)):
		return False

	tl = grid [yPos - 1][xPos - 1]
	tr = grid [yPos - 1][xPos + 1]
	bl = grid [yPos + 1][xPos - 1]
	br = grid [yPos + 1][xPos + 1]

	if (not (tl == 'M' or tl == 'S')):
		return False
	if (not (tr == 'M' or tr == 'S')):
		return False
	if (not (bl == 'M' or bl == 'S')):
		return False
	if (not (br == 'M' or br == 'S')):
		return False
	if (tl == br):
		return False
	if (tr == bl):
		return False
	return True

#	if (tl == 'M'):
#		if (br == 'S'):
#			if (tr == 'M'):
#				if (bl == 'S'):
#					return True
#				else:
#					return False
#			elif (tr == 'S'):
#				if (bl == 'M'):
#					return True
#				else:
#					return False
#			else:
#				return False
#		else:
#			return False
#	elif (tl == 'S'):
#		if (br == 'M'):
#			if (tr == 'M'):
#				if (bl == 'S'):
#					return True
#				else:
#					return False
#			elif (tr == 'S'):
#				if (bl == 'M'):
#					return True
#				else:
#					return False
#			else:
#				return False
#		else:
#			return False
#	else:
#		return False

for yPos, row in enumerate (grid):
	for xPos, letter in enumerate (row):
		if (letter == 'A'):
			xmas = checkDirection (xPos, yPos)
			if (xmas):
				totalCount += 1

print (totalCount)
