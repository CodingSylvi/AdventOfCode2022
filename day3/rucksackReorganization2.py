import string

def caluclatePoints(letter):
    pointsOfSameLetter = 0
    allLetters = string.ascii_letters
    i=1
    for al in allLetters:
        if(al == letter):
            pointsOfSameLetter = i
        i += 1

    return pointsOfSameLetter

def addThreeRows(list_):
    return [list_[i:i+3] for i in range(0, len(list_), 3)]

def findBadge(firstRucksack, secondRucksack, thirdRucksack):
    for fr in firstRucksack:
        for sr in secondRucksack:
            for tr in thirdRucksack:
                if fr == sr == tr:
                    return fr

filename = "input.txt"
with open(filename) as f:
    rucksacks = f.readlines()
f.close()

sumOfPoints = 0

allRucksacks = addThreeRows(rucksacks)

for group in allRucksacks:

    firstRucksack = ""
    secondRucksack = ""
    thirdRucksack = ""
    i = 1
    for rucksack in group:
        if i==1:
            firstRucksack = rucksack
        elif i==2:
            secondRucksack = rucksack
        elif i==3:
            thirdRucksack = rucksack
        i += 1
    
    badge = findBadge(firstRucksack, secondRucksack, thirdRucksack)
                    
    pointsOfBadge = caluclatePoints(badge)
    sumOfPoints += pointsOfBadge

print("sum of points = " + str(sumOfPoints))
