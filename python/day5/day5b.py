#!/usr/bin/env python3

from functools import cmp_to_key

import os

inputFile = open("./input.txt", "r")
data = inputFile.read()
inputFile.close()

test = """47|53
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
97,13,75,29,47"""
# totalOfCorrectMiddlePages == 143#
# totalOfFixedMiddlePages == 123
# data = test

totalOfCorrectMiddlePages = 0
totalOfFixedMiddlePages = 0

sections = data.split("\n\n")

rulesRaw = sections[0].splitlines()
printRunsRaw = sections[1].splitlines()

rulesByBefore = {}
rulesByAfter = {}

pageNumbersMap = {}

for rule in rulesRaw:
    ruleData = list(map(int, rule.split("|")))
    before = ruleData[0]
    after = ruleData[1]
    if not before in rulesByBefore:
        rulesByBefore[before] = {}
    if not after in rulesByAfter:
        rulesByAfter[after] = {}

    if not before in pageNumbersMap:
        pageNumbersMap[before] = True
    if not after in pageNumbersMap:
        pageNumbersMap[after] = True
    rulesByBefore[before][after] = True
    rulesByAfter[after][before] = True


def compare(page1, page2):
    value = 0
    # 	print (str(page1) + ':' + str(page2))
    if page1 in rulesByBefore and page2 in rulesByBefore[page1]:
        if not (value == 0 or value == -1):
            print("conflict rule a:" + str(page1) + ":" + str(page2))
        value = -1
    elif page2 in rulesByAfter and page1 in rulesByAfter[page2]:
        if not (value == 0 or value == -1):
            print("conflict rule b:" + str(page1) + ":" + str(page2))
        value = -1
    elif page2 in rulesByBefore and page1 in rulesByBefore[page2]:
        if not (value == 0 or value == 1):
            print("conflict rule c:" + str(page1) + ":" + str(page2))
        value = 1
    elif page1 in rulesByAfter and page2 in rulesByAfter[page1]:
        if not (value == 0 or value == 1):
            print("conflict rule d:" + str(page1) + ":" + str(page2))
        value = 1
    else:
        print("unknown rule: " + str(page1) + ":" + str(page2))
        value = 0
    return value


pageNumberOrder = sorted(list(pageNumbersMap), key=cmp_to_key(compare))

printRuns = []

for printRunRaw in printRunsRaw:
    printRun = list(map(int, printRunRaw.split(",")))
    printRuns.append(printRun)

printRunsToBeFixed = []

for printRun in printRuns:
    sortedPrintRun = sorted(printRun, key=cmp_to_key(compare))
    if printRun == sortedPrintRun:
        middlePos = int(len(printRun) / 2)  # 0 indexed!
        middlePage = printRun[middlePos]
        totalOfCorrectMiddlePages += middlePage
    else:
        printRunsToBeFixed.append(printRun)

for printRun in printRunsToBeFixed:
    fixedPrintRun = sorted(printRun, key=cmp_to_key(compare))
    middlePos = int(len(fixedPrintRun) / 2)  # 0 indexed!
    middlePage = fixedPrintRun[middlePos]
    totalOfFixedMiddlePages += middlePage

print(totalOfCorrectMiddlePages)
print(totalOfFixedMiddlePages)
