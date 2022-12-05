filename = "input.txt"
with open(filename) as f:
    calories = f.readlines()
f.close()

sumCalories = 0
mostCalories = 0

for calorie in calories:
    if calorie == "\n":
        if(sumCalories > mostCalories):
            mostCalories = sumCalories
        sumCalories = 0
    else:
        sumCalories = sumCalories + int(calorie)

print(mostCalories)