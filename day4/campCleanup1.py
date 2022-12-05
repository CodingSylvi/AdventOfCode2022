filename = "input.txt"
with open(filename) as f:
    pairs = f.readlines()
f.close()

subsets = 0

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

    if set(firstElve) <= set(secondElve):
        subsets += 1
    elif set(secondElve) <= set(firstElve):
        subsets += 1

print("number of subsets = " + str(subsets))
