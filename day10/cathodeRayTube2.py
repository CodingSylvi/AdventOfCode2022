def X2Sprite(X):
    spritePosition = ""
    for i in range(1, 41):
        if i == X or i == X+1 or i == X+2:
            spritePosition += "#"
        else:
            spritePosition += "."
    return spritePosition

filename = "input.txt"
with open(filename) as f:
    lines = f.readlines()
f.close()

X = 1
cycles = 0
sumSignalStrengths = 0
currentCTRrow = ""
ctr = 0

for line in lines:
    parts = line.split()
    if line.strip() == "noop":
        cycles += 1
        if X2Sprite(X)[ctr] == "#":
            currentCTRrow += "#"
        else:
            currentCTRrow += "."
        ctr += 1
        if cycles==40 or cycles==80 or cycles==120 or cycles==160 or cycles==200 or cycles==240:
            print(currentCTRrow)
            currentCTRrow = ""
            ctr = 0
    elif parts[0] == "addx":
        cycles += 1
        if X2Sprite(X)[ctr] == "#":
            currentCTRrow += "#"
        else:
            currentCTRrow += "."
        ctr += 1
        if cycles==40 or cycles==80 or cycles==120 or cycles==160 or cycles==200 or cycles==240:
            print(currentCTRrow)
            currentCTRrow = ""
            ctr = 0

        cycles += 1
        if X2Sprite(X)[ctr] == "#":
            currentCTRrow += "#"
        else:
            currentCTRrow += "."
        ctr += 1
        if cycles==40 or cycles==80 or cycles==120 or cycles==160 or cycles==200 or cycles==240:
            print(currentCTRrow)
            currentCTRrow = ""
            ctr = 0

        X += int(parts[1])
