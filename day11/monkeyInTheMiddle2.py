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

filename = "input_simple.txt"
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

rounds = 10000
for round in range(1, rounds+1):
    for m in range(len(monkeyList)):
        #print("Monkey " + str(m))
        for item in monkeyList[m][0].copy():
            monkeyList[m][6] += 1
            new = calculate(item, monkeyList[m][1], monkeyList[m][2])
            if new % prime == 0:
                toMonkey = int(monkeyList[m][4])
                monkeyList[toMonkey][0].append(new)
                monkeyList[m][0].remove(item)
                #print("\tthrow " + item + " to " + toMonkey)
            else:
                toMonkey = int(monkeyList[m][5])
                monkeyList[toMonkey][0].append(new)
                monkeyList[m][0].remove(item)
                #print("\tthrow " + str(item) + " to " + str(toMonkey))
    #printItems(monkeyList)

    if round == 1 or round == 20 or round == 1000 or round == 2000 or round == 3000 or round == 4000 or round == 5000 or round == 6000 or round == 7000 or round == 8000 or round == 9000 or round == 10000:
        #print("== After round " + str(round) + " ==")
        for m in range(len(monkeyList)):
            timesInspected = monkeyList[m][6]
            #print("Monkey " + str(m) + " inspected items " + str(timesInspected) + " times") 

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
