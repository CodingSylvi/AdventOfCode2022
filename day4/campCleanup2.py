def overlap(first, second):
    for f in first:
        for s in second:
            if f == s:
                return True
    return False


filename = "input.txt"
with open(filename) as f:
    pairs = f.readlines()
f.close()

overlaps = 0

for p in pairs:
    elves = p.split(",")

    firstElve = []
    secondElve = []

    elve1 = elves[0]
    bottom = int(elve1.split("-")[0])
    top = int(elve1.split("-")[1])
    for i in range(bottom, top+1):
        firstElve.append(i)

    elve2 = elves[1]
    bottom = int(elve2.split("-")[0])
    top = int(elve2.split("-")[1])
    for i in range(bottom, top+1):
        secondElve.append(i)
    
    overlaps += overlap(firstElve, secondElve)

print("number of overlaps = " + str(overlaps))
