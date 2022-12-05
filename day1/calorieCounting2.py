filename = "input.txt"
with open(filename) as f:
    calories = f.readlines()
f.close()

sumCalories = 0
mostCalories = 0
secondMostCalories = 0
thirdMostCalories = 0

elves = []

for calorie in calories:
    if calorie == "\n":
        elves.append(sumCalories)
        sumCalories = 0
    else:
        sumCalories = sumCalories + int(calorie)
elves.append(sumCalories)

for e in elves:
    if e > mostCalories:
        mostCalories = e

for e in elves:
    if (e > secondMostCalories) and (e < mostCalories):
        secondMostCalories = e

for e in elves:
    if (e > thirdMostCalories) and (e < secondMostCalories):
        thirdMostCalories = e

sumTopThreeCalories = mostCalories + secondMostCalories + thirdMostCalories
print("sum of the top three calorie-sums = " + str(sumTopThreeCalories))