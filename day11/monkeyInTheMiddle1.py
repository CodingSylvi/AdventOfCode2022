def calculate(old, operator, number):
    if number == "old":
        number = old
        
    if operator == "+":
        return int(old) + int(number)
    elif operator == "-":
        return int(old) - int(number)
    elif operator == "*":
        return int(old) * int(number)

def printItems(monkeyList):
    for monkey in monkeyList:
        print(monkey[0])

filename = "input.txt"
with open(filename) as f:
    lines = f.readlines()
f.close()

monkeyList = []
monkey = [] # items, operator, number, test, true, false, numberOfInspections
items = []

for line in lines:
    if line.strip() == "":
        monkey.append(0)
        monkeyList.append(monkey)
        monkey = []
        items = []
    else:
        parts = line.split()
        if parts[0] == "Starting":
            p = line.split(":")
            items = p[1].strip().split(",")
            intItems = []
            for i in items:
                intItems.append(int(i))
            monkey.append(intItems)
        if parts[0] == "Operation:":
            monkey.append(parts[4])
            monkey.append(parts[5])
        if parts[0] == "Test:":
            monkey.append(parts[3])
        if parts[1] == "true:":
            monkey.append(parts[5])
        if parts[1] == "false:":
            monkey.append(parts[5])
monkey.append(0)
monkeyList.append(monkey)

prime = 1
for m in range(len(monkeyList)):
    prime = prime * int(monkeyList[m][3])

rounds = 20
for round in range(rounds):
    for m in range(len(monkeyList)):
        for item in monkeyList[m][0].copy():
            monkeyList[m][6] += 1
            new = calculate(item, monkeyList[m][1], monkeyList[m][2])
            new = int(new / 3)
            if new % prime == 0:
                toMonkey = int(monkeyList[m][4])
                monkeyList[toMonkey][0].append(new)
                monkeyList[m][0].remove(item)
            else:
                toMonkey = int(monkeyList[m][5])
                monkeyList[toMonkey][0].append(new)
                monkeyList[m][0].remove(item)

mostInspections = 0
secondMostInspections = 0
for monkey in monkeyList:
    timesInspected = monkey[6]
    if timesInspected > mostInspections:
        mostInspections = timesInspected
for monkey in monkeyList:
    timesInspected = monkey[6]
    if timesInspected > secondMostInspections and timesInspected < mostInspections:
        secondMostInspections = timesInspected
levelOfMonkeyBusiness = mostInspections * secondMostInspections

print("level of monkey business = " + str(levelOfMonkeyBusiness))
