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

filename = "input.txt"
with open(filename) as f:
    rucksacks = f.readlines()
f.close()

sumOfPoints = 0
for r in rucksacks:
    # split line in half
    firstpart, secondpart = r[:len(r)//2], r[len(r)//2:]

    # compare first and second part for same letters
    sameLetter = ""
    for fp in firstpart:
        for sp in secondpart:
            if(fp == sp):
                sameLetter = fp

    # calculate the points of the same letters     
    pointsOfSameLetter = caluclatePoints(sameLetter)
    sumOfPoints += pointsOfSameLetter

print("sum of points = " + str(sumOfPoints))
