def move(stacks, quantity, fromStack, toStack): # CrateMover 9000
    for stack in range(1, len(stacks)+1):
        if stack == fromStack:
            for often in range(quantity):
                for sameStack in range(1, len(stacks)+1):
                    if(sameStack == toStack):
                        # moving
                        help = stacks[fromStack-1].pop(0)
                        stacks[toStack-1].insert(0, help)


filename = "input.txt"
with open(filename) as f:
    lines = f.readlines()
f.close()

rows = []
for line in lines:
    if not line.strip().startswith('['):
		# move ... to ... comes next
        break
    else:
        crates = []
        numberSpaces = 0
        for element in line:
            if element.isalpha(): #check if its a letter
                crates.append(element.strip())
                numberSpaces = 0
            elif element == ' ':
                numberSpaces += 1
            if  numberSpaces >= 4:
                numberSpaces = 0
                crates.append("NULL")
        rows.append(crates)

columns = [*zip(*rows)]

stacks = []
for column in columns:
    crates = []
    for element in column:
        if element != "NULL":
            crates.append(element)
    stacks.append(crates)

for line in lines:
    quantity = 0
    fromStack = 0
    toStack = 0
    if line.strip().startswith('move'):
        words = (line.strip()).split(" ")
        quantity = words[1]
        fromStack = words[3]
        toStack = words[5]
        move(stacks, int(quantity), int(fromStack), int(toStack)) # lifo queue

answer = ""
for stack in stacks:
    answer += stack[0]
print("answer = " + answer)
