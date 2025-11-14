#!/usr/bin/env python3

import os

inputFile = open ('./python/day5/input.txt', 'r')
data = inputFile.read ()
inputFile.close ()

test = '''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47'''
#totalOfCorrectMiddlePages == 143
#totalOfFixedMiddlePages == 123
data = test

totalOfCorrectMiddlePages = 0
totalOfFixedMiddlePages = 0

sections = data.split ('\n\n')

rulesRaw = sections [0].splitlines ()
printRunsRaw = sections [1].splitlines ()

rulesByBefore = {}
rulesByAfter = {}

for rule in rulesRaw:
	ruleData = list (map (int, rule.split ('|')))
	before = ruleData [0]
	after = ruleData [1]
	if not before in rulesByBefore:
		rulesByBefore [before] = {}
	if not after in rulesByAfter:
		rulesByAfter [after] = {}
	rulesByBefore [before] [after] = True
	rulesByAfter [after] [before] = True

printRuns = []

for printRunRaw in printRunsRaw:
	printRun = list (map (int, printRunRaw.split (',')))
	printRuns.append (printRun)

printRunsToBeFixed = []

for printRun in printRuns:
	valid = True
	pagesSeen = {}
	for page in printRun:
		for seenPage in pagesSeen:
			if (page in rulesByBefore and seenPage in rulesByBefore [page]):
				valid = False
		pagesSeen [page] = True
	if (valid):
		middlePos = int(len (printRun) / 2) #0 indexed!
		middlePage = printRun [middlePos]
		totalOfCorrectMiddlePages += middlePage
	else:
		printRunsToBeFixed.append (printRun)

print (printRunsToBeFixed)

print (totalOfFixedMiddlePages)
